import os
from rich import print
import whisper
from whisper.utils import write_srt
from googletrans import Translator


def transcribe(mp4path):
    print("⚡ Iniciando a criação da legenda...")
    model = whisper.load_model("tiny")  # tiny, base, small, medium, large
    transcription = model.transcribe(mp4path, fp16=False)  # fp16 não suportado pela AMD, usando fp32
    #print(transcription["segments"]["avg_logprob"])

    originalSubtitles = f"{os.path.splitext(mp4path)[0]}.srt"
    with open(originalSubtitles, "w", encoding="utf-8") as srt:
         write_srt(transcription["segments"], file=srt) 
    print("✅ [green]Legenda criada com sucesso![/green]")

    return originalSubtitles


versos = []
def translate(originalSubtitles, languageCode):
    print("\n⚡ Iniciando a tradução da legenda...")
    with open(originalSubtitles, "r") as f:
        for line in f:
            if line[0].isnumeric():
                versos.append(line.strip())
            else:
                translation = Translator().translate(line, dest=languageCode)
                versos.append(translation.text.strip())
    print("✅ [green]Legenda traduzida com sucesso![/green]\n")

    translatedSubtitles = f"{os.path.splitext(originalSubtitles)[0]}_{languageCode}.srt"
    return translatedSubtitles


def writing(translatedSubtitles):
    with open(translatedSubtitles, "w") as f:
        for i in range(len(versos)):
            f.write(f"{versos[i]}\n")

    return translatedSubtitles
