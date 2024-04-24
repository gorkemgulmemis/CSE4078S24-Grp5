import json

# Veri setini yükle
with open('güncel json.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Yeni düzenlenmiş veri listesi
new_data = []

# Her bir girdi için döngü
for i in range(len(data["column0"])):
    input_text = data["column0"][i]
    label = data["column1"][i]

    # Duygu durumunu olumlu veya olumsuz olarak belirle
    if label == "Positive":
        output = "Olumlu"
    elif label == "Notr":
        output = "Notr"
    else:
        output = "Olumsuz"

    # Inputları büyük harfle başlat
    input_text = input_text.capitalize()

    # Yeni formata uygun veri oluştur
    new_entry = {
        "instruction": "Aşağıdaki yorumun duygu durumunun olumlu veya olumsuz olduğunu söyle",
        "input": input_text,
        "output": output
    }

    # Yeni veri listesine ekle
    new_data.append(new_entry)

# Yeni veriyi dosyaya yaz
with open('duzenlenmis_veri2.json', 'w', encoding='utf-8') as file:
    json.dump(new_data, file, ensure_ascii=False, indent=4)
