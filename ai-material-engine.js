(function(global){
  const STORAGE_KEY='russianStructureLab.aiLibrary.v1';
  const MAX_ITEMS=50;
  function cleanJson(raw=''){
    let s=String(raw).trim();
    s=s.replace(/^```(?:json)?\s*/i,'').replace(/\s*```$/,'');
    const a=s.indexOf('{'),b=s.lastIndexOf('}');
    if(a>=0&&b>a)s=s.slice(a,b+1);
    return s;
  }
  function idsUnique(items,label,sid){
    const seen=new Set();
    for(const item of items||[]){
      if(!item?.id)continue;
      if(seen.has(item.id))throw Error(`Sentence ${sid} / ${label} ${item.id}: duplicate id`);
      seen.add(item.id);
    }
  }
  function validate(data){
    if(!data||typeof data!=='object'||Array.isArray(data))throw Error('Top-level JSON object is required');
    if(data.schemaVersion!=='1.0')throw Error(`Unsupported schemaVersion: ${data.schemaVersion ?? 'missing'}`);
    if(data.language!=='ru')throw Error('language must be "ru"');
    if(!Array.isArray(data.sentences)||!data.sentences.length)throw Error('sentences must be a non-empty array');
    for(let si=0;si<data.sentences.length;si++){
      const s=data.sentences[si], sid=s?.id||`#${si+1}`;
      if(typeof s?.text!=='string')throw Error(`Sentence ${sid}: text is required`);
      idsUnique(s.words,'word',sid); idsUnique(s.chunks,'chunk',sid);
      const wordIds=new Set((s.words||[]).map(w=>w.id).filter(Boolean));
      for(const w of s.words||[]){
        if(Number.isInteger(w.start)&&Number.isInteger(w.end)&&s.text.slice(w.start,w.end)!==w.surface){
          throw Error(`Sentence ${sid} / word ${w.id||'?'}: offset mismatch for "${w.surface||''}"`);
        }
      }
      for(const c of s.chunks||[]){
        if(Number.isInteger(c.start)&&Number.isInteger(c.end)&&s.text.slice(c.start,c.end)!==c.text){
          throw Error(`Sentence ${sid} / chunk ${c.id||'?'}: offset mismatch for "${c.text||''}"`);
        }
        for(const id of c.wordIds||[])if(!wordIds.has(id))throw Error(`Sentence ${sid} / chunk ${c.id||'?'}: unknown wordId ${id}`);
      }
      function walk(node){
        if(!node)return;
        for(const id of node.refIds||[])if(!wordIds.has(id))throw Error(`Sentence ${sid} / structure ${node.id||'?'}: unknown refId ${id}`);
        for(const child of node.children||[])walk(child);
      }
      walk(s.structure?.tree);
    }
    return {ok:true,data};
  }
  function storage(){return global.localStorage || null;}
  function listLessons(){
    try{return JSON.parse(storage()?.getItem(STORAGE_KEY)||'[]')}catch{return []}
  }
  function saveLesson(data){
    validate(data);
    const list=listLessons();
    const key=data.originalText||data.title||String(Date.now());
    const entry={key,title:data.title||'Russian AI Material',savedAt:Date.now(),data};
    const next=[entry,...list.filter(x=>x.key!==key)].slice(0,MAX_ITEMS);
    storage()?.setItem(STORAGE_KEY,JSON.stringify(next));
    return entry;
  }
  function deleteLesson(key){
    const next=listLessons().filter(x=>x.key!==key);
    storage()?.setItem(STORAGE_KEY,JSON.stringify(next));
    return next;
  }
  global.RSL_AI_MATERIAL_ENGINE={STORAGE_KEY,cleanJson,validate,listLessons,saveLesson,deleteLesson};
})(typeof window !== 'undefined' ? window : globalThis);
