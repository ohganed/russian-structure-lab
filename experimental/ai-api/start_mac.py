#!/usr/bin/env python3
"""Start the optional Mac-only Ollama UI; public GitHub Pages stays unchanged.

No external Python packages or OpenAI API keys needed.
"""
import json
import os
import platform
import secrets
import sys
import webbrowser
from http.server import ThreadingHTTPServer
from urllib.error import URLError
from urllib.request import urlopen

from server import OllamaProvider, handler_factory


def require_ollama(provider):
    try:
        with urlopen(provider.url + "/api/tags", timeout=4) as response:
            data = json.load(response)
    except (URLError, TimeoutError, OSError, ValueError) as exc:
        raise RuntimeError(
            "Ollamaに接続できません。MacでOllamaを起動してから再実行してください。"
        ) from exc
    names = [item.get("name") or item.get("model") for item in data.get("models", [])]
    if provider.model not in names:
        raise RuntimeError(
            f"モデル {provider.model} が見つかりません。"
            f" ターミナルで ollama pull {provider.model} を実行してください。"
            f" インストール済み: {', '.join(names) if names else '(なし)'}"
        )


def main():
    if platform.system() != "Darwin":
        raise SystemExit("この起動画面はMac専用です。通常APIのテストは別途実行できます。")
    try:
        provider = OllamaProvider()
        require_ollama(provider)
    except (RuntimeError, ValueError) as exc:
        raise SystemExit(str(exc)) from exc

    token = secrets.token_urlsafe(32)  # never commit, print or store the session token
    try:
        port = int(os.environ.get("RSL_PORT", "8766"))
        # Explicitly no RSL_ALLOWED_ORIGIN: only same-origin pilot can POST.
        with ThreadingHTTPServer(
            ("127.0.0.1", port), handler_factory(provider, token)
        ) as server:
            url = f"http://127.0.0.1:{port}/pilot"
            print("\nRussian Structure Lab · Mac Ollama Studio")
            print(f"モデル: {provider.model}")
            print("解析はこのMac内で行います。AI Materialへの取り込みはJSONコピー方式です。")
            print(f"ローカル画面: {url}")
            print("終了: Control+C\n", flush=True)
            if not webbrowser.open(url):
                print("ブラウザが自動で開かない場合は上記URLを開いてください。")
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                print("\n終了しました。", flush=True)
    except OSError as exc:
        raise SystemExit(
            f"ポート {port} を使用できません。別プロセスが使っていないか確認してください: {exc}"
        ) from exc


if __name__ == "__main__":
    main()
