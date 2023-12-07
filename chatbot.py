
data={
    "intents": [{
        "tag": "google",
        "patterns": ["google", "search", "internet"],
        "responses": ["Redirecting to Google..."]
    }, {
        "tag": "greeting",
        "patterns": ["Aslam O Alaikum","Hi there", "How are you", "Is anyone there?", "Hey", "Hi"],
        "responses": [" وعلیکم السلام !میں اپ کی کیا مدد کر سکتا ہوں؟"],

    }, {
        "tag": "thanks",
        "patterns": ["Thanks", "Thank you", "That's helpful", "Awesome, thanks", "Thanks for helping me"],
        "responses": ["Happy to help!", "Any time!", "My pleasure"],

    }, {
        "tag": "noanswer",
        "patterns": [],
        "responses": ["Sorry, can't understand you", "Please give me more info", "Not sure I understand"],

    }, {
        "tag": "options",
        "patterns": ["How you could help me?", "What you can do?", "What help you provide?", "How you can be helpful?", "What support is offered"],
        "responses": ["I am a general purpose chatbot. My capabilities are : \n 1. I can chat with you. Try asking me for jokes or riddles! \n 2. Ask me the date and time \n 3. I can google search for you. Use format google: your query \n 4. I can get the present weather for any city. Use format weather: city name \n 5. I can get you the top 10 trending news in India. Use keywords 'Latest News' \n 6. I can get you the top 10 trending songs globally. Type 'songs' \n 7. I can set a timer for you. Enter 'set a timer: minutes to timer' \n 8. I can get the present Covid stats for any country. Use 'covid 19: world' or 'covid 19: country name' \n For suggestions to help me improve, send an email to ted.thedlbot.suggestions@gmail.com . Thank you!! "],


    }, {
        "tag": "locationn,واقع ,جگہ",
        "patterns": [" اپ کا ادارہ کہاں ہے"," شبلی سکول کہاں  ہے"," where is shibli school situated"," where is shibli school"],
        "responses": [" شیبلی سکول سول ہسپتال مونگی بنگلہ کے پاس واقع ہے"]

   }, {
        "tag":  "چھٹیاں",
        "patterns": [
    "When will the vacations be?",
    "Can you tell me when the vacations will start?",
    "When are the summer holidays?",
    "What are the dates for the summer vacations?",
    "Do you know when the summer holidays will be and how long they will last?",
    "Can you provide me with the details of the vacations, including the start and end dates?",
    "When do the summer holidays begin and for how many days?",
    "Please inform me about the start and end dates of the summer vacations.",
    "What are the dates for the summer break?",
    "Can you tell me when the summer holidays are scheduled to begin and how long they will last?"


"Dhai mahine ki chhutiyan", "چھٹیاں کدو ہون گیاں؟",    "کیا آپ بتا سکدے ہو کہ چھٹیاں کدو ہون گیاں؟",    "میرے سکول کی گرمیوں کدو ہون گیاں؟",    "گرمیوں کی چھٹیاں کدوں شروع ہون گیاں اور کتھے دناں لئی ہون گیاں؟",    "کیا آپ کو یہ معلوم ہے کہ چھٹیاں کدو ہون گیاں اور کتھے دناں تک ہون گیاں؟",    "میرے سکول کی گرمیوں کدو ہون گیاں اور کتھے دناں لئی ہون گیاں؟",    "چھٹیاں کدوں شروع ہون گیاں اور کتھے دناں تک رہیاں گیاں؟",    "کیا آپ بتا سکدے ہو کہ چھٹیاں کدو ہوں گیاں اور کتھے دناں لئی ہون گیاں؟",    "میرے سکول کی گرمیوں کدو ہون گیاں اور کتھے دناں لئی ہون گیاں؟",    "گرمیوں کی چھٹیاں کدوں شروع ہون گیاں اور کتھے دناں تک ہون گیاں"

    "چھٹیاں کب ہونگی؟",
    "کیا آپ بتا سکتے ہیں کہ چھٹیاں کب ہوں گی؟",
    "میرے مدرسے کی گرمیوں کی چھٹیاں کب ہونگی؟",
    "گرمیوں کی چھٹیاں کب شروع ہونگی اور کتنے دنوں کے لئے ہونگی؟",
    "کیا آپ کو یہ معلوم ہے کہ چھٹیاں کب ہونگی اور کتنے عرصے تک ہونگی؟",
    "میرے سکول کی گرمیوں کی چھٹیاں کب ہونگی اور کتنے دنوں کے لئے ہونگی؟",
    "چھٹیاں کب شروع ہونگی اور کتنے عرصے تک رہیں گی؟",
    "کیا آپ بتا سکتے ہیں کہ چھٹیاں کب ہوگی اور کتنے دنوں کے لئے ہوگی؟",
    "میرے سکول کی گرمیوں کی چھٹیاں کب ہونگی اور کتنے دنوں کے لئے ہونگی؟",
    "گرمیوں کی چھٹیاں کب شروع ہونگی اور کتنے دنوں کے لئے ہونگی؟",
    " گرمیاں دیاں چھٹیاں کدوں ہون گیاں ؟", "when summer holidays will starts","summer vacations" ," گرمیاں دیاں چھٹیاں", "  ٹائیاں مہینیاں دیاں چھٹیاں"," garmiyon diyan chhutiyan kiddon hon gian"],
        "responses":[" چھٹیوں کا اغاز یکم جون سے ہوگا"," chhutiyan June 1,2023 se hongi"],

   }, {
        "tag": " پرنسپل کا نام",
        "patterns": ["  ہیڈ ماسٹر کا نام"," پرنسپل کا نام"," who is the principal of shiblee School", " principal", " name of principal", " ہیڈ ماسٹر کون یے", " شیبلی سکول کا ہیڈ ماسٹر"],
        "responses": [" MUHAMMAD WAQAR AHMAD Sahib"]
    }, {
        "tag": " کھلے گا، سکول کا ٹائم",
        "patterns": [" What is schedule of classes", "time table"," period start","prayer time"," کلاسز کب شروع ہوتی ہیں","  pahla period kab Shuru Hota Hai"," پہلا پیریڈ کب شروع ہوتا ہے"," چھٹی کب ہوتی ہے"],
        "responses": ["prayer time:7:15\n first period 8:00\n end classes 2:00PM"," پریئر ساڑھے سات  شروع ہوتی ہے\nکلاس اٹھ بجے شروع ہوتی ہے \n  چھٹی دو بجے ہوتی ہے"]
    }, {
        "tag":"fees",
        "patterns": ["What is fees of 6th class", " چھٹی کلاس کی فیس کتنی ہے"," ساتویں کلاس کی فیس کتنی ہے"," اٹھویں کلاس کی فیس کتنی ہے"," نویں کلاس کی فیس کتنی ہے"," دسویں کلاس کی فیس کتنی ہے"],
        "responses": ["6th class: Rs. 1100\n7th class: Rs. 1200\n8th class: Rs. 1300\n9th class: Rs. 1400\n10th class: Rs.1500"]
    }, {
        "tag": " clour  رنگ ",
        "patterns": [" لیڑیاں دا رنگ","یونی فارم کا رنگ  "," شرٹ کا کلر "," پینٹ کا رنگ ","ٹائی کا کلر "," شوز کا کلر "],
        "responses": [" شرٹ کا رنگ وائٹ ہے\n پینٹ کا رنگ بلیک ہے\n ٹائی کا رنگ بلو ہے\n شوز کا رنگ بلیک ہے"]
   } , {
        "tag": " ٹیچرز کے نام, teachers names",
        "patterns": [
        "names of  teachers",
    " teachers names",
    "teacher names at school",
    "school educators names",
    "who are the school teachers",
    "tell me  teachers' names",
    "what are the names of teachers.",
    "please provide the names of school teachers",
    "which educators teach at the school",
    "give me the list of school teachers",
    "  اساتذہ کے نام کیا ہیں؟",
    "  اساتذہ کے نام بیان کریں",
    "اسکول میں اساتذہ کے نام بتائیں",
    " معلمین کے نام بتائیے",
    "  معلمین کون ہیں",
    " اساتذے کون ہیں",
    "اسکول کے معلمین کون ہیں",
    "اسکول کے معلمین کے نام کیے ہیں",
    " کونسے اساتذہ مدرس ہیں",
    "اسکول کے اساتذہ کے نام کا فہرست دیں",
    " اساتذے دے نام کیا ہن؟",
    "اسکول دے اساتذے دے نام بیان کریں",
    " اساتذے دے نام بتائیں",
    "اسکول وچ معلمین دے نام بتائیے",
    "اسکول دے معلمین کیوں ہن",
    "اسکول دے اساتذے کون ہن",
    "اسکول دے معلمین کون ہن",
    "اسکول دے معلمین دے نام کیے ہن",
    "اسکول وچ کونسے اساتذے  پڑاندے ہن",
    "اسکول دے اساتذے دے نام دی فہرست دیں"
  ],

  "responses" : ["(اونر)سرور صاحب\n(پرنسیپل)وقار صاحب\n(میتھ)یاسر ساحب\n(کیمسٹری)احسن صاحب\n(فزکس)محسن صاحب\n(انگلش)حسن صاحب\n(بیالوجی)امانت صاحب\n(سائنس)عبید صاحب\n(اردو)انور صاحب\n(کمپیوٹر)عدنان صاحب\n(سائنس)سعد صاحب\n(اردو)لقمان صاحب\n(اسلامیات)ذیشان صاحب\n(میتھ)مبشر صاحب"]
    }, {
        "tag": "exam ,terms",
        "patterns": ["exam", "term", " سالانہ امتحان کب ہوں گے","  فسٹ ٹرم کب ہوگی"," سیکنڈ ٹرم کب ہوگی"," تھرڈ ٹرم کب ہوگی"],
        "responses": ["فسٹ ٹرم 10 مئی سے شروع ہوگی\nسیکنڈ ٹرم یکم اگست سے شروع ہو گی\nتھرڈ ٹرم یکم دسمبر سے شروع ہوگی\nسالانہ امتحانات 10 فروری کو ہوں گے\nنوٹ! سالانہ امتحان کے نتائج کا اعلان\nفروری کی 28 تاریخ کو کیا جائے گا"]
    }, {
        "tag": "fees card",
        "patterns": [" فیس کارڈ کتنے  روپے کا ہے", " رزلٹ کارڈ کتنے کا ہے", " رزلٹ کارڈ کی قیمت کیا ہے", " price of result card"],
        "responses": [" فیس کارڈ کی قیمت 70 روپے ہے\n رزلٹ کارڈ کی قیمت 50 روپے ہے"]
    }, {
        "tag": "contact",
        "patterns": ["your phone number"," your contact number"," School cell number"," شبلی سکول کا فون نمبر","شبلی اسکول کا رابطہ نمبر"],
        "responses":["03467711243 \n ubaid243@gmail.com"]
    }, {
        "tag": "میڈیم",
        "patterns": [" kya aapka School English medium hai"," shibli is English medium or Urdu medium" ,"who motivates you"],
        "responses": ["Shiblee school is English medium"]
    }, {
        "tag": "شعر",
        "patterns": [" کوئی شعر سناؤ"],
        "responses": ["خودی کو کر بلند اتنا کہ ہر تقدیر سے پہلے \n خدا بندے سے خود پوچھے، بتا تیری رضا کیا  ہے","ہیں اور بھی دنیا میں سخنور بہت اچھے\n کہتے ہیں کہ غالب کا ہے انداز بیاں اور"]
    }, {
        "tag": " اقوال زریں",
        "patterns": [" Koi aqwal E Zareen sunao"," کوئی اقوال زریں سناؤ"],
        "responses": ["حیا کی سیڑھی سے اگر عورت کا پاؤں پھسل جاۓ تو پورا گھرانہ منہ کے بل گرتا ہے"]
    }, {
        "tag": "Math",
        "patterns": ["i am good", "I'm good", "i am fine", " i'm fine", "good"],
        "responses": ["Good to know!"]
    }, {
        "tag": "Chemistry",
        "patterns": ["covid 19 "],
        "responses": ["..."]
    }, {
        "tag": "biology",
        "patterns": ["you are useless", "useless", "suggest", "suggestions", "you are bad"],
        "responses": ["Please mail your suggestions to ted.thedlbot.suggestions@gmail.com. Thank you for helping me improve!"]
    }, {
        "tag":"کنٹین",
        "patterns": ["کنٹین ہے سکول میں"],
        "context": ["ہاں ہے"]
    }, {
        "tag": " سا ٔییکل سٹینڈ ",
        "patterns": [" سا ٔییکل سٹینڈ ہے "],
        "responses": ["ہاں ھۓ"]
   }, {
  "tag": "yours,تمہارا, آپ  , تہاڈا,یورز ",
  "patterns": [
    "what is your name",
    "tell me your name",
    "name please",
    "what do you go by",
    "may I know your name",
    "what should I call you",
    "your name?",
    "name?",
    "who are you",
    "who goes there",
    "آپ کا نام کیا ہے؟",
    "مجھے اپنا نام بتائیں",
    "براہ کرم نام",
    "آپ کیا جانا چاہتے ہیں",
    "کیا میں آپ کا نام جان سکتا ہوں",
    "میں آپ کو کیا بولوں",
    "آپ کا نام؟",
    "نام؟",
    "آپ کون ہیں",
    "کون ہے وہاں جاتا ہے",
    "توھانوں کا ناں کی اے؟",
    "میں ہیں اپنا ناں",
    "ناں لیس کریو",
    "توھانوں کا ناں کی ہے؟",
    "کیا میں تھاڈے ناں جان سکاں",
    "میں تھاڈا نام جانناں چونداں",
    "تھاڈا ناں؟",
    "ناں؟",
    "توھانوں کی کیندے اے؟",
    "کون ہو؟",
    "توسیں کون ہو؟",
    "کون ہو؟",
    "توں کون بولداں؟",
    " تسی ناں دسوں گے اپنا"
  ],
  "responses":[ "Muhammad Ubaid Akhtar- محمد عبید اختر"]
    },{
  "tag": "presence",
  "patterns": [
    "are Sarwar sahib present. I want to talk to him.",
    "Is Sarwar sahib here? I need to speak with him.",
    "Is Sarwar sahib available? I have something to discuss.",
    "Can I talk to Sarwar sahib?",
    "I would like to speak with Sarwar sahib. Is he around?",
    "Is Sarwar sahib in the office?",
    "Where can I find Sarwar sahib?",
    "Can you let me know if Sarwar sahib is here?",
    "I have a meeting with Sarwar sahib. Is he present?",
    "Is Sarwar sahib currently in the building?",
    "I want to call to sarwar sahib","I want to talk to sarwar sahib","I want to chat to sarwar sahib"
    "کیا سرور صاحب موجود ہیں۔ میں ان سے بات کرنا چاہتا ہوں۔",
    "سرور صاحب یہاں ہیں؟ مجھے ان سے بات کرنی ہے۔",
    "سرور صاحب دستیاب ہیں؟ میں کچھ گفتگو کرنا چاہتا ہوں۔",
    "کیا میں سرور صاحب سے بات کرسکتا ہوں؟",
    "میں سرور صاحب سے بات کرنا چاہتا ہوں۔ کیا وہ موجود ہیں؟",
    "سرور صاحب دفتر میں ہیں؟",
    "میں سرور صاحب کہاں تلاش کرسکتا ہوں؟",
    "کیا آپ مجھے بتا سکتے ہیں کہ سرور صاحب موجود ہیں؟",
    "میری سرور صاحب سے ملاقات ہے۔ کیا وہ موجود ہیں؟",
    "کیا سرور صاحب فی الحال عمارت میں ہیں؟",
    "جی _  انتظار فرمائیے",
    "کیا سرور صاحب موجود ہیں۔ میں ان نال بولنا چاہندا ہاں۔",
    "سرور صاحب کیا یہاں ہندا ہے؟ میں ان نال گل گچ چ کرنا چاہندا ہاں۔",
    "سرور صاحب دستیاب ہندے ہندا ہے؟ میں کجھ کال بولنا چاہندا ہاں۔",
    "کیا میں سرور صاحب نال گل گچ چ کرسکدا ہاں؟",
    "میں سرور صاحب نال بولنا چاہندا ہاں۔ کیا اوہ نال ہندے ہندے ہندے ہندے؟",
    "سرور صاحب دفتر میں ہندے ہندے ہندے ہندے؟",
    "میں سرور صاحب نوں کجھ کال بولنا چاہندا ہاں؟",
    "کیا آپ میں سرور صاحب نال گل گچ چ کرسکدے ہو؟",
    "میں سرور صاحب نوں کجھ ملاقات ہے۔ کیا اوہ موجود ہے؟",
    "کیا سرور صاحب فی الحال عمارت میں ہندے ہندے ہندے ہندے؟","سرور صاحب نا گپ شپ لاونی سی"
  ],
  "responses" :[" جی موجود ہیں فون کال کیجئے\nSarwar Shiblee College\nMobile: 0340 0075179 "]



},{
  "tag": " پرنسپل سے بات  talk to principal",
  "patterns": [
    "I want to talk to Principal Waqar Sahib.",
    "Can I speak with Principal Waqar Sahib?",
    "I need to have a conversation with Principal Waqar Sahib.",
    "Is Principal Waqar Sahib available for a discussion?",
    "May I talk to Principal Waqar Sahib?",
    "I wish to communicate with Principal Waqar Sahib.",
    "Can you connect me to Principal Waqar Sahib?",
    "I would like to speak to Principal Waqar Sahib.",
    "Please put me through to Principal Waqar Sahib.",
    "I have something to discuss with Principal Waqar Sahib.",
    "پرنسپل وقار صاحب سے بات کرنی ہے",
    "مجھے پرنسپل وقار صاحب سے بات کرنی ہے",
    "پرنسپل وقار صاحب کونسی وقت دستیاب ہیں؟",
    "کیا میں پرنسپل وقار صاحب سے بات کر سکتا ہوں؟",
    "میں پرنسپل وقار صاحب سے بات کرنا چاہتا ہوں",
    "کیا آپ مجھے پرنسپل وقار صاحب سے جوڑ سکتے ہیں؟",
    "میں پرنسپل وقار صاحب سے بات کرنا چاہتا ہوں",
    "براہ کرم مجھے پرنسپل وقار صاحب سے جوڑ دیجئے",
    "میں پرنسپل وقار صاحب سے کچھ چیزیں بحث کرنی ہیں",
    "جی موجود ہیں بات کیجئے",
    "پرنسپل وقار صاحب نال بات ہونی اے",
    "مینو پرنسپل وقار صاحب نال بات چاہیدی اے",
    "پرنسپل وقار صاحب دستیاب اے کی نہیں؟",
    "کیا میں پرنسپل وقار صاحب نال بات کر سکدا ہان؟",
    "میں پرنسپل وقار صاحب نال بات کرنا چاہیندا ہان",
    "کیا توں مینو پرنسپل وقار صاحب نال جوڑ سکدا ہان؟",
    "میں پرنسپل وقار صاحب نال بات کرنا چاہیندا ہان",
    "کرپیا مینو پرنسپل وقار صاحب نال جوڑ دیو",
    "میں پرنسپل وقار صاحب نال کجھ گل باتاں کرنیاں ہان"
  ],
  "responses": [
    "جی موجود ہیں فون کال کیجئے\nPrincipal: وقار صاحب\nph: 03447866158"
  ]
},{
  "tag": " سیر، ٹور",
  "patterns": [
    "When will the school tour go to Murree?",
    "What is the date of the school tour to Murree?",
    "Can you tell me when the school trip to Murree is scheduled?",
    "I want to know the timing of the school tour to Murree.",
    "Please inform me about the date of the school excursion to Murree.",
    "When is the school trip to Murree?",
    "What are the dates for the school tour to Murree?",
    "Could you let me know the schedule for the school trip to Murree?",
    "I'm interested to know when the school will visit Murree.",
    "Do you have information about the school tour to Murree?",
    "کب ہو گی مری کے لئے اسکول کی تعطیل سفر؟",
    "مری کے لئے اسکول کی تعطیل کی تاریخ کیا ہے؟",
    "کیا آپ مجھے بتا سکتے ہیں کہ مری کے لئے اسکول کی سیر کا انتظام کب ہوا ہے؟",
    "مجھے معلوم کرنا ہے کہ مری کے لئے اسکول کی سیر کا وقت کیا ہے۔",
    "برائے کرم مجھے مری کے لئے اسکول کی تعطیل کی تاریخ کے بارے میں مطلع کریں۔",
    "مری کے لئے اسکول کی تعطیل کب ہے؟",
    "مری کے لئے اسکول کی تعطیل کی تاریخیں کیا ہیں؟",
    "کیا آپ مجھے مری کے لئے اسکول کی تعطیل کے لئے اسکیڈول کی معلومات فراہم کر سکتے ہیں؟",
    "میں جاننا چاہتا ہوں کہ مری کے لئے اسکول کب جائے گا۔",
    "کیا آپ کو مری کے لئے اسکول کے سفر کے بارے میں معلومات ہے؟",
    "کدھ ہو گی مری کے لئے اسکول کی تعطیل کے لئے اسکیڈول؟",
    "مری کے لئے اسکول کی تعطیل کب ہو گی؟",
    "مری کے لئے اسکول کی سیر کی تاریخوں کیا ہیں؟",
    "کیا آپ مجھے مری کے لئے اسکول کی سیر کا انتظام کا شیڈول بتا سکتے ہیں؟",
    "میں مری کے لئے اسکول کی سیر کوئیڈ ہونا چاہتا ہوں۔",
    "کیا آپ کے پاس مری کے لئے اسکول کی سیر کے بارے میں معلومات ہے؟",
    "جی موجود ہیں بات کیجئے\nٹھنڈے موسم کی چھٹیوں میں"
  ],
  "responses": [
    "During Summer Vacations\n گرمیوں کی چھٹیوں میں جائے گا"
  ]
}


]
 }

