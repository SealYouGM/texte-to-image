import numpy as np
from PIL import Image
import os

######################## Reprend le chemin d'accès du dossier à partir du log ########################
def get_path():
    path = os.getcwd()
    return(path)

def character_to_color(character, niveau_gris):
    color = niveau_gris.find(character)*255/len(niveau_gris)
    if color < 0:
        color = 0
    #print(color)
    return(int(color))

def creation_image(path, nom_image, gris):
    with open(path+"\\"+nom_image+".txt", "r", encoding='utf-8') as image_txt:
        image_string = image_txt.readlines()

    w = len(image_string[0])
    print(w)
    h = len(image_string)
    print(h)
    pixel = [] #265, 85
    image = Image.new("L",(w,h)) #265, 85
    for ligne in image_string:
        for character in ligne:
            couleur = character_to_color(character, gris)
            pixel.append(couleur)
    image.putdata(pixel)

    image.save(path+"\\"+nom_image+".jpeg")
  
######################## MAIN ########################
def main():
    
    nom_image = input("Entrez le nom du fichier texte à transformer en image : ")
    gris_choix = input("Nuance de gris [10] ou [70] (niveau de précision): ")
    nuance_gris = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    if gris_choix == 10:
        nuance_gris = "@%#*+=-:. "
    elif gris_choix ==70:
        nuance_gris = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    elif gris_choix == -1:
        nuance_gris = "abcdefghijklmnopqrstuvwxyz"

    print("Création du chef d'oeuvre en cours...")
    path = get_path()
    creation_image(path, nom_image, nuance_gris)
    print("Tadam!")

if __name__ == "__main__":
    main()