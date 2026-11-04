#!/usr/bin/env node
'use strict';
const fs=require('node:fs');
const path=require('node:path');
const assert=require('node:assert/strict');

const root=path.resolve(__dirname,'..');
const pages=[
'index.html','feature-map.html','ai-material.html','my-material.html','verb-explorer.html',
'morphology-hub.html','aspect-lab.html','prefix-lab.html','suffix-lab.html',
'word-family-lab.html','morphology-check.html','level-browser.html','legacy-index.html'
];
const errors=[];
function check(condition,message){if(!condition)errors.push(message);}
check(fs.existsSync(path.join(root,'ui-system.css')),'Shared stylesheet missing');
for(const page of pages){
 const full=path.join(root,page);
 check(fs.existsSync(full),'Missing page: '+page);
 if(!fs.existsSync(full))continue;
 const html=fs.readFileSync(full,'utf8');
 check(/href=["']ui-system\.css\?v=\d+["']/.test(html),page+': missing shared stylesheet');
 if(page!=='feature-map.html')check(/href=["']feature-map\.html["']/.test(html),page+': missing function-guide navigation');
 for(const match of html.matchAll(/href=["']([^"'#?]+\.html)(?:\?[^"']*)?["']/g)){
   const dest=match[1];
   check(fs.existsSync(path.join(root,dest)),page+': broken link to '+dest);
 }
}
const guide=fs.readFileSync(path.join(root,'feature-map.html'),'utf8');
const destinations=[...guide.matchAll(/class="tile"[^>]*href="([^"]+\.html)"/g)].map(x=>x[1]);
const expected=pages.filter(page=>page!=='feature-map.html');
check(destinations.length>0,'Feature guide must list destinations');
for(const page of expected)check(destinations.includes(page),'Feature guide missing page: '+page);
for(const dest of destinations)check(fs.existsSync(path.join(root,dest)),'Feature guide has broken destination: '+dest);
check(new Set(destinations).size===destinations.length,'Feature guide has duplicate destinations');
if(errors.length){
 for(const error of errors)process.stderr.write('FAIL '+error+'\n');
 process.exitCode=1;
}else{
 process.stdout.write('PASS: '+pages.length+' shared-style pages, function-guide links and '+destinations.length+' discoverable features.\n');
}
