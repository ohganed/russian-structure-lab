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

test('all six curated examples cover core case relationships',()=>{
 assert.equal(examples.length,6);
 const roles=examples.flatMap(e=>e.tokens.map(t=>t.role));
 for(const expected of ['主格','対格','生格','与格','造格','前置格']){
  assert.ok(roles.some(role=>role.includes(expected)),`missing case: ${expected}`);
 }
 for(const e of examples){
  assert.equal(e.question.split('_____').length,2,'exactly one blank per question');
  assert.equal(new Set(e.choices).size,e.choices.length,'choices must be distinct');
  assert.ok(e.tokens.map(t=>t.word).join(' ').replace(/\s+/g,' ').length>0);
 }
});
