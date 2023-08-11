import os
from time import sleep
from pytube import Search
from pytube import YouTube
from rich import print
from complementary import printHeader,  clearName


ytSearchHeader = ["\n", "-"*60, "Resultados".center(60), ("-"*10).center(60)]
def ytSearch(userSearch):
    printHeader(ytSearchHeader)

    searchResults = Search(userSearch).results  # <pytube.__main__.YouTube object: videoId=fJ9rUzIMcZQ>

    for i in range(len(searchResults)):
        print(f"[{i+1}] - {searchResults[i].title}")
        #sleep(0.2)
    print("-"*60)

    return searchResults


def download(vidObject):
    print("\n⚡ Iniciando o download...")
    title = clearName(vidObject.title)
    path = f"./storage/{title}_{vidObject.video_id}"  # ID no path para evitar conflitos

    video = YouTube(f'https://www.youtube.com/watch?v={vidObject.video_id}', use_oauth=True)  # acessar vídeos +18
    file = video.streams.get_highest_resolution().download(path, filename=f"{title}.mp4")
    print("✅ [green]Download finalizado com sucesso![/green]\n")

    mp4path = f"{path}/{os.path.split(file)[1]}"
    return mp4path
