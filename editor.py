import os
from rich import print


def legend(subtitles):
    print("⚡ Adicionando legenda ao vídeo...")
    inputFile = f"{subtitles[:-7]}.mp4"
    outputFile = f"{os.path.splitext(subtitles)[0]}_legended.mp4"

    comando = f"ffmpeg -i {inputFile} -vf subtitles={subtitles} {outputFile}"  # >/dev/null 2>&1
    os.system(comando)

    print("✅ [green]Legenda adicionada com sucesso![/green]")
