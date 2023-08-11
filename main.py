"""To-do list
- implementar logica quando a legenda ja existe
- graficos da precissão
"""

from ai import transcribe, translate, writing
from complementary import printHeader
from editor import legend
from menus import videoSelector, languageSelector
from youtube import ytSearch, download


mainHeader = ["-"*60, "YouTube Legender".center(60), "Legendas em qualquer idioma para videos no YT.".center(60), "-"*60]
printHeader(mainHeader)

try:
    userSearch = input("Pesquise um vídeo: ")
except KeyboardInterrupt:
    print("\n[yellow]Pesquisa encerrada pelo usário[/yellow]")
    exit()

video = videoSelector(ytSearch(userSearch))
language = languageSelector()
versos = translate(transcribe(download(video)), language)
legend((writing(versos)))
