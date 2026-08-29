// Russian Structure Lab — A1 expansion batch 01
// 50 sentences: 5 per recurring category.
// Quality Gate v1 applied: naturalness, A1 load, grammar/focus, JP/EN meaning.
// Individual corrections below are explicit; unlisted candidates retain candidate status
// until the full corpus receives an external/native-speaker audit.
window.RSL_A1_QUALITY_GATE_01 = {
  gate:'Educational / CEFR Quality Gate v1',
  reviewed:50,
  status:'internal-pass-with-corrections',
  corrections:{
    'A1-DL-006':{focus:['present','time'],note:'в семь часов is treated pedagogically as a time expression, not labeled ACC-time.'},
    'A1-WS-009':{focus:['present','time'],note:'в девять is presented as a time expression at A1.'},
    'A1-TM-008':{focus:['motion','present','time'],note:'в восемь is presented as a time expression at A1.'},
    'A1-FS-006':{jp:'リンゴが1キロ必要です。',focus:['DAT','GEN','need'],note:'Translation now matches Мне нужен rather than an imperative request; experiencer label removed.'},
    'A1-TO-008':{jp:'私には、これは簡単に思えます。',note:'JP pathway now exposes the dative perspective more clearly.'},
    'A1-CE-009':{focus:['time','present'],note:'в семь is presented as a time expression at A1.'}
  },
  checks:{
    russianNaturalness:'PASS-internal',
    grammarFocus:'PASS-after-corrections',
    japaneseMeaning:'PASS-after-corrections',
    englishMeaning:'PASS-internal',
    cefrA1Load:'PASS-with-monitoring',
    duplicateAudit:'NOT_YET_FINAL',
    nativeSpeakerAudit:'NOT_VERIFIED'
  }
};

// Apply QA corrections without destroying the original 50-sentence dataset.
(function(){
 const rows=window.RSL_A1_EXPANSION_01||[];
 const fixes=window.RSL_A1_QUALITY_GATE_01.corrections;
 rows.forEach(row=>{
   const fix=fixes[row.id];
   if(fix){
     if(fix.jp) row.jp=fix.jp;
     if(fix.en) row.en=fix.en;
     if(fix.focus) row.focus=fix.focus;
     row.qaNote=fix.note;
   }
   row.qa='internal-v1';
 });
})();