import json# write the JSON object to file
with open("intents.json", "w") as f:
    json.dump(data, f)

intents = json.loads(open('intents.json').read())

import tensorflow as tf
import nltk
nltk.download('wordnet')
nltk.download('punkt')
import random
import pickle
import numpy as np
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

words = [] #All tokenized words of  a pattern (one sentence).
classes = []#list of names of all tags
documents = []#list of sentences .Each sentence has tokenized words  .
ignore_letters = ['?','!','.',',']
for intent in data["intents"]:
# mean key named "patterns" of single intent.
#pattern mean one sentence in the "patterns" key wali line main.
    for pattern in intent["patterns"]:
#list of tokenized words in one sentence in "patterns" (single key).
#because word_tokenize returns list
        words_list_of_pattern = nltk.word_tokenize(pattern)
#extend() adds  all but only elements(not list itself) of other list in first list altogether in one turn.
        words.extend(words_list_of_pattern)
        documents.append((words_list_of_pattern, intent["tag"]))
    if intent["tag"] not in classes:
        classes.append(intent["tag"])
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
#set() removes any duplicate element.
#sorted() arrange elements in  list in  Alphabatical ascending order.
words = sorted (set (words))
classes = sorted (set(classes))
pickle.dump (words, open('words.pkl', 'wb'))
pickle.dump (classes, open('classes.pkl', 'wb'))

