const {test,expect}=require('@playwright/test');
const {spawn}=require('node:child_process');
let server;
test.beforeAll(async()=>{server=spawn('python3',['-m','http.server','8765','--bind','127.0.0.1'],{stdio:'ignore'});await new Promise(r=>setTimeout(r,900))});
test.afterAll(()=>{if(server)server.kill()});
test('case explorer loads, checks answer, and moves to next example',async({page})=>{
 await page.goto('http://127.0.0.1:8765/case-structure-explorer.html');
 await expect(page.locator('#sentence button')).toHaveCount(4);
 await expect(page.locator('#progress')).toContainText('1 / 6');
 await expect(page.locator('#reason')).toContainText('解説は正解後');
 const choices=page.locator('#choices button');
 await choices.nth(0).click();
 await expect(page.locator('#feedback')).toContainText('もう一度');
 await expect(page.locator('#reason')).toContainText('解説は正解後');
 await choices.nth(1).click();
 await expect(page.locator('#feedback')).toContainText('正解');
 await expect(choices.nth(1)).toBeDisabled();
 await page.locator('#next').click();
 await expect(page.locator('#progress')).toContainText('2 / 6');
 await expect(page.locator('#feedback')).toBeEmpty();
});
test('canonical Learn links to case explorer',async({page})=>{
 await page.goto('http://127.0.0.1:8765/index.html');
 await page.locator('a[href="case-structure-explorer.html"]').click();
 await expect(page).toHaveURL(/case-structure-explorer\.html$/);
 await page.getByRole('link',{name:/Learn に戻る/}).click();
 await expect(page).toHaveURL(/index\.html$/);
});

test('mobile touch viewport and audio failure are handled',async({browser})=>{
 const context=await browser.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true});
 const page=await context.newPage();
 await page.goto('http://127.0.0.1:8765/case-structure-explorer.html');
 await expect(page.locator('#sentence button').first()).toHaveAttribute('aria-label',/を聞く/);
 const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth);
 expect(overflow).toBe(false);
 await page.locator('#listen').tap();
 await expect(page.locator('#sentence button').first()).toBeVisible();
 await context.close();
});

test('retry resets a completed answer and explanation',async({page})=>{
 await page.goto('http://127.0.0.1:8765/case-structure-explorer.html');
 const choices=page.locator('#choices button');
 await choices.nth(1).click();
 await expect(page.locator('#reason')).not.toContainText('解説は正解後');
 await expect(choices.nth(1)).toBeDisabled();
 await page.locator('#retry').click();
 await expect(page.locator('#reason')).toContainText('解説は正解後');
 await expect(page.locator('#feedback')).toBeEmpty();
 await expect(choices.nth(1)).toBeEnabled();
 await choices.nth(1).click();
 await expect(page.locator('#feedback')).toContainText('正解');
});

test('six examples cycle back to the first and clear previous answers',async({page})=>{
 await page.goto('http://127.0.0.1:8765/case-structure-explorer.html');
 const initial=await page.locator('#question').textContent();
 for(let n=2;n<=6;n++){
  await page.locator('#next').click();
  await expect(page.locator('#progress')).toContainText(`${n} / 6`);
  await expect(page.locator('#reason')).toContainText('解説は正解後');
  await expect(page.locator('#feedback')).toBeEmpty();
 }
 await page.locator('#next').click();
 await expect(page.locator('#progress')).toContainText('1 / 6');
 await expect(page.locator('#question')).toHaveText(initial);
});

test('every curated case accepts its own answer and reveals the matching explanation',async({page})=>{
 await page.goto('http://127.0.0.1:8765/case-structure-explorer.html');
 const examples=await page.evaluate(()=>window.RSL_CASE_EXAMPLES.map(e=>({question:e.question,correct:e.correct,reason:e.reason,explanation:e.explanation})));
 expect(examples).toHaveLength(6);
 for(let i=0;i<examples.length;i++){
  const example=examples[i];
  await expect(page.locator('#question')).toHaveText(example.question);
  await expect(page.locator('#reason')).toContainText('解説は正解後');
  await page.locator('#choices button').nth(example.correct).click();
  await expect(page.locator('#feedback')).toContainText(example.explanation);
  await expect(page.locator('#reason')).toHaveText(example.reason);
  await expect(page.locator('#choices button:disabled')).toHaveCount(3);
  if(i<examples.length-1)await page.locator('#next').click();
 }
});
