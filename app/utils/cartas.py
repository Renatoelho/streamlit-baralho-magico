
import os
from pathlib import Path
from random import sample


caminho_cartas = f"{Path(os.path.abspath(__file__)).parent.parent}/imagens/"

CARTAS = [
    ["01full.jpg", "01half.jpg", "01plus.jpg"],
    ["02full.jpg", "02half.jpg", "02plus.jpg"],
    ["03full.jpg", "03half.jpg", "03plus.jpg"],
    ["04full.jpg", "04half.jpg", "04plus.jpg"],
    ["05full.jpg", "05half.jpg", "05plus.jpg"],
    ["06full.jpg", "06half.jpg", "06plus.jpg"],
    ["07full.jpg", "07half.jpg", "07plus.jpg"],
    ["08full.jpg", "08half.jpg", "08plus.jpg"],
    ["09full.jpg", "09half.jpg", "09plus.jpg"],
    ["10full.jpg", "10half.jpg", "10plus.jpg"],
    ["11full.jpg", "11half.jpg", "11plus.jpg"],
    ["12full.jpg", "12half.jpg", "12plus.jpg"],
    ["13full.jpg", "13half.jpg", "13plus.jpg"],
    ["14full.jpg", "14half.jpg", "14plus.jpg"],
    ["15full.jpg", "15half.jpg", "15plus.jpg"],
    ["16full.jpg", "16half.jpg", "16plus.jpg"],
    ["17full.jpg", "17half.jpg", "17plus.jpg"],
    ["18full.jpg", "18half.jpg", "18plus.jpg"],
    ["19full.jpg", "19half.jpg", "19plus.jpg"],
    ["20full.jpg", "20half.jpg", "20plus.jpg"],
    ["21full.jpg", "21half.jpg", "21plus.jpg"],
    ["22full.jpg", "22half.jpg", "22plus.jpg"],
    ["23full.jpg", "23half.jpg", "23plus.jpg"],
    ["24full.jpg", "24half.jpg", "24plus.jpg"],
    ["25full.jpg", "25half.jpg", "25plus.jpg"],
    ["26full.jpg", "26half.jpg", "26plus.jpg"],
    ["27full.jpg", "27half.jpg", "27plus.jpg"],
    ["28full.jpg", "28half.jpg", "28plus.jpg"],
    ["29full.jpg", "29half.jpg", "29plus.jpg"],
    ["30full.jpg", "30half.jpg", "30plus.jpg"],
    ["31full.jpg", "31half.jpg", "31plus.jpg"],
    ["32full.jpg", "32half.jpg", "32plus.jpg"],
    ["33full.jpg", "33half.jpg", "33plus.jpg"],
    ["34full.jpg", "34half.jpg", "34plus.jpg"],
    ["35full.jpg", "35half.jpg", "35plus.jpg"],
    ["36full.jpg", "36half.jpg", "36plus.jpg"],
    ["37full.jpg", "37half.jpg", "37plus.jpg"],
    ["38full.jpg", "38half.jpg", "38plus.jpg"],
    ["39full.jpg", "39half.jpg", "39plus.jpg"],
    ["40full.jpg", "40half.jpg", "40plus.jpg"],
    ["41full.jpg", "41half.jpg", "41plus.jpg"],
    ["42full.jpg", "42half.jpg", "42plus.jpg"],
    ["43full.jpg", "43half.jpg", "43plus.jpg"],
    ["44full.jpg", "44half.jpg", "44plus.jpg"],
    ["45full.jpg", "45half.jpg", "45plus.jpg"],
    ["46full.jpg", "46half.jpg", "46plus.jpg"],
    ["47full.jpg", "47half.jpg", "47plus.jpg"],
    ["48full.jpg", "48half.jpg", "48plus.jpg"],
    ["49full.jpg", "49half.jpg", "49plus.jpg"],
    ["50full.jpg", "50half.jpg", "50plus.jpg"],
    ["51full.jpg", "51half.jpg", "51plus.jpg"],
    ["52full.jpg", "52half.jpg", "52plus.jpg"]
]

def selecionando_cartas() -> list:
    selecionadas = sample(CARTAS, 15)
    selecionadas = (
        [
            [
                f"{caminho_cartas}{cartas[0]}",
                f"{caminho_cartas}{cartas[1]}",
                f"{caminho_cartas}{cartas[2]}"
            ] 
            for cartas in selecionadas
        ]
    )
    
    return selecionadas
