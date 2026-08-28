window.RSL_CURRICULUM = {
  version: '1.0.0',
  targetSentenceCount: 3000,
  levels: ['A1','A2','B1','B2','C1','C2'],
  perLevel: 500,
  categories: [
    {code:'DL', emoji:'🏠', name:'Daily Life', targetPerLevel:50},
    {code:'PR', emoji:'👥', name:'People & Relationships', targetPerLevel:50},
    {code:'WS', emoji:'💼', name:'Work & Study', targetPerLevel:50},
    {code:'TM', emoji:'🚆', name:'Travel & Movement', targetPerLevel:50},
    {code:'FS', emoji:'🍽️', name:'Food & Shopping', targetPerLevel:50},
    {code:'BE', emoji:'❤️', name:'Body & Emotion', targetPerLevel:50},
    {code:'NE', emoji:'🌦️', name:'Nature & Environment', targetPerLevel:50},
    {code:'SI', emoji:'📰', name:'Society & Information', targetPerLevel:50},
    {code:'TO', emoji:'🧠', name:'Thought & Opinion', targetPerLevel:50},
    {code:'CE', emoji:'🎭', name:'Culture & Expression', targetPerLevel:50}
  ],
  sentenceShape: {
    required: ['id','level','category','ru','jp','en'],
    optional: ['subCategory','chunks','caseFocus','aspectFocus','anatomyFocus','grammarFocus','register','scene','notes']
  },
  idPattern: 'LEVEL-CATEGORY-NNN',
  philosophy: {
    spiral: 'same worlds, deeper language',
    discovery: 'complexity should be discovered, not presented',
    interaction: 'tap → sound → meaning → chunk → structure → grammar/morphology → network',
    wordDisplay: 'original spelling + decomposition when linguistically meaningful',
    caseDisplay: 'show all six cases when available; highlight current form with 📍'
  }
};

window.RSL_getCurriculumCategory = function(code){
  return window.RSL_CURRICULUM.categories.find(c => c.code === code) || null;
};

window.RSL_validateSentence = function(item){
  const missing = window.RSL_CURRICULUM.sentenceShape.required.filter(k => !item || !item[k]);
  return {ok: missing.length === 0, missing};
};
