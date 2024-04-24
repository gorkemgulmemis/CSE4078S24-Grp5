import json

girdi_dosyasi = "duzenlenmis_veri.json"
cikti_dosyasi = "duzenlenmis_veri.json"

with open(girdi_dosyasi, "r", encoding="utf-8") as f:
    veri = json.load(f)


duzenlenmis_veri = []

for satir in veri:
    
    duzenlenmis_veri.append({
        "instruction": "Aşağıdaki yorumun duygu durumunun olumlu veya olumsuz olduğunu söyle",
        "input": satir["input"].capitalize(),
        "output": satir["output"].capitalize()
    })

with open(cikti_dosyasi, "w", encoding="utf-8") as f:
    json.dump(duzenlenmis_veri, f, ensure_ascii=False, indent=4)

print("Dönüşüm tamamlandı. Çıktı dosyası:", cikti_dosyasi)
