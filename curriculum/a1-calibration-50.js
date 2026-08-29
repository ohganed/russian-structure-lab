// Russian Structure Lab — A1 calibration corpus
// 10 recurring categories × 5 sentences = 50.
// This is the calibration set for the A1 quality gate before expansion to 500.
// Schema: id, level, category, title, ru, jp, en, emoji, chunks, focus
window.RSL_A1_CALIBRATION = [
{id:'A1-DL-001',level:'A1',category:'DL',title:'Morning window',ru:'Я открываю окно.',jp:'私は窓を開けます。',en:'I open the window.',emoji:'🌅 🪟',chunks:['Я','открываю окно'],focus:['ACC','present']},
{id:'A1-DL-002',level:'A1',category:'DL',title:'Tea',ru:'Я пью чай.',jp:'私は紅茶を飲みます。',en:'I drink tea.',emoji:'☕',chunks:['Я','пью чай'],focus:['ACC','present']},
{id:'A1-DL-003',level:'A1',category:'DL',title:'At home',ru:'Мама дома.',jp:'母は家にいます。',en:'Mom is at home.',emoji:'🏠 👩',chunks:['Мама','дома'],focus:['location']},
{id:'A1-DL-004',level:'A1',category:'DL',title:'Book on table',ru:'Книга на столе.',jp:'本は机の上にあります。',en:'The book is on the table.',emoji:'📖 🪵',chunks:['Книга','на столе'],focus:['PREP']},
{id:'A1-DL-005',level:'A1',category:'DL',title:'Before sleep',ru:'Я читаю перед сном.',jp:'私は寝る前に読みます。',en:'I read before sleep.',emoji:'📖 🌙',chunks:['Я читаю','перед сном'],focus:['INST']},

{id:'A1-PR-001',level:'A1',category:'PR',title:'My friend',ru:'Это мой друг.',jp:'これは私の友達です。',en:'This is my friend.',emoji:'👤 🤝',chunks:['Это','мой друг'],focus:['NOM']},
{id:'A1-PR-002',level:'A1',category:'PR',title:'My sister',ru:'У меня есть сестра.',jp:'私には姉妹がいます。',en:'I have a sister.',emoji:'👨‍👩‍👧',chunks:['У меня','есть сестра'],focus:['GEN','possession']},
{id:'A1-PR-003',level:'A1',category:'PR',title:'Name',ru:'Меня зовут Анна.',jp:'私の名前はアンナです。',en:'My name is Anna.',emoji:'👋',chunks:['Меня зовут','Анна'],focus:['ACC','fixed expression']},
{id:'A1-PR-004',level:'A1',category:'PR',title:'Friend nearby',ru:'Друг рядом со мной.',jp:'友達は私のそばにいます。',en:'My friend is next to me.',emoji:'🧑‍🤝‍🧑',chunks:['Друг','рядом со мной'],focus:['INST']},
{id:'A1-PR-005',level:'A1',category:'PR',title:'We talk',ru:'Мы говорим по-русски.',jp:'私たちはロシア語で話します。',en:'We speak Russian.',emoji:'🗣️ 🇷🇺',chunks:['Мы говорим','по-русски'],focus:['adverb']},

{id:'A1-WS-001',level:'A1',category:'WS',title:'At school',ru:'Я учусь в школе.',jp:'私は学校で勉強しています。',en:'I study at school.',emoji:'🏫',chunks:['Я учусь','в школе'],focus:['PREP']},
{id:'A1-WS-002',level:'A1',category:'WS',title:'Teacher',ru:'Учитель говорит медленно.',jp:'先生はゆっくり話します。',en:'The teacher speaks slowly.',emoji:'👨‍🏫 🐢',chunks:['Учитель говорит','медленно'],focus:['present']},
{id:'A1-WS-003',level:'A1',category:'WS',title:'Notebook',ru:'Я пишу в тетради.',jp:'私はノートに書きます。',en:'I write in my notebook.',emoji:'✍️ 📓',chunks:['Я пишу','в тетради'],focus:['PREP']},
{id:'A1-WS-004',level:'A1',category:'WS',title:'Question',ru:'У меня есть вопрос.',jp:'質問があります。',en:'I have a question.',emoji:'❓',chunks:['У меня','есть вопрос'],focus:['GEN','possession']},
{id:'A1-WS-005',level:'A1',category:'WS',title:'Work today',ru:'Сегодня я работаю дома.',jp:'今日は家で仕事をします。',en:'Today I work at home.',emoji:'💼 🏠',chunks:['Сегодня','я работаю','дома'],focus:['time','present']},

{id:'A1-TM-001',level:'A1',category:'TM',title:'To Moscow',ru:'Я еду в Москву.',jp:'私はモスクワへ行きます。',en:'I am going to Moscow.',emoji:'🚆 📍',chunks:['Я еду','в Москву'],focus:['ACC','motion']},
{id:'A1-TM-002',level:'A1',category:'TM',title:'At station',ru:'Мы на вокзале.',jp:'私たちは駅にいます。',en:'We are at the station.',emoji:'🚉',chunks:['Мы','на вокзале'],focus:['PREP']},
{id:'A1-TM-003',level:'A1',category:'TM',title:'Bus',ru:'Автобус уже здесь.',jp:'バスはもうここにいます。',en:'The bus is already here.',emoji:'🚌',chunks:['Автобус','уже здесь'],focus:['location']},
{id:'A1-TM-004',level:'A1',category:'TM',title:'Where is metro',ru:'Где метро?',jp:'地下鉄はどこですか。',en:'Where is the metro?',emoji:'🚇 ❓',chunks:['Где','метро'],focus:['question']},
{id:'A1-TM-005',level:'A1',category:'TM',title:'Walk to hotel',ru:'Я иду в гостиницу.',jp:'私はホテルへ歩いて行きます。',en:'I am walking to the hotel.',emoji:'🚶 🏨',chunks:['Я иду','в гостиницу'],focus:['ACC','motion']},

{id:'A1-FS-001',level:'A1',category:'FS',title:'Bread please',ru:'Дайте хлеб, пожалуйста.',jp:'パンをください。',en:'Bread, please.',emoji:'🍞 🙏',chunks:['Дайте хлеб','пожалуйста'],focus:['ACC','request']},
{id:'A1-FS-002',level:'A1',category:'FS',title:'Coffee',ru:'Я хочу кофе.',jp:'コーヒーが欲しいです。',en:'I want coffee.',emoji:'☕',chunks:['Я хочу','кофе'],focus:['ACC','want']},
{id:'A1-FS-003',level:'A1',category:'FS',title:'Price',ru:'Сколько это стоит?',jp:'これはいくらですか。',en:'How much does this cost?',emoji:'💰 ❓',chunks:['Сколько','это стоит'],focus:['question']},
{id:'A1-FS-004',level:'A1',category:'FS',title:'Apples',ru:'Я покупаю яблоки.',jp:'私はリンゴを買います。',en:'I buy apples.',emoji:'🛒 🍎',chunks:['Я покупаю','яблоки'],focus:['ACC','present']},
{id:'A1-FS-005',level:'A1',category:'FS',title:'Restaurant',ru:'Мы едим в ресторане.',jp:'私たちはレストランで食べます。',en:'We eat at a restaurant.',emoji:'🍽️',chunks:['Мы едим','в ресторане'],focus:['PREP']},

{id:'A1-BE-001',level:'A1',category:'BE',title:'Tired',ru:'Я устал.',jp:'私は疲れました。',en:'I am tired.',emoji:'😮‍💨',chunks:['Я','устал'],focus:['past','gender']},
{id:'A1-BE-002',level:'A1',category:'BE',title:'Cold',ru:'Мне холодно.',jp:'私は寒いです。',en:'I am cold.',emoji:'🥶',chunks:['Мне','холодно'],focus:['DAT','experiencer']},
{id:'A1-BE-003',level:'A1',category:'BE',title:'Head hurts',ru:'У меня болит голова.',jp:'頭が痛いです。',en:'My head hurts.',emoji:'🤕',chunks:['У меня','болит голова'],focus:['GEN','possession']},
{id:'A1-BE-004',level:'A1',category:'BE',title:'Happy',ru:'Я рад.',jp:'私はうれしいです。',en:'I am glad.',emoji:'😊',chunks:['Я','рад'],focus:['short adjective']},
{id:'A1-BE-005',level:'A1',category:'BE',title:'Want sleep',ru:'Я хочу спать.',jp:'眠りたいです。',en:'I want to sleep.',emoji:'😴',chunks:['Я хочу','спать'],focus:['infinitive']},

{id:'A1-NE-001',level:'A1',category:'NE',title:'Rain',ru:'Сегодня идёт дождь.',jp:'今日は雨が降っています。',en:'It is raining today.',emoji:'🌧️',chunks:['Сегодня','идёт дождь'],focus:['weather']},
{id:'A1-NE-002',level:'A1',category:'NE',title:'Cold outside',ru:'На улице холодно.',jp:'外は寒いです。',en:'It is cold outside.',emoji:'❄️',chunks:['На улице','холодно'],focus:['PREP','state']},
{id:'A1-NE-003',level:'A1',category:'NE',title:'Sun',ru:'Солнце светит.',jp:'太陽が輝いています。',en:'The sun is shining.',emoji:'☀️',chunks:['Солнце','светит'],focus:['present']},
{id:'A1-NE-004',level:'A1',category:'NE',title:'Snow',ru:'Зимой здесь снег.',jp:'冬はここに雪があります。',en:'There is snow here in winter.',emoji:'❄️ ⛄',chunks:['Зимой','здесь снег'],focus:['INST','time']},
{id:'A1-NE-005',level:'A1',category:'NE',title:'Park',ru:'В парке много деревьев.',jp:'公園には木がたくさんあります。',en:'There are many trees in the park.',emoji:'🌳',chunks:['В парке','много деревьев'],focus:['PREP','GEN']},

{id:'A1-SI-001',level:'A1',category:'SI',title:'News',ru:'Я читаю новости.',jp:'私はニュースを読みます。',en:'I read the news.',emoji:'📰',chunks:['Я читаю','новости'],focus:['ACC']},
{id:'A1-SI-002',level:'A1',category:'SI',title:'Phone message',ru:'У меня новое сообщение.',jp:'新しいメッセージがあります。',en:'I have a new message.',emoji:'📱 💬',chunks:['У меня','новое сообщение'],focus:['GEN','agreement']},
{id:'A1-SI-003',level:'A1',category:'SI',title:'Photo',ru:'Это моя фотография.',jp:'これは私の写真です。',en:'This is my photo.',emoji:'📷',chunks:['Это','моя фотография'],focus:['NOM','agreement']},
{id:'A1-SI-004',level:'A1',category:'SI',title:'Internet',ru:'Интернет сегодня медленный.',jp:'今日はインターネットが遅いです。',en:'The internet is slow today.',emoji:'🌐 🐢',chunks:['Интернет','сегодня медленный'],focus:['adjective']},
{id:'A1-SI-005',level:'A1',category:'SI',title:'Call later',ru:'Я позвоню вечером.',jp:'夕方に電話します。',en:'I will call in the evening.',emoji:'📞 🌙',chunks:['Я позвоню','вечером'],focus:['PF','future','INST-time']},

{id:'A1-TO-001',level:'A1',category:'TO',title:'I know',ru:'Я знаю ответ.',jp:'私は答えを知っています。',en:'I know the answer.',emoji:'🧠 ✅',chunks:['Я знаю','ответ'],focus:['ACC']},
{id:'A1-TO-002',level:'A1',category:'TO',title:'I think',ru:'Я думаю, что это хорошо.',jp:'これは良いと思います。',en:'I think this is good.',emoji:'🤔',chunks:['Я думаю','что это хорошо'],focus:['что-clause']},
{id:'A1-TO-003',level:'A1',category:'TO',title:'Understand',ru:'Я понимаю.',jp:'分かります。',en:'I understand.',emoji:'💡',chunks:['Я','понимаю'],focus:['present']},
{id:'A1-TO-004',level:'A1',category:'TO',title:'Do not know',ru:'Я не знаю.',jp:'分かりません。',en:"I don't know.",emoji:'🤷',chunks:['Я','не знаю'],focus:['negation']},
{id:'A1-TO-005',level:'A1',category:'TO',title:'Like Russian',ru:'Мне нравится русский язык.',jp:'私はロシア語が好きです。',en:'I like the Russian language.',emoji:'❤️ 🇷🇺',chunks:['Мне нравится','русский язык'],focus:['DAT','experiencer']},

{id:'A1-CE-001',level:'A1',category:'CE',title:'Music',ru:'Я слушаю музыку.',jp:'私は音楽を聴きます。',en:'I listen to music.',emoji:'🎵',chunks:['Я слушаю','музыку'],focus:['ACC']},
{id:'A1-CE-002',level:'A1',category:'CE',title:'Film',ru:'Мы смотрим фильм.',jp:'私たちは映画を見ます。',en:'We are watching a film.',emoji:'🎬',chunks:['Мы смотрим','фильм'],focus:['ACC']},
{id:'A1-CE-003',level:'A1',category:'CE',title:'Book',ru:'Эта книга интересная.',jp:'この本は面白いです。',en:'This book is interesting.',emoji:'📚',chunks:['Эта книга','интересная'],focus:['agreement']},
{id:'A1-CE-004',level:'A1',category:'CE',title:'Museum',ru:'Сегодня музей открыт.',jp:'今日は博物館が開いています。',en:'The museum is open today.',emoji:'🏛️',chunks:['Сегодня','музей открыт'],focus:['short adjective']},
{id:'A1-CE-005',level:'A1',category:'CE',title:'Russian song',ru:'Это русская песня.',jp:'これはロシアの歌です。',en:'This is a Russian song.',emoji:'🎶 🇷🇺',chunks:['Это','русская песня'],focus:['NOM','agreement']}
];
