// Russian Structure Lab — A1 expansion batch 01
// 50 new sentences: 5 per recurring category.
// Designed from the category + structure coverage dashboards.
// IDs continue after the 5-sentence calibration seed in each category.
// Status remains candidate until CEFR / naturalness / pedagogy QA passes.
window.RSL_A1_EXPANSION_01 = [
// 🏠 Daily Life
{id:'A1-DL-006',level:'A1',category:'DL',status:'candidate',ru:'Я встаю в семь часов.',jp:'私は7時に起きます。',en:'I get up at seven.',emoji:'⏰ 🛏️',chunks:['Я встаю','в семь часов'],focus:['present','ACC-time'],aspect:{impf:'вставать',pf:'встать'}},
{id:'A1-DL-007',level:'A1',category:'DL',status:'candidate',ru:'Я завтракаю на кухне.',jp:'私は台所で朝食をとります。',en:'I have breakfast in the kitchen.',emoji:'🥣 🏠',chunks:['Я завтракаю','на кухне'],focus:['present','PREP']},
{id:'A1-DL-008',level:'A1',category:'DL',status:'candidate',ru:'Я мою руки.',jp:'私は手を洗います。',en:'I wash my hands.',emoji:'🧼 👐',chunks:['Я мою','руки'],focus:['present','ACC'],aspect:{impf:'мыть',pf:'помыть'}},
{id:'A1-DL-009',level:'A1',category:'DL',status:'candidate',ru:'Вечером мы смотрим телевизор.',jp:'夕方、私たちはテレビを見ます。',en:'In the evening we watch TV.',emoji:'🌙 📺',chunks:['Вечером','мы смотрим телевизор'],focus:['INST-time','present','ACC'],aspect:{impf:'смотреть',pf:'посмотреть'}},
{id:'A1-DL-010',level:'A1',category:'DL',status:'candidate',ru:'Я ложусь спать поздно.',jp:'私は遅く寝ます。',en:'I go to bed late.',emoji:'🌙 😴',chunks:['Я ложусь спать','поздно'],focus:['present','infinitive'],aspect:{impf:'ложиться',pf:'лечь'}},

// 👥 People & Relationships
{id:'A1-PR-006',level:'A1',category:'PR',status:'candidate',ru:'Это мой брат.',jp:'これは私の兄弟です。',en:'This is my brother.',emoji:'👦 👨‍👩‍👧',chunks:['Это','мой брат'],focus:['NOM','agreement']},
{id:'A1-PR-007',level:'A1',category:'PR',status:'candidate',ru:'Моя сестра живёт в Москве.',jp:'私の姉妹はモスクワに住んでいます。',en:'My sister lives in Moscow.',emoji:'👩 🏙️',chunks:['Моя сестра','живёт в Москве'],focus:['agreement','PREP','present']},
{id:'A1-PR-008',level:'A1',category:'PR',status:'candidate',ru:'Я звоню маме.',jp:'私は母に電話します。',en:'I call my mother.',emoji:'📞 👩',chunks:['Я звоню','маме'],focus:['DAT','present'],aspect:{impf:'звонить',pf:'позвонить'}},
{id:'A1-PR-009',level:'A1',category:'PR',status:'candidate',ru:'Мы идём с друзьями в кафе.',jp:'私たちは友達とカフェへ行きます。',en:'We are going to a cafe with friends.',emoji:'👥 🚶 ☕',chunks:['Мы идём','с друзьями','в кафе'],focus:['motion','INST','ACC']},
{id:'A1-PR-010',level:'A1',category:'PR',status:'candidate',ru:'Я хорошо знаю Анну.',jp:'私はアンナをよく知っています。',en:'I know Anna well.',emoji:'🙂 🤝',chunks:['Я хорошо знаю','Анну'],focus:['ACC','present']},

// 💼 Work & Study
{id:'A1-WS-006',level:'A1',category:'WS',status:'candidate',ru:'Я читаю учебник.',jp:'私は教科書を読みます。',en:'I read the textbook.',emoji:'📘 👀',chunks:['Я читаю','учебник'],focus:['ACC','present'],aspect:{impf:'читать',pf:'прочитать'}},
{id:'A1-WS-007',level:'A1',category:'WS',status:'candidate',ru:'Учитель задаёт вопрос.',jp:'先生が質問をします。',en:'The teacher asks a question.',emoji:'👨‍🏫 ❓',chunks:['Учитель задаёт','вопрос'],focus:['NOM','ACC','present'],aspect:{impf:'задавать',pf:'задать'}},
{id:'A1-WS-008',level:'A1',category:'WS',status:'candidate',ru:'Я отвечаю учителю.',jp:'私は先生に答えます。',en:'I answer the teacher.',emoji:'🙋 👨‍🏫',chunks:['Я отвечаю','учителю'],focus:['DAT','present'],aspect:{impf:'отвечать',pf:'ответить'}},
{id:'A1-WS-009',level:'A1',category:'WS',status:'candidate',ru:'Урок начинается в девять.',jp:'授業は9時に始まります。',en:'The lesson starts at nine.',emoji:'🕘 📚',chunks:['Урок начинается','в девять'],focus:['present','ACC-time'],aspect:{impf:'начинаться',pf:'начаться'}},
{id:'A1-WS-010',level:'A1',category:'WS',status:'candidate',ru:'Сегодня у нас тест.',jp:'今日はテストがあります。',en:'We have a test today.',emoji:'📝 📅',chunks:['Сегодня','у нас тест'],focus:['GEN','possession','time']},

// 🚆 Travel & Movement
{id:'A1-TM-006',level:'A1',category:'TM',status:'candidate',ru:'Я иду на станцию.',jp:'私は駅へ歩いて行きます。',en:'I am walking to the station.',emoji:'🚶 🚉',chunks:['Я иду','на станцию'],focus:['motion','ACC']},
{id:'A1-TM-007',level:'A1',category:'TM',status:'candidate',ru:'Мы едем на автобусе.',jp:'私たちはバスで行きます。',en:'We are going by bus.',emoji:'🚌 ➡️',chunks:['Мы едем','на автобусе'],focus:['motion','PREP']},
{id:'A1-TM-008',level:'A1',category:'TM',status:'candidate',ru:'Поезд приходит в восемь.',jp:'列車は8時に到着します。',en:'The train arrives at eight.',emoji:'🚆 🕗',chunks:['Поезд приходит','в восемь'],focus:['motion','present','ACC-time'],aspect:{impf:'приходить',pf:'прийти'}},
{id:'A1-TM-009',level:'A1',category:'TM',status:'candidate',ru:'Я жду автобус.',jp:'私はバスを待っています。',en:'I am waiting for the bus.',emoji:'⏳ 🚌',chunks:['Я жду','автобус'],focus:['ACC','present']},
{id:'A1-TM-010',level:'A1',category:'TM',status:'candidate',ru:'Остановка рядом с банком.',jp:'バス停は銀行のそばです。',en:'The bus stop is next to the bank.',emoji:'🚏 🏦',chunks:['Остановка','рядом с банком'],focus:['INST','location']},

// 🍽️ Food & Shopping
{id:'A1-FS-006',level:'A1',category:'FS',status:'candidate',ru:'Мне нужен килограмм яблок.',jp:'リンゴを1キロください。',en:'I need a kilogram of apples.',emoji:'🍎 ⚖️',chunks:['Мне нужен','килограмм яблок'],focus:['DAT','GEN','experiencer']},
{id:'A1-FS-007',level:'A1',category:'FS',status:'candidate',ru:'У вас есть вода?',jp:'水はありますか。',en:'Do you have water?',emoji:'💧 ❓',chunks:['У вас есть','вода'],focus:['GEN','possession','question']},
{id:'A1-FS-008',level:'A1',category:'FS',status:'candidate',ru:'Я плачу картой.',jp:'私はカードで払います。',en:'I pay by card.',emoji:'💳 💰',chunks:['Я плачу','картой'],focus:['INST','present']},
{id:'A1-FS-009',level:'A1',category:'FS',status:'candidate',ru:'Этот суп очень вкусный.',jp:'このスープはとてもおいしいです。',en:'This soup is very tasty.',emoji:'🍲 😋',chunks:['Этот суп','очень вкусный'],focus:['NOM','agreement']},
{id:'A1-FS-010',level:'A1',category:'FS',status:'candidate',ru:'Дайте мне чай без сахара.',jp:'砂糖なしの紅茶をください。',en:'Please give me tea without sugar.',emoji:'☕ 🚫🍬',chunks:['Дайте мне','чай','без сахара'],focus:['DAT','ACC','GEN','request']},

// ❤️ Body & Emotion
{id:'A1-BE-006',level:'A1',category:'BE',status:'candidate',ru:'Мне жарко.',jp:'私は暑いです。',en:'I am hot.',emoji:'🥵',chunks:['Мне','жарко'],focus:['DAT','experiencer']},
{id:'A1-BE-007',level:'A1',category:'BE',status:'candidate',ru:'Мне хорошо.',jp:'私は気分がいいです。',en:'I feel good.',emoji:'🙂',chunks:['Мне','хорошо'],focus:['DAT','experiencer']},
{id:'A1-BE-008',level:'A1',category:'BE',status:'candidate',ru:'У меня болит спина.',jp:'背中が痛いです。',en:'My back hurts.',emoji:'😣',chunks:['У меня','болит спина'],focus:['GEN','possession','present']},
{id:'A1-BE-009',level:'A1',category:'BE',status:'candidate',ru:'Я боюсь собак.',jp:'私は犬が怖いです。',en:'I am afraid of dogs.',emoji:'😨 🐕',chunks:['Я боюсь','собак'],focus:['GEN','present']},
{id:'A1-BE-010',level:'A1',category:'BE',status:'candidate',ru:'Я хочу отдохнуть.',jp:'私は休みたいです。',en:'I want to rest.',emoji:'🛋️ 😌',chunks:['Я хочу','отдохнуть'],focus:['infinitive','PF'],aspect:{impf:'отдыхать',pf:'отдохнуть'}},

// 🌦️ Nature & Environment
{id:'A1-NE-006',level:'A1',category:'NE',status:'candidate',ru:'Сегодня тепло.',jp:'今日は暖かいです。',en:'It is warm today.',emoji:'🌤️',chunks:['Сегодня','тепло'],focus:['weather','state']},
{id:'A1-NE-007',level:'A1',category:'NE',status:'candidate',ru:'На улице сильный ветер.',jp:'外は風が強いです。',en:'There is a strong wind outside.',emoji:'💨',chunks:['На улице','сильный ветер'],focus:['PREP','agreement']},
{id:'A1-NE-008',level:'A1',category:'NE',status:'candidate',ru:'Ночью идёт снег.',jp:'夜は雪が降ります。',en:'It snows at night.',emoji:'🌙 ❄️',chunks:['Ночью','идёт снег'],focus:['INST-time','weather']},
{id:'A1-NE-009',level:'A1',category:'NE',status:'candidate',ru:'Я люблю море.',jp:'私は海が好きです。',en:'I love the sea.',emoji:'❤️ 🌊',chunks:['Я люблю','море'],focus:['ACC','present']},
{id:'A1-NE-010',level:'A1',category:'NE',status:'candidate',ru:'Мы гуляем в парке.',jp:'私たちは公園を散歩します。',en:'We walk in the park.',emoji:'🚶 🌳',chunks:['Мы гуляем','в парке'],focus:['PREP','present']},

// 📰 Society & Information
{id:'A1-SI-006',level:'A1',category:'SI',status:'candidate',ru:'Я смотрю новости утром.',jp:'私は朝ニュースを見ます。',en:'I watch the news in the morning.',emoji:'📰 🌅',chunks:['Я смотрю новости','утром'],focus:['ACC','INST-time','present'],aspect:{impf:'смотреть',pf:'посмотреть'}},
{id:'A1-SI-007',level:'A1',category:'SI',status:'candidate',ru:'Телефон не работает.',jp:'電話が動きません。',en:'The phone does not work.',emoji:'📱 ❌',chunks:['Телефон','не работает'],focus:['negation','present']},
{id:'A1-SI-008',level:'A1',category:'SI',status:'candidate',ru:'Я пишу сообщение другу.',jp:'私は友達にメッセージを書きます。',en:'I write a message to a friend.',emoji:'💬 ✍️',chunks:['Я пишу','сообщение','другу'],focus:['ACC','DAT','present'],aspect:{impf:'писать',pf:'написать'}},
{id:'A1-SI-009',level:'A1',category:'SI',status:'candidate',ru:'Где мой телефон?',jp:'私の電話はどこですか。',en:'Where is my phone?',emoji:'📱 ❓',chunks:['Где','мой телефон'],focus:['question','NOM','agreement']},
{id:'A1-SI-010',level:'A1',category:'SI',status:'candidate',ru:'Завтра я позвоню вам.',jp:'明日あなたに電話します。',en:'I will call you tomorrow.',emoji:'📞 📅',chunks:['Завтра','я позвоню вам'],focus:['DAT','PF','future'],aspect:{impf:'звонить',pf:'позвонить'}},

// 🧠 Thought & Opinion
{id:'A1-TO-006',level:'A1',category:'TO',status:'candidate',ru:'Я помню это слово.',jp:'私はこの単語を覚えています。',en:'I remember this word.',emoji:'🧠 📝',chunks:['Я помню','это слово'],focus:['ACC','present']},
{id:'A1-TO-007',level:'A1',category:'TO',status:'candidate',ru:'Я не понимаю вопрос.',jp:'私は質問が分かりません。',en:'I do not understand the question.',emoji:'🤔 ❓',chunks:['Я не понимаю','вопрос'],focus:['negation','ACC','present']},
{id:'A1-TO-008',level:'A1',category:'TO',status:'candidate',ru:'Мне кажется, это легко.',jp:'これは簡単だと思います。',en:'It seems easy to me.',emoji:'💭 🙂',chunks:['Мне кажется','это легко'],focus:['DAT','experiencer']},
{id:'A1-TO-009',level:'A1',category:'TO',status:'candidate',ru:'Как вы думаете?',jp:'どう思いますか。',en:'What do you think?',emoji:'🤔 ❓',chunks:['Как','вы думаете'],focus:['question','present']},
{id:'A1-TO-010',level:'A1',category:'TO',status:'candidate',ru:'Я думаю о работе.',jp:'私は仕事について考えています。',en:'I am thinking about work.',emoji:'💭 💼',chunks:['Я думаю','о работе'],focus:['PREP','present']},

// 🎭 Culture & Expression
{id:'A1-CE-006',level:'A1',category:'CE',status:'candidate',ru:'Я люблю эту песню.',jp:'私はこの歌が好きです。',en:'I love this song.',emoji:'❤️ 🎵',chunks:['Я люблю','эту песню'],focus:['ACC','agreement']},
{id:'A1-CE-007',level:'A1',category:'CE',status:'candidate',ru:'Она хорошо поёт.',jp:'彼女は歌が上手です。',en:'She sings well.',emoji:'🎤 🙂',chunks:['Она хорошо поёт'],focus:['present']},
{id:'A1-CE-008',level:'A1',category:'CE',status:'candidate',ru:'Мы идём в музей.',jp:'私たちは博物館へ行きます。',en:'We are going to a museum.',emoji:'🚶 🖼️',chunks:['Мы идём','в музей'],focus:['motion','ACC']},
{id:'A1-CE-009',level:'A1',category:'CE',status:'candidate',ru:'Фильм начинается в семь.',jp:'映画は7時に始まります。',en:'The film starts at seven.',emoji:'🎬 🕖',chunks:['Фильм начинается','в семь'],focus:['ACC-time','present'],aspect:{impf:'начинаться',pf:'начаться'}},
{id:'A1-CE-010',level:'A1',category:'CE',status:'candidate',ru:'Мне нравится русская музыка.',jp:'私はロシア音楽が好きです。',en:'I like Russian music.',emoji:'❤️ 🇷🇺 🎵',chunks:['Мне нравится','русская музыка'],focus:['DAT','experiencer','agreement']}
];
