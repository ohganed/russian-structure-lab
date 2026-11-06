"""Contract and HTTP integration tests. No Ollama or network service needed."""
import copy
import json
import pathlib
import sys
import threading
import unittest
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from contract import ContractError, validate_material  # noqa: E402
from server import handler_factory  # noqa: E402

SOURCE = "Я читаю."
LESSON = {
    "schemaVersion": "1.0", "language": "ru", "originalText": SOURCE, "title": "Reading",
    "sentences": [{
        "id": "s1", "text": SOURCE, "stressedText": "Я чита́ю.",
        "ttsText": SOURCE, "overallMeaning": {"ja": "私は読んでいます", "en": "I am reading."},
        "words": [
            {"id": "w1", "surface": "Я", "stressed": "Я", "start": 0, "end": 1},
            {"id": "w2", "surface": "читаю", "stressed": "чита́ю", "start": 2, "end": 7},
        ],
        "chunks": [
            {"id": "c1", "text": "Я читаю", "start": 0, "end": 7, "wordIds": ["w1", "w2"],
             "meaningOrder": {"ja": "私は―読む", "en": "I — read"},
             "naturalMeaning": {"ja": "私は読んでいます", "en": "I am reading."}},
        ],
        "structure": {"tree": {"id": "n1", "refIds": ["w1", "w2"], "children": []}}
    }]
}


class ContractTests(unittest.TestCase):
    def test_accepts_valid(self):
        self.assertEqual(validate_material(copy.deepcopy(LESSON), SOURCE)["language"], "ru")

    def test_rejects_changed_original(self):
        with self.assertRaisesRegex(ContractError, "originalText"):
            validate_material(LESSON, "Я пишу.")

    def test_rejects_wrong_offset(self):
        lesson = copy.deepcopy(LESSON)
        lesson["sentences"][0]["words"][1]["start"] = 1
        with self.assertRaises(ContractError):
            validate_material(lesson, SOURCE)

    def test_rejects_changed_stress_spelling(self):
        lesson = copy.deepcopy(LESSON)
        lesson["sentences"][0]["words"][1]["stressed"] = "чета́ю"
        with self.assertRaisesRegex(ContractError, "stressed"):
            validate_material(lesson, SOURCE)

    def test_rejects_missing_sentence(self):
        lesson = copy.deepcopy(LESSON)
        original = SOURCE + " Я иду."
        lesson["originalText"] = original
        with self.assertRaisesRegex(ContractError, "unprocessed"):
            validate_material(lesson, original)

    def test_rejects_unknown_chunk_reference(self):
        lesson = copy.deepcopy(LESSON)
        lesson["sentences"][0]["chunks"][0]["wordIds"].append("missing")
        with self.assertRaisesRegex(ContractError, "unknown"):
            validate_material(lesson, SOURCE)

    def test_rejects_missing_word(self):
        lesson = copy.deepcopy(LESSON)
        lesson["sentences"][0]["words"].pop()
        with self.assertRaisesRegex(ContractError, "omit"):
            validate_material(lesson, SOURCE)

    def test_utf16_offset_emojis(self):
        original = "🙂 Я."
        lesson = copy.deepcopy(LESSON)
        lesson["originalText"] = original
        s = lesson["sentences"][0]
        s["text"] = s["stressedText"] = original
        s["words"] = [{"id": "w1", "surface": "Я", "start": 3, "end": 4}]
        s["chunks"] = [{"id": "c1", "text": "Я", "start": 3, "end": 4, "wordIds": ["w1"]}]
        s["structure"]["tree"]["refIds"] = ["w1"]
        validate_material(lesson, original)

    def test_keep_yo_when_adding_accent(self):
        from contract import remove_stress
        self.assertEqual(remove_stress("ёлка́"), "ёлка")


class StubProvider:
    def __init__(self, response):
        self.response = response

    def generate(self, original):
        return copy.deepcopy(self.response)


class HttpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.provider = StubProvider(LESSON)
        handler = handler_factory(cls.provider, "test-very-long-secret", None)
        cls.httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f"http://127.0.0.1:{cls.httpd.server_address[1]}/v1/analyze"

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()
        cls.thread.join()

    def request(self, token="test-very-long-secret", origin=None, host_override=None):
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        if origin is not None:
            headers["Origin"] = origin
        if host_override is not None:
            headers["Host"] = host_override
        req = Request(self.url, data=json.dumps({"originalText": SOURCE}).encode(),
                      headers=headers, method="POST")
        try:
            with urlopen(req, timeout=3) as resp:
                return resp.status, json.load(resp)
        except HTTPError as exc:
            return exc.code, json.load(exc)

    def test_success(self):
        status, body = self.request()
        self.assertEqual(status, 200)
        self.assertEqual(body["originalText"], SOURCE)

    def test_reject_unauthorized(self):
        self.assertEqual(self.request(token="wrong")[0], 401)

    def test_reject_browser_origin(self):
        self.assertEqual(self.request(origin="https://ohganed.github.io")[0], 403)

    def test_same_origin_browser_post(self):
        origin = self.url.rsplit("/", 2)[0]
        self.assertEqual(self.request(origin=origin)[0], 200)

    def test_reject_rebinding_host(self):
        self.assertEqual(self.request(host_override="not-localhost.example")[0], 403)

    def test_pilot_served_locally_with_nonce_and_private_token(self):
        url = self.url.replace("/v1/analyze", "/pilot")
        with urlopen(url, timeout=3) as response:
            html = response.read().decode("utf-8")
            csp = response.headers.get("Content-Security-Policy", "")
            self.assertEqual(response.status, 200)
            self.assertEqual(response.headers["Cache-Control"], "no-store")
        self.assertIn("const token=\\\"test-very-long-secret\\\";", html)
        self.assertIn("script-src 'nonce-", csp)
        self.assertIn("frame-ancestors 'none'", csp)
        self.assertNotIn("__RSL_NONCE__", html)
        self.assertNotIn("__RSL_TOKEN_JSON__", html)

    def test_foreign_site_cannot_read_pilot(self):
        req = Request(self.url.replace("/v1/analyze", "/pilot"),
                      headers={"Origin": "https://attacker.example"})
        with self.assertRaises(HTTPError) as caught:
            urlopen(req, timeout=3)
        self.assertEqual(caught.exception.code, 403)

    def test_health_does_not_expose_token(self):
        with urlopen(self.url.replace("/v1/analyze", "/health"), timeout=3) as response:
            raw = response.read().decode("utf-8")
        self.assertNotIn("test-very-long-secret", raw)

    def test_reject_invalid_generated_output(self):
        self.provider.response = {**LESSON, "originalText": "Changed"}
        try:
            status, body = self.request()
            self.assertEqual(status, 422)
            self.assertEqual(body["error"], "AI output rejected")
        finally:
            self.provider.response = LESSON


if __name__ == "__main__":
    unittest.main()
