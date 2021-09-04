# -*- coding: utf-8 -*-


"""


/////////////////////////////////////////////////////////////////////////////////////////
///                                    H E X A P A W N                                  /
/////////////////////////////////////////////////////////////////////////////////////////


"""



"""
--------------------------------------------
-Import des différents modules nécessaires -
--------------------------------------------
"""
from tkinter import *
from PIL import ImageTk, Image
import os
import sys 
import time
from random import *
from math import *
from winsound import *


"""
---------------------------
-Définition des fonctions -
---------------------------
"""

def creation_fenetre(fenetre):
    """permet de définir la taille de la fenêtre (ici résolution 500x500)
              de le centrer au milieu de l'écran
              et de faire en sorte que l'utilisateur ne puisse pas changer la taille
              de le nommer
    """

    #Récupérer la résolution de l'écran utilisé
    screen_x = int(fenetre.winfo_screenwidth())
    screen_y = int(fenetre.winfo_screenheight())

    #Entrer les valeurs de taille de la fenêtre
    window_x = 500
    window_y = 500

    #Calcul des coordonnées pour que la fenêtre soit au milieu
    pos_x = (screen_x // 2) - (window_x // 2)
    pos_y = (screen_y // 2) - (window_y // 2)
    geo = "{}x{}+{}+{}".format(window_x, window_y, pos_x, pos_y)

    app.geometry(geo)
    #On bloque la taille en 500x500
    app.resizable(width=False, height=False)
    app.title("Potatopawn")

def quitter_programme () :
    print("quitter programme")
    sys.exit(0)


def import_img () :
    """ va chercher toutes les images dont on a besoin pour le jeu
        renvoie un tableau contenant toutes les images """
    app_path = os.getcwd()
    tab = []

    #0 game background
    background = ImageTk.PhotoImage(Image.open(app_path+"/img/hexapawn_fond.png").resize((500, 500), Image.ANTIALIAS))
    tab.append(background)
    #1 potato rouge
    happypotato = ImageTk.PhotoImage(Image.open(app_path+"/img/pion_cute_potato.png").resize((100, 100), Image.ANTIALIAS))
    tab.append(happypotato)
    #2 potato blue
    sadlypotato = ImageTk.PhotoImage(Image.open(app_path+"/img/pion_sad_potato.png").resize((100, 100), Image.ANTIALIAS))
    tab.append(sadlypotato)
    #3
    spotted = ImageTk.PhotoImage(Image.open(app_path+"/img/spotted.png").resize((100, 100), Image.ANTIALIAS))
    tab.append(spotted)
    #4
    clicked = ImageTk.PhotoImage(Image.open(app_path+"/img/clicked.png").resize((100, 100), Image.ANTIALIAS))
    tab.append(clicked)
    #5
    victoirer = ImageTk.PhotoImage(Image.open(app_path+"/img/victoirer.png").resize((70, 70), Image.ANTIALIAS))
    tab.append(victoirer)
    #6
    victoireb = ImageTk.PhotoImage(Image.open(app_path+"/img/victoireb.png").resize((70, 70), Image.ANTIALIAS))
    tab.append(victoireb)
    #7
    bg_menu = ImageTk.PhotoImage(Image.open(app_path+"/img/hexapawn_menu.png").resize((500, 500), Image.ANTIALIAS))
    tab.append(bg_menu)
    #8
    quitter = ImageTk.PhotoImage(Image.open(app_path+"/img/quitter.png").resize((95, 65), Image.ANTIALIAS))
    tab.append(quitter)
    #9
    pvp = ImageTk.PhotoImage(Image.open(app_path+"/img/pvp.png").resize((95, 95), Image.ANTIALIAS))
    tab.append(pvp)
    #10
    pvia = ImageTk.PhotoImage(Image.open(app_path+"/img/pvia.png").resize((95, 95), Image.ANTIALIAS))
    tab.append(pvia)
    #11
    noob = ImageTk.PhotoImage(Image.open(app_path+"/img/noob.png").resize((95, 95), Image.ANTIALIAS))
    tab.append(noob)
    #12
    normal = ImageTk.PhotoImage(Image.open(app_path+"/img/normal.png").resize((95, 95), Image.ANTIALIAS))
    tab.append(normal)
    #13
    hard = ImageTk.PhotoImage(Image.open(app_path+"/img/hard.png").resize((95, 95), Image.ANTIALIAS))
    tab.append(hard)

    return tab


def initialisation_damier () :
    """
    code du damier :
    une case = ab
    a = _ -> case vide
    a = R -> pion rouge
    a = B -> pion bleu

    b = C -> case clicked 
    b = S -> case spotted


    """


    global damier
    damier = [["B_","B_","B_"],
              ["__","__","__"],
              ["R_","R_","R_"]]





def coords_clic_rouge (xb, yb) :

    global round

    global damier


    if xb > 90 and xb < 410 and yb > 90 and yb < 410 :

        """on récupère les coordonnées du clic et on le convertit en index du tableau damier """
        CoordsDamier = CoordsToIndex (xb, yb)
        ordonnee = CoordsDamier[0]
        abcisse = CoordsDamier[1]


        if damier[ordonnee][abcisse][0] == "R" :
            nettoyage_damier ()

            damier[ordonnee][abcisse] = damier[ordonnee][abcisse][0] + "C"


            if damier[ordonnee-1][abcisse][0] == "_" :
                damier[ordonnee-1][abcisse] = damier[ordonnee-1][abcisse][0] + "S"


            if abcisse != 0 and damier[ordonnee-1][abcisse-1][0] == "B" :
                damier[ordonnee-1][abcisse-1] = damier[ordonnee-1][abcisse-1][0] + "S"

            if abcisse != 2 and damier[ordonnee-1][abcisse+1][0] == "B" :
                damier[ordonnee-1][abcisse+1] = damier[ordonnee-1][abcisse+1][0] + "S"



        elif damier[ordonnee][abcisse][1] == "S" :
            for x2 in range (3) :
                for y2 in range (3) :
                    if damier[y2][x2][1] == "C" :
                        ordonneeS, abcisseS = y2, x2
                
            damier[ordonneeS][abcisseS] = "__"
            damier[ordonnee][abcisse] = "R_"

            #PlaySound(app_path+"/img/pok", SND_FILENAME)

            nettoyage_damier ()
            round += 1

        else :
            nettoyage_damier ()

    else :
        print("click hors damier")
        nettoyage_damier ()

def IAplay (xb, yb) :

    global round
    global damier
    global pattern
    global liste_move



    if xb > 90 and xb < 410 and yb > 90 and yb < 410 :

        """on récupère les coordonnées du clic et on le convertit en index du tableau damier """
        CoordsDamier = CoordsToIndex (xb, yb)
        ordonnee = CoordsDamier[0]
        abcisse = CoordsDamier[1]


        if damier[ordonnee][abcisse][0] == "R" :
            nettoyage_damier ()

            damier[ordonnee][abcisse] = damier[ordonnee][abcisse][0] + "C"


            if damier[ordonnee-1][abcisse][0] == "_" :
                damier[ordonnee-1][abcisse] = damier[ordonnee-1][abcisse][0] + "S"


            if abcisse != 0 and damier[ordonnee-1][abcisse-1][0] == "B" :
                damier[ordonnee-1][abcisse-1] = damier[ordonnee-1][abcisse-1][0] + "S"

            if abcisse != 2 and damier[ordonnee-1][abcisse+1][0] == "B" :
                damier[ordonnee-1][abcisse+1] = damier[ordonnee-1][abcisse+1][0] + "S"



        elif damier[ordonnee][abcisse][1] == "S" :
            for x2 in range (3) :
                for y2 in range (3) :
                    if damier[y2][x2][1] == "C" :
                        ordonneeS, abcisseS = y2, x2
                
            damier[ordonneeS][abcisseS] = "__"
            damier[ordonnee][abcisse] = "R_"

            nettoyage_damier ()
            
            round += 1
            


            """

            IA

            """






            #jeu de l'IA


            somme_score = 0
            liste_move = []

            #on cherche un damier identique
            for i in range (len(pattern)) :
                if damier == pattern[i][0] :
                    print ("index du damier : ", i)


                    #on parcourt les déplacements de ce pattern et on somme les scores
                    for k in range (len(pattern[i][1])) :
                        score_temp = int(pattern[i][1][k]["score"])
                        move_score = calcul_proba (score_temp)
                        print("move ", k, " - ", pattern[i][1][k]["score"], " score final = ", move_score)

                        somme_score += move_score
                        liste_move.append(move_score)

                    if somme_score == 0 :
                        index_move = randint (0, len(liste_move)-1)


                    else :
                        #on transforme chaque score en pourcentage de probabilité
                        for e in range (len(liste_move)) :
                            liste_move[e] = (liste_move[e] / somme_score) * 100



                         #sommation de chaque proba avec ceux qui précèdent
                        if len(liste_move) > 1 :
                            for k in range (1, len(liste_move) - 1) :
                                liste_move[k] = liste_move[k-1] +  liste_move[k]
                        liste_move[-1] = 100
                        print (liste_move)

                        tirage = randint(1,100)

                        for p in range (len(liste_move)) :
                            if  tirage <= liste_move[p] :
                                print ("move = ", p)
                                index_move = p
                                break

                    #on met le déplacement en mémoire
                    selected_move.append ([int(i),int(index_move)])


                    damier[pattern[i][1][index_move]["y1"]][pattern[i][1][index_move]["x1"]] = "__"
                    damier[pattern[i][1][index_move]["y2"]][pattern[i][1][index_move]["x2"]] = "B_"

                   

                    round += 1


        else :
            nettoyage_damier ()

    else :
        print("click hors damier")
        nettoyage_damier ()


def calcul_proba (score) :
    global n

    if score <= 0 :
        return 0
    
    
    return (score**n)



def coords_clic_bleu (xb, yb) :
    
    global round
    global damier

    if xb > 90 and xb < 410 and yb > 90 and yb < 410 :

        """on récupère les coordonnées du clic et on le convertit en index du tableau damier """
        CoordsDamier = CoordsToIndex (xb, yb)
        ordonnee = CoordsDamier[0]
        abcisse = CoordsDamier[1]


        if damier[ordonnee][abcisse][0] == "B" :
            nettoyage_damier ()

            damier[ordonnee][abcisse] = damier[ordonnee][abcisse][0] + "C"


            if damier[ordonnee+1][abcisse][0] == "_" :
                damier[ordonnee+1][abcisse] = damier[ordonnee+1][abcisse][0] + "S"


            if abcisse != 0 and damier[ordonnee+1][abcisse-1][0] == "R" :
                damier[ordonnee+1][abcisse-1] = damier[ordonnee+1][abcisse-1][0] + "S"

            if abcisse != 2 and damier[ordonnee+1][abcisse+1][0] == "R" :
                damier[ordonnee+1][abcisse+1] = damier[ordonnee+1][abcisse+1][0] + "S"



        elif damier[ordonnee][abcisse][1] == "S" :
            for x2 in range (3) :
                for y2 in range (3) :
                    if damier[y2][x2][1] == "C" :
                        ordonneeS, abcisseS = y2, x2
                
            damier[ordonneeS][abcisseS] = "__"
            damier[ordonnee][abcisse] = "B_"

            nettoyage_damier ()
            round += 1

        else :
            nettoyage_damier ()

    else :
        print("click hors damier")
        nettoyage_damier ()


def coords_clic(event):
    """ Toutes les actions liées au clic gauche de l'utilisateur"""


    global round
    global gamemode
    global game_state

    xb = event.x
    yb = event.y

    if game_state == "game" :

        if gamemode == 2 :
            if round % 2 == 0 :
                coords_clic_rouge (xb, yb)
        
            else :
                coords_clic_bleu (xb, yb)

        elif gamemode == 1 :
            if round % 2 == 0 :
                IAplay (xb, yb)

        update_game ()

    elif game_state == "end" :
        game_state = "game"
        initialisation_damier ()
        update_game ()


def nettoyage_damier () :
    for x2 in range (3) :
        for y2 in range (3) :
            damier[x2][y2] = damier[x2][y2][0] + "_"


def IndexToCoords (x, y) :
    x2 = 90 + y * 110
    y2 = 90 + x * 110
    t = [x2, y2]
    return t

def CoordsToIndex (x, y) :
    x2 = (y - 90) // 110
    y2 = (x - 90) // 110
    t = [x2, y2]
    return t

def afficher_damier (tableau) :
    """ Fonction qui va lire un tableau représentant les placements des pions sur le damier, et qui va placer les images correspondantes
        sur l'écran du jeu"""


    canvas.create_image(250, 250,  image=img[0])


    #affichage des lunettes
    if lastWinner == "R" :
        canvas.create_image(10, 420, image=img[5], anchor=NW)
    elif lastWinner == "B" :
        canvas.create_image(420, 420, image=img[6], anchor=NW)




    for ligne in range (3) :
        for colonne in range (3) :


            if tableau[ligne][colonne][0] == "B" :
                coords = IndexToCoords (ligne,colonne)
                imgPion1 = canvas.create_image(coords[0], coords[1], image=img[2], anchor=NW)


            elif tableau[ligne][colonne][0] == "R" :
                coords = IndexToCoords (ligne,colonne)
                imgPion2 = canvas.create_image(coords[0], coords[1], image=img[1], anchor=NW)


            if tableau[ligne][colonne][1] == "S" :
                coords = IndexToCoords (ligne,colonne)
                imgSpotted = canvas.create_image(coords[0], coords[1], image=img[3], anchor=NW)


            elif tableau[ligne][colonne][1] == "C" :
                coords = IndexToCoords (ligne,colonne)
                imgCLicked = canvas.create_image(coords[0], coords[1], image=img[4], anchor=NW)


    canvas.create_text(360, 460, text = str(ScoreBleu), font=("Helvetica", 55))
    canvas.create_text(140, 460, text = str(ScoreRouge), font=("Helvetica", 55))


def check_resultat () :
    """ FOnction qui détermine s'il y a un gagnant dans cette manche
        est activé à chaque déplacement"""
    nbPionBleu = 0
    nbPionRouge = 0
    spotted = 0

    for y in range (3) :
        for x in range (3) :
            if damier[y][x][0] == "B" :
                nbPionBleu += 1
            if damier[y][x][0] == "R" :
                nbPionRouge += 1

    if nbPionBleu == 0 :
        return "R" 
    elif nbPionRouge == 0 :
        return "B" 

    for x in range (3) :
        if damier[0][x][0] == "R" :
            return "R"
        if damier[2][x][0] == "B" :
            return "B"

    for ordonnee in range (3) :
        for abcisse in range (3) :
            if damier[ordonnee][abcisse][0] == "B" :

                if damier[ordonnee+1][abcisse][0] == "_" :
                    spotted += 1


                if abcisse != 0 and damier[ordonnee+1][abcisse-1][0] == "R" :
                    spotted += 1

                if abcisse != 2 and damier[ordonnee+1][abcisse+1][0] == "R" :
                    spotted += 1
            if damier[ordonnee][abcisse][0] == "R" :

                if damier[ordonnee-1][abcisse][0] == "_" :
                    spotted += 1


                if abcisse != 0 and damier[ordonnee-1][abcisse-1][0] == "B" :
                    spotted += 1

                if abcisse != 2 and damier[ordonnee-1][abcisse+1][0] == "B" :
                    spotted += 1
    if spotted == 0 :
        if (round % 2) == 1 :
            return "R"
        else :
            return "B"


    return "nul"


def update_game () :

    global ScoreBleu
    global ScoreRouge
    global round
    global lastWinner
    global game_state
    global selected_move
    global n

    
    #print("selected moves = ", selected_move)

    lastWinner = check_resultat ()

    if lastWinner == "B" :

        

        ScoreBleu += 1
        round = 0
        game_state = "end"

        for e in selected_move :
            p = int(e[0])
            k = int(e[1])
            if pattern[p][1][k]["score"] < 1 :
                pattern[p][1][k]["score"] = 1.0
            else :
                pattern[p][1][k]["score"] += 1.0
        selected_move = []


    elif lastWinner == "R" :


        ScoreRouge += 1
        round = 0

        game_state = "end"

        for e in selected_move :
            p = int(e[0])
            k = int(e[1])
            if n == 2 :
                pattern[p][1][k]["score"] -= 10.0
            elif n == 1 :
                pattern[p][1][k]["score"] -= 3.0
        selected_move = []

    afficher_damier (damier)

    

    lastWinner = ""


def playervsplayer () :
    start_game(2)

def dif1 () :
    global n
    n = 0
    start_game(1)

def dif2 () :
    global n
    n = 1
    start_game(1)

def dif3 () :
    global n
    n = 2
    start_game(1)

def playervsIA () :


    menu.delete(ALL)

    menu.create_image(250, 250,  image=img[7])

    Button(menu,  command = dif1,image = img[11]).place(x = 90, y = 200)
    Button(menu, command = dif2, image = img[12]).place(x = 310, y = 200)
    Button(menu, command = dif3, image = img[13]).place(x = 200, y = 200)

    menu.create_text(142, 140, text = "Le robot\nn'apprend pas\nde ses\nerreurs", font=("Helvetica", 9))
    menu.create_text(257, 140, text = "Le robot\napprend lentement\nde ses\nerreurs", font=("Helvetica", 9))
    menu.create_text(363, 140, text = "Le robot\napprend vite\nde ses\nerreurs", font=("Helvetica", 9))

    

def start_game (nb) :
    
    global canvas
    global gamemode 

    menu.destroy()

    gamemode = nb

    canvas = Canvas(app,height=500, width=500)
    canvas.pack(expand=1,fill= BOTH)
    canvas.bind("<Button-1>", coords_clic)

    Button(canvas, command = end_game, image = img[8]).place(x = 200, y = 420)


    afficher_damier (damier)



def end_game () :
    app.quit
    sys.exit(0)



#créer la fenêtre du jeu
app = Tk()
creation_fenetre(app)

app_path = os.getcwd()


PlaySound(app_path+"/img/latartalabriko.wav", SND_LOOP  | SND_ASYNC)


"""
---------------------------
-Définition des variables -
---------------------------
"""


#on importe les images
img = import_img ()

round = 0
ScoreBleu = 0
ScoreRouge = 0
lastWinner = ""
canvas = None
gamemode = 2
n = 1
game_state = "game"
selected_move = []
default_score = 10
pattern = [

        #1 1A
        [
        [["B_","B_","B_"],
        ["R_","__","__"],
        ["__","R_","R_"]], [{"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 0 , "score" : default_score }, {"y1" : 0 ,"x1" : 1 , "y2" : 1 , "x2" : 1 , "score" : default_score }, {"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 2 , "score" : default_score }]],
        
        #1 1B
        [
        [["B_","B_","B_"],
        ["__","__","R_"],
        ["R_","R_","__"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 0 , "score" : default_score }, {"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 1 , "score" : default_score }, {"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 2 , "score" : default_score }]],
        
         #1 2
        [
        [["B_","B_","B_"],
        ["__","R_","__"],
        ["R_","__","R_"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 0 , "score" : default_score }, {"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 2 , "score" : default_score }, {"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 1 , "score" : default_score },{"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 1 , "score" : default_score }]],

         #2 1A
        [
        [["__","B_","B_"],
        ["B_","R_","R_"],
        ["R_","__","__"]], [{"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 2 , "score" : default_score }, {"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 1, "score" : default_score }]],

         #2 1B
        [
        [["B_","B_","__"],
        ["R_","R_","B_"],
        ["__","__","R_"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 1 , "score" : default_score }, {"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 0, "score" : default_score }]],

         #2 2A
        [
        [["__","B_","B_"],
        ["__","B_","R_"],
        ["R_","__","__"]], [{"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 2 , "score" : default_score }, {"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 0 , "score" : default_score },{"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 1 , "score" : default_score }]],

          #2 2B
        [
        [["B_","B_","__"],
        ["R_","B_","__"],
        ["__","__","R_"]], [{"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 0 , "score" : default_score }, {"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 2 , "score" : default_score }, {"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 1 , "score" : default_score }]],

          #2 3A
        [
        [["B_","B_","__"],
        ["R_","__","R_"],
        ["__","__","R_"]], [{"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 0 , "score" : default_score }, {"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 1 , "score" : default_score }, {"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 2 , "score" : default_score }]],

        #2 3B
        [
        [["__","B_","B_"],
        ["R_","__","R_"],
        ["R_","__","__"]], [{"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 0 , "score" : default_score }, {"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 1 , "score" : default_score }, {"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 2 , "score" : default_score }]],

         #2 4A
        [
        [["B_","__","B_"],
        ["R_","__","__"],
        ["__","__","R_"]], [{"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 2 , "score" : default_score }]],

          #2 4B
        [
        [["B_","__","B_"],
        ["__","__","R_"],
        ["R_","__","__"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 0 , "score" : default_score }]],


         #2 6A
        [
        [["B_","__","B_"],
        ["R_","R_","__"],
        ["__","R_","__"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 1 , "score" : default_score }, {"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 2 , "score" : default_score }, {"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 1 , "score" : default_score }]],

        #2 6B
        [
        [["B_","__","B_"],
        ["__","R_","R_"],
        ["__","R_","__"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 1 , "score" : default_score }, {"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 0 , "score" : default_score }, {"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 1 , "score" : default_score }]],

         #2 7A
        [
        [["__","B_","B_"],
        ["R_","B_","__"],
        ["__","__","R_"]], [{"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 0 , "score" : default_score }, {"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 2 , "score" : default_score },{"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 1 , "score" : default_score }, {"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 2 , "score" : default_score }]],
        
          #2 7B
        [
        [["__","B_","B_"],
        ["R_","B_","__"],
        ["__","__","R_"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 0 , "score" : default_score }, {"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 2 , "score" : default_score }, {"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 1 , "score" : default_score }, {"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 0 , "score" : default_score }]],

        #2 8A
        [
        [["__","B_","B_"],
        ["__","R_","__"],
        ["__","__","R_"]], [{"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 2 , "score" : default_score }, {"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 1 , "score" : default_score }]],

        #2 8B
        [
        [["B_","B_","__"],
        ["__","R_","__"],
        ["R_","__","__"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 0 , "score" : default_score }, {"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 1 , "score" : default_score }]],

         #2 9A
        [
        [["B_","__","B_"],
        ["B_","R_","__"],
        ["__","__","R_"]], [{"y1" : 1 , "x1" : 0 , "y2" : 2 , "x2" : 0 , "score" : default_score }, {"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 1 , "score" : default_score }, {"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 1 , "score" : default_score }, {"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 2 , "score" : default_score }]],

         #2 9B
        [
        [["B_","__","B_"],
        ["__","R_","B_"],
        ["R_","__","__"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 0 , "score" : default_score }, {"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 1 , "score" : default_score }, {"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 1 , "score" : default_score }, {"y1" : 1 , "x1" : 2 , "y2" : 2 , "x2" : 2 , "score" : default_score }]],

         #2 10A
        [
        [["B_","__","B_"],
        ["B_","__","R_"],
        ["__","R_","__"]], [{"y1" : 1 , "x1" : 0 , "y2" : 2 , "x2" : 1 , "score" : default_score }]],

         #2 10B
        [
        [["B_","__","B_"],
        ["R_","__","B_"],
        ["__","R_","__"]], [{"y1" : 1 , "x1" : 2 , "y2" : 2 , "x2" : 1 , "score" : default_score }]],


          #2 11A
        [
        [["__","B_","B_"],
        ["__","R_","__"],
        ["R_","__","__"]], [{"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 1 , "score" : default_score }, {"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 2 , "score" : default_score }]],

           #2 11B
        [
        [["B_","B_","__"],
        ["__","R_","__"],
        ["__","__","R_"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 1 , "score" : default_score }, {"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 0 , "score" : default_score }]],
  
        #3 1A
        [
        [["__","B_","__"],
        ["B_","R_","R_"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 2 , "score" : default_score },	{"y1" : 1 , "x1" : 0 , "y2" : 2 , "x2" : 0 , "score" : default_score }]],

        #3 1B
        [
        [["__","B_","__"],
        ["R_","R_","B_"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 0 , "score" : default_score },	{"y1" : 1 , "x1" : 2 , "y2" : 2 , "x2" : 2 , "score" : default_score }]],


        #3 2A
        [
        [["B_","__","__"],
        ["B_","R_","__"],
        ["__","__","__"]], [{"y1" : 1 , "x1" : 0 , "y2" : 2,  "x2" : 0, "score" : default_score },	{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 1 , "score" : default_score }]],

        #3 2B
        [
        [["__","__","B_"],
        ["__","R_","B_"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 2 , "y2" : 1,  "x2" : 1, "score" : default_score },	{"y1" : 1 , "x1" : 2 , "y2" : 2 , "x2" : 2 , "score" : default_score }]],


        #3 3A
        [
        [["B_","__","__"],
        ["B_","B_","R_"],
        ["__","__","__"]], [{"y1" : 1 , "x1" : 0 , "y2" : 2 , "x2" : 0, "score" : default_score },	{"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 1, "score" : default_score }]],

        #3 3B
        [
        [["__","__","B_"],
        ["R_","B_","B_"],
        ["__","__","__"]], [{"y1" : 1 , "x1" : 2 , "y2" : 2 , "x2" : 2, "score" : default_score },	{"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 1, "score" : default_score }]],

        #3 4A
        [
        [["B_","__","__"],
        ["R_","R_","R_"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 1, "score" : default_score }]],

        #3 4B
        [
        [["__","__","B_"],
        ["R_","R_","R_"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 1, "score" : default_score }]],


#3 6A
        [
        [["__","B_","__"],
        ["R_","B_","__"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 1, "y2" : 1 , "x2" : 0, "score" : default_score },	{"y1" : 1 , "x1" : 1 , "y2" : 2, "x2" : 1, "score" : default_score }]],
  
#3 6B
        [
        [["__","B_","__"],
        ["__","B_","R_"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 2, "score" : default_score },	{"y1" : 1 , "x1" : 1 , "y2" : 2, "x2" : 1, "score" : default_score }]],

#3 7A
        [
        [["__","__","B_"],
        ["B_","R_","__"],
        ["__","__","__"]], [{"y1" : 1 , "x1" : 0 , "y2" : 2 , "x2" : 0, "score" : default_score },	{"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 1, "score" : default_score }]],

#3 7B
        [
        [["B_","__","__"],
        ["__","R_","B_"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 1, "score" : default_score },	{"y1" : 1 , "x1" : 2 , "y2" : 2 , "x2" : 2, "score" : default_score }]],

#3 8A
        [
        [["B_","__","__"],
        ["B_","R_","__"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1, "x2" : 1, "score" : default_score },	{"y1" : 1 , "x1" : 0 , "y2" : 2 , "x2" : 0, "score" : default_score }]],

#3 8B
        [
        [["__","__","B_"],
        ["__","R_","B_"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 2 , "y2" : 1, "x2" : 1, "score" : default_score },	{"y1" : 1 , "x1" : 2 , "y2" : 2 , "x2" : 2, "score" : default_score }]],

#3 9A
        [
        [["__","B_","__"],
        ["R_","R_","B_"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 0, "score" : default_score },	{"y1" : 1 , "x1" : 2 , "y2" : 2 , "x2" : 2, "score" : default_score }]],

#3 9B
        [
        [["__","B_","__"],
        ["B_","R_","R_"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 2, "score" : default_score },	{"y1" : 1 , "x1" : 0 , "y2" : 2 , "x2" : 0, "score" : default_score }]],

#3 10A
        [
        [["__","__", "B_"],
        ["B_","B_","R_"],
        ["__","__","__"]], [{"y1" : 1 , "x1" : 0 , "y2" : 2 , "x2" : 0, "score" : default_score },	{"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 1, "score" : default_score }]],

#3 10B
        [
        [["B_","__","__"],
        ["R_","B_","B_"],
        ["__","__","__"]], [{"y1" : 1 , "x1" : 2 , "y2" : 2 , "x2" : 2, "score" : default_score },	{"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 1, "score" : default_score }]],

        #3 11A
        [
        [["B_","B_","__"],
        ["__","R_","__"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 1, "score" : default_score }]],

         #3 11B
        [
        [["__","B_","B_"],
        ["__","R_","__"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 1, "score" : default_score }]],

         #3 12A
        [
        [["B_","B_","__"],
        ["__","B_","R_"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 0, "score" : default_score }, {"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 1, "score" : default_score }, {"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 2, "score" : default_score }]],

         #3 12B
        [
        [["__","B_","B_"],
        ["R_","B_","__"],
        ["__","__","__"]], [{"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 2, "score" : default_score }, {"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 1, "score" : default_score }, {"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 0, "score" : default_score }]],

         #3 13A
        [
        [["B_","B_","__"],
        ["__","B_","R_"],
        ["R_","__","__"]], [{"y1" : 0 , "x1" : 0 , "y2" : 1 , "x2" : 0, "score" : default_score }, {"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 1, "score" : default_score }, {"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 0, "score" : default_score }, {"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 2, "score" : default_score }]],
        
         #3 13A
        [
        [["__","B_","B_"],
        ["R_","B_","__"],
        ["__","__","R_"]], [{"y1" : 0 , "x1" : 2 , "y2" : 1 , "x2" : 2, "score" : default_score }, {"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 2, "score" : default_score }, {"y1" : 1 , "x1" : 1 , "y2" : 2 , "x2" : 1, "score" : default_score }, {"y1" : 0 , "x1" : 1 , "y2" : 1 , "x2" : 0, "score" : default_score }]],
        
        
        ]












damier = [["B_","B_","B_"],
           ["__","__","__"],
           ["R_","R_","R_"]]

initialisation_damier ()






"""

/////////////////////////////////////////////////////////////////////////////////////////
///                                    PROGRAMME PRINCIPAL                              /
/////////////////////////////////////////////////////////////////////////////////////////

"""






menu = Canvas(app,height=500, width=500)
menu.pack(expand=1,fill= BOTH)
menu.create_image(250, 250,  image=img[7])


Button(menu,  command = playervsplayer,image = img[9]).place(x = 90, y = 200)
Button(menu, command = playervsIA, image = img[10]).place(x = 310, y = 200)

menu.create_text(142, 140, text = "Défiez vos amis,\nou vos ennemis\ndans ce mode de\njeu incroyable !", font=("Helvetica", 9))
menu.create_text(363, 140, text = "Défiez le puissant,\nrobot qui a\nbattu alpha0 !", font=("Helvetica", 9))

app.mainloop()
