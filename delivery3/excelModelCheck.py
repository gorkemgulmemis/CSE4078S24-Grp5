from transformers import TextStreamer, AutoTokenizer, AutoModelForCausalLM
import torch
import openpyxl

# Tokenizer ve modeli yükleyin
#tokenizer = AutoTokenizer.from_pretrained('modelinizin_yolu')
#model = AutoModelForCausalLM.from_pretrained('modelinizin_yolu').to('cuda')

# TextStreamer nesnesini oluşturun
text_streamer = TextStreamer(tokenizer)

# Excel dosyasını yükleyin
wb = openpyxl.load_workbook('NLP Tablo.xlsx')
sheet = wb.active

# Excel dosyasındaki verileri kullanarak modeli çalıştırın
for row in range(2, sheet.max_row):
    # Excel dosyasından instruction ve input alın
    instruction = sheet[f'B{row}'].value
    input_text = sheet[f'C{row}'].value

    # Model için girdileri hazırlayın
    inputs = tokenizer(
        [
            alpaca_prompt.format(instruction, input_text, "")
        ],
        return_tensors="pt"
    ).to("cuda")

    # Modeli çalıştırın ve sonuçları alın
    outputs = model.generate(**inputs, streamer=text_streamer, max_new_tokens=128)

    # Sonuçları decode edin ve Excel dosyasına yazın
    # Sonuçları decode edin
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # İlk olarak, sadece modelin ürettiği çıktıyı (output) ayıklayın
    output_only = result.split(input_text)[-1].strip()

    # Daha sonra, başındaki 'Response:' yazısını silin
    final_output = output_only.replace('Response:', '').strip()

    # Çıktıyı "olumlu", "olumsuz" veya "nötr" olarak etiketleyin
    if "olumlu" in final_output.lower():
        labeled_output = "olumlu"
    elif "olumsuz" in final_output.lower():
        labeled_output = "olumsuz"
    else:
        labeled_output = "nötr"

    # Son olarak, etiketlenmiş çıktıyı Excel dosyasının F sütununa yazdırın
    sheet[f'S{row}'].value = labeled_output

    # Eğer instructionlar biterse döngüden çık
    if not instruction:
        break

# Excel dosyasını kaydedin
wb.save(' New NLP Tablo.xlsx')
