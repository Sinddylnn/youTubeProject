from rich import print
from complementary import printHeader, pathAlreadyExists, clearName
from ai import translate, writing
from editor import legend
import googletrans

languageSelectorHeader = ["\n", "-"*60, "Idiomas".center(60), ("-"*10).center(60)]
def languageSelector():
    printHeader(languageSelectorHeader)
    for i, (codes, language) in enumerate(googletrans.LANGUAGES.items()):
        print(f"[{i+1}] - {language.title()}" )
    print("-"*60)

    try: 
        selectedLanguage = int(input("Selecione o idioma de destino: "))
    except ValueError:
        print("[red]Informe apenas o número correspondente ao idioma.[/red]")
        exit()
    except KeyboardInterrupt:
        print("\n[yellow]Operação de selecionar idiomas encerrada pelo usuário[/yellow]")
        exit()
    
    languageCodes = list(googletrans.LANGUAGES.keys())
    if  1 <= selectedLanguage <= len(languageCodes):
        languageCode = languageCodes[selectedLanguage-1]
    else:
        print("[red]Esse número não corresponde a nenhum idioma![/red]")
        exit()

    return languageCode


def videoSelector(videoObjects):
    try:
        selectedVideo = int(input("Selecione um resultado: "))
    except ValueError:
        print("[red]Informe apenas o número correspondente ao vídeo.[/red]")
        exit()
    except KeyboardInterrupt:
        print("\n[yellow]Seleção encerrada pelo usuário.[/yellow]")
        exit()

    if 1 <= selectedVideo <= len(videoObjects):
        vidObject = videoObjects[selectedVideo-1]
    else:
        print("[red]Esse número não corresponde a nenhum vídeo![/red]")
        exit()

    return vidObject
    