const {test,expect}=require('@playwright/test');
const {spawn}=require('node:child_process');
let server;
test.beforeAll(async()=>{server=spawn('python3',['-m','http.server','8765','--bind','127.0.0.1'],{stdio:'ignore'});await new Promise(r=>setTimeout(r,900))});
test.afterAll(()=>{if(server)server.kill()});
test('case explorer loads, checks answer, and moves to next example',async({page})=>{
 await page.goto('http://127.0.0.1:8765/case-structure-explorer.html');
 await expect(page.locator('#sentence button')).toHaveCount(4);
 await expect(page.locator('#progress')).toContainText('1 / 3');
 await expect(page.locator('#reason')).toContainText('解説は正解後');
 const choices=page.locator('#choices button');
 await choices.nth(0).click();
 await expect(page.locator('#feedback')).toContainText('もう一度');
 await expect(page.locator('#reason')).toContainText('解説は正解後');
 await choices.nth(1).click();
 await expect(page.locator('#feedback')).toContainText('正解');
 await expect(choices.nth(1)).toBeDisabled();
 await page.locator('#next').click();
 await expect(page.locator('#progress')).toContainText('2 / 3');
 await expect(page.locator('#feedback')).toBeEmpty();
});
test('canonical Learn links to case explorer',async({page})=>{
 await page.goto('http://127.0.0.1:8765/index.html');
 await page.locator('a[href="case-structure-explorer.html"]').click();
 await expect(page).toHaveURL(/case-structure-explorer\.html$/);
 await page.getByRole('link',{name:/Learn に戻る/}).click();
 await expect(page).toHaveURL(/index\.html$/);
});
