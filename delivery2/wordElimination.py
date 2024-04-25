import json

# Verilen JSON dosyasının yolu
dosya_yolu = "duzenlenmis_veri2.json"

# Silmek istediğiniz kelimelerin listesi
istenmeyen_kelimeler = ["sikiş", "sex", "seks", "sikis", "sapık", "cinsel", "akp", "chp", "hdp", "pkk", "mhp", "tayyip", "erdoğan", 
                        "kılıcdaroglu", "kılıçtaroğlu", "devlet", "hükümet", "orospu", "piç", "pic", "orospu", "hdpkk", "azgın", "sikici", 
                        "erotik", "am", "dul", "ensest", "porno", "porn", "türkifsa", "ifsa", "ifşa", "dul", "sikilmek", "bosalma", "boşalma", 
                        "cuckold", "porn", "olgun", "göt", "got", "swinger", "azdım", "azmak", "liseli", "türbanlı", "eskort", "kerhane",
                        "pezevenk", "sokam", "gavat", "suriyeli", "suriye", "tecavüz", "tecavuz", "amk", "şerefsiz", "serefsiz", "fahise",
                        "fahişe", "iftira", "provokasyon", "bomba", "kürt" , "kurt", "terorist", "anasını", "siken", "embesil", "piclere",
                        "kahpe", "kevaşe", "kaltak", "arab", "pişkin", "siksin","amcıgını", "godoş", "götlek", "yanıııııkkkkk", "yanık", "pkk",
                        "hdp", "orul", "sictimin", "hımına", "domal", "yarra", "sikerim", "aq", "kaypaklık", "bok", "sakso", "bdsm", "sahine", 
                        "mistress", "kole", "slave", "fetiş", "travesti", "yalatmak", "fuck", "fuckbody", "yosma", "öpüşmek", "sanalsex", 
                        "astürbasyon", "anal", "oral", "boşalma", "brazzers", "nude", "erotik", "sürtük", "nah", "fetö", "feto","itahat", 
                        "sokim", "aptal", "salak", "gerizekalı", "yavsak", "yavşak", "swinger", "ayak", "fetiş", "sugar", "sugardaddy", 
                        "daddy", "tanga", "ak parti", "demokrat", "mhp", "dem", "parlamenter", "parlementer", "kaymakam", "muhtar", "siyasi", 
                        "siyasal", "siyaset", "siyasetçi", "politika", "politik", "partileri", "başkan", "baskan", "belediye", "büyükşehir",
                        "gazate", "muhalefet", "vekil", "milletvekili", "kamu", "hiyerarşik", "senatör", "büyükelçi", "reform", "reformist",
                        "senato", "istihbarat", "terorıst", "teror", "terörizm", "vali", "doğu perinçek", "içişleri bakanı", "atatürk", 
                        "turgut özal", "devlet bahceli", "erkan baş", "tbmm", "binali yıldırım", "mevlüt çavuşoğlu", "berat albayrak",
                        "ismail kahraman", "fahrettin koca","ömer çelik", "turizm bakanı","fatma şahin" ,"feminist","feminizm",
                        "iç işleri","dış işleri","aktivist","cumhuriyet halk partisi", "adalet ve kalkınma partisi" ,"iyi parti" ,"solcu",
                        "solcular" ,"sol parti","sağcı","yeşiller partisi","bağımsız","türkiye","vatan haini","vatan partisi","saadet partisi"
                        ,"elçi","yargıç","seçmen","liberalizm","muhalefet","burjuvazi","kamuouyu","sözleşme","millet","örgüt","manifesto" ,
                        "sistem","anarşist","partizan","egemenlik","halk","devlet","cumhurbaşkanı","brokrasi","staliko","rejim","cumhuriyet"
                        ,"ülkücü","ideolojik","meclis","anayasa" ,"güçler ayrılığı","hukuk","yasama","bakan","otoriter","rejim","dünya savaşı",
                        "sovyet","senato","sivil haklar","ayaklanma","vatandaşlık","otonomi","barış anlaşması","anlaşma" ,"antlaşma","suikast",
                        "federasyon","konfederasyon","seçim bölgesi" ,"siyasetçi","bülent ecevit","devrim","tayip","silivri","darbe",
                        "büyükşehir belediye","mansur yavaş","diplomat","ekonomi","yunan dölleri","çatışma" ,"yolsuzluk" ,"lobi","diplomasi",
                        "propaganda","azınlık","ittifak","koalisyon","ırkçılık","manifesto","meral akşener","komunist" ,"sandık","sandık alanları"
                        ,"komunizm","populizm","populist","popülizm","iktidar","referandum","hitler","faşist","diktatör","otokrasi","totalitarizm"
                        ,"sosyalizm","sosyalist","kapitalizm","kapitalist","liberalizm","ulus" ,"ulusal" ,"ulusalcılık","muhafazakar",
                        "muhafazakarlık","ulusal","politikacı","siyasi parti","parlamenter","heyet" ,"protesto","miting","boykot","kanun"
                        ,"kararname" ,"yönetmelik","kayyum","savaş" ,"üstteğmen","propaganda","hükümet","demokrat" ,"demokrasi","gelecek partisi"
                        ,"ahmet davutoğlu","iyi parti","anavatan partisi","genel seçim","yerel seçim", "sik", "taşak", "tasak", "kevase", "öküz",
                        "kasar", "kaşar", "fuhus", "fuhuş", "küfür", "ananıskm","dürzü", "bela", "eşşek", "puşt", "oy hakkı","sömürge",
                        "silahlanma yarışı","silahlanma" ,"komutan","asker","askeri","komünist partisi","deniz gezmiş","mebus" ,"cami" ,"tanrı" ,
                        "ülke","osmanlı","sınır","ermenistan","komutan","tümen","güvenlik güçleri","çin","intihar etmek","arafat","aristokrasi",
                        "birlik","süvari","hür","yönetim biçimi" ,"açık yönetim","örtülü yönetim","monarşi","kadın hakları" ,"kölelik",
                        "işçi partisi","iş cinayetleri","ordu"]

# JSON dosyasını açıp veriyi yükleme
with open(dosya_yolu, "r", encoding="utf-8") as dosya:
    veri = json.load(dosya)

# İstenmeyen kelimeleri kontrol ederek uygun cümleleri filtreleme
filtrelenmis_veri = [yorum for yorum in veri if not any(kelime.lower() in yorum["input"].lower() for kelime in istenmeyen_kelimeler)]

# Filtrelenmiş veriyi dosyaya yazma
with open(dosya_yolu, "w", encoding="utf-8") as dosya:
    json.dump(filtrelenmis_veri, dosya, ensure_ascii=False, indent=4)

print("İstenmeyen kelimeler içeren cümleler silindi.")
