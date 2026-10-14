const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const read = file => fs.readFileSync(path.join(root,file),'utf8');
const sandbox = {window:{}};
vm.runInNewContext(read('case-structure-data.js'),sandbox);
const examples = sandbox.window.RSL_CASE_EXAMPLES;
test('curated examples have valid answers and no duplicate Russian sentences',()=>{
 assert.ok(Array.isArray(examples) && examples.length>=3);
 assert.equal(new Set(examples.map(e=>e.ru)).size,examples.length);
 for(const e of examples){
  assert.ok(e.ru && e.jp && e.question && e.reason && e.explanation);
  assert.ok(Array.isArray(e.tokens) && e.tokens.every(t=>t.word && t.role));
  assert.ok(Array.isArray(e.choices) && e.choices.length>=3);
  assert.ok(Number.isInteger(e.correct) && e.correct>=0 && e.correct<e.choices.length);
  assert.ok(e.question.includes('_____'));
  assert.ok(e.ru.includes(e.choices[e.correct]), 'correct choice must occur in example: '+e.ru);
 }
});
test('main Learn navigation points to case explorer and back',()=>{
 assert.match(read('index.html'),/href="case-structure-explorer\.html"/);
 assert.match(read('case-structure-explorer.html'),/href="index\.html"/);
});
test('exercise loads data and protects explanations until success',()=>{
 const html=read('case-structure-explorer.html');
 assert.match(html,/src="case-structure-data\.js"/);
 assert.match(html,/解説は正解後に表示します/);
 assert.match(html,/if\(ok\)\{completed=true;el\('reason'\)\.textContent=d\.reason;/);
 assert.match(html,/if\(completed\)return/);
 assert.doesNotMatch(html,/localStorage\.(setItem|removeItem|clear)/);
});
