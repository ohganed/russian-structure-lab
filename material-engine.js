(function(){
  'use strict';

  const VERSION = '0.1.0';

  function splitSlash(value){
    return typeof value === 'string' && value.length ? value.split('/') : [];
  }

  function normalizeLegacy(row){
    if(!Array.isArray(row)) return null;
    const [id,context,ru,jp,scene,stressed,lemmas,wordMeanings,chunks,jpChunks,architecture] = row;
    if(!id || !ru) return null;
    const chunkRu = splitSlash(chunks);
    const chunkJp = splitSlash(jpChunks);
    return {
      id,
      level: 'UNCLASSIFIED',
      category: null,
      subCategory: null,
      context: context || '',
      ru,
      jp: jp || '',
      en: '',
      scene: scene || '',
      sound: {
        stressedWords: splitSlash(stressed)
      },
      words: splitSlash(stressed).map((surface,index)=>(
        {
          surface,
          lemma: splitSlash(lemmas)[index] || '',
          jp: splitSlash(wordMeanings)[index] || ''
        }
      )),
      chunks: chunkRu.map((text,index)=>({
        ru:text,
        jp:chunkJp[index] || ''
      })),
      architecture: splitSlash(architecture),
      caseFocus: [],
      aspectFocus: null,
      anatomyFocus: null,
      grammarFocus: [],
      register: null,
      source: 'legacy-materials',
      sourceShape: 'legacy-array',
      verification: 'NOT VERIFIED'
    };
  }

  function normalizeModern(item){
    if(!item || typeof item !== 'object' || !item.id || !item.ru) return null;
    return {
      id: item.id,
      level: item.level || 'UNCLASSIFIED',
      category: item.category || null,
      subCategory: item.subCategory || null,
      context: item.context || '',
      ru: item.ru,
      jp: item.jp || '',
      en: item.en || '',
      scene: item.scene || '',
      sound: item.sound || null,
      words: Array.isArray(item.words) ? item.words : [],
      chunks: Array.isArray(item.chunks) ? item.chunks.map(c=>typeof c === 'string' ? {ru:c,jp:'',en:''} : c) : [],
      architecture: Array.isArray(item.architecture) ? item.architecture : [],
      caseFocus: Array.isArray(item.caseFocus) ? item.caseFocus : [],
      aspectFocus: item.aspectFocus || null,
      anatomyFocus: item.anatomyFocus || null,
      grammarFocus: Array.isArray(item.grammarFocus) ? item.grammarFocus : [],
      register: item.register || null,
      notes: item.notes || null,
      source: item.source || 'curriculum',
      sourceShape: 'normalized-object',
      verification: item.verification || 'NOT VERIFIED'
    };
  }

  function collect(){
    const legacy = Array.isArray(window.RSL_MATERIALS)
      ? window.RSL_MATERIALS.map(normalizeLegacy).filter(Boolean)
      : [];
    const a1 = Array.isArray(window.RSL_A1_CALIBRATION)
      ? window.RSL_A1_CALIBRATION.map(normalizeModern).filter(Boolean)
      : [];
    const byId = new Map();
    legacy.forEach(x=>byId.set(x.id,x));
    a1.forEach(x=>byId.set(x.id,x));
    return Array.from(byId.values());
  }

  function getAll(){ return collect(); }
  function getByLevel(level){ return collect().filter(x=>x.level === level); }
  function getByCategory(level,category){
    return collect().filter(x=>(!level || x.level===level) && (!category || x.category===category));
  }
  function getById(id){ return collect().find(x=>x.id===id) || null; }
  function stats(){
    const all=collect();
    const levels={};
    ['A1','A2','B1','B2','C1','C2','UNCLASSIFIED'].forEach(l=>levels[l]=all.filter(x=>x.level===l).length);
    return {version:VERSION,total:all.length,levels};
  }

  window.RSL_MATERIAL_ENGINE = {
    version: VERSION,
    normalizeLegacy,
    normalizeModern,
    getAll,
    getByLevel,
    getByCategory,
    getById,
    stats
  };
})();