training_data = []
#creates a list of number of zeros equal to length of classes(no. of tags)
output_empty = [0]*len(classes)
#documents means all documents in all patterns.
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training_data.append([bag, output_row])
random.shuffle(training_data)
training_data = np.array(training_data)


#first_list of array is first(dimension or column) and we will take it as train_x
train_x = list(training_data[:, 0])
#2nd_list of array is 2nd (dimension or column) and we will take it as y_train
train_y = list(training_data[:, 1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))
optimizer=tf.keras.optimizers.SGD(learning_rate=0.1)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
epochs=331
hist = model.fit(np.array(train_x), np.array(train_y), epochs=epochs, batch_size=5, verbose=1)
model.save('chatbotmodel.h5', hist)
print("Done")


import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
#from tensorflow.keras.models import load_model
lemmatizer = WordNetLemmatizer()
#intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
sentences = pickle.load(open('classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize (word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for W in sentence_words:
        for i, word in enumerate(words):
            if word == W:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words (sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res)
if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


import random
def get_response(intents_list, intents_json):
    # Extract the predicted intent from the intents_list
    tag = intents_list[0]['intent']
    # Retrieve the list of intents from intents_json
    list_of_intents = intents_json['intents']
    # Search for a matching intent in the list_of_intents
    for i in list_of_intents:
        if i['tag'] == tag:
            # If a matching intent is found,
    #return a random response from its list
           return random.choice(i['responses'])
           if i['tag'] != tag:
# If no matching intent is found, return a default responses written.
               print( "Sorry, I can't answer that. It's not relevant to me.")
print("Welcome to Shiblee College! \n Ask your Questions!")
while True:
    message=input(" ")
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)