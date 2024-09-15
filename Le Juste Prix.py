############################# programme jeu du juste prix ######################################

#importation des bibliothèques necéssaires
from tkinter import *
from random import *
import platform
if platform.system() =="Darwin" :
    from tkmacosx import Button

#fonction pour page quand c'est perdu
def gameover():
    gameover = Tk()
    gameover.title("Game Over")
    gameover.config(bg='purple')
    titre = Label(gameover, text="Game over !", font=("Showcard Gothic", 75), bg='purple', fg='white')
    titre.pack(pady=50)
    titre2 = Label(gameover, text="Tu n'as plus d'essais tu as perdu la partie :(", font=("Showcard Gothic", 15), bg='purple', fg='white')
    titre2.pack(pady=5)
    quitter2 =  Button(gameover, text="Quitter le jeu", font=("Showcard Gothic", 15), bg='red', fg='white', command=(gameover.destroy))
    quitter2.pack(side = BOTTOM, pady = 10)
    retour_acceuil = Button(gameover, text="Retour à l'acceuil", font=("Showcard Gothic", 15), bg='green', fg='white', command=lambda: [gameover.destroy(), acceuil()])
    retour_acceuil.pack(side=BOTTOM)
#fonction pour page acceuil
def acceuil():
    #fenetre de jeu
    fenetre = Tk()
    fenetre.geometry("1000x600")
    fenetre.config(background='purple')
    frame = Frame(fenetre, bg='purple')
    titre = Label(frame, text="Le Juste Prix", font=("Showcard Gothic", 75), bg='purple', fg='white')
    titre.pack(pady=50)
    # page pour choisir la difficulté du jeu
    def choix_difficultés():
        fenetre.destroy()
        fchoix_difficultés = Tk()
        fchoix_difficultés.config(background='purple')
        diff= Label(fchoix_difficultés, bg="purple")
        diff.pack(expand=YES)
        #definitions des variables globals
        global score
        score = 0
        global choix_images
        choix_images = 0
        global max_img
        max_img = 14
        global max_img2
        max_img2 = 4
        global essai
        essai=150
        global essai_facile
        essai_facile = 50
        global essai_moyen
        essai_moyen = 75
        global essai_difficile
        essai_difficile = 100
        # fonction pour ouvrir la fenêtre de jeu
        def fjeu():
            fchoix_difficultés.destroy()
            #création fenetre de jeu
            fjeu = Tk()
            fjeu.config(background='purple')
            #importation des images
            vélo = PhotoImage(file="vélo.gif")
            téléphone = PhotoImage(file="téléphone.gif")
            télé = PhotoImage(file="télé.gif")
            ordinateur = PhotoImage(file="ordinateur.gif")
            enceinte = PhotoImage(file="enceinte.gif")
            multipla = PhotoImage(file="multipla.gif")
            chaussure_nike = PhotoImage(file="chaussure_nike.gif")
            piscine = PhotoImage(file="piscine.gif")
            ps5 = PhotoImage(file="ps5.gif")
            sac = PhotoImage(file="sac a dos.gif")
            rolex =  PhotoImage(file="rolex.gif")
            toilette_or =  PhotoImage(file="or.gif")
            clavier =  PhotoImage(file="clavier.gif")
            bic =  PhotoImage(file="bic.gif")
            bateau =  PhotoImage(file="bateau.gif")
            #création d'une liste contenant toutes les images du jeu et les prix
            total_image = [vélo, téléphone, télé, ordinateur, enceinte, multipla, chaussure_nike, piscine, ps5, sac, rolex, toilette_or, clavier, bic , bateau]
            total_prix = [randint(2000,3000), randint(900,1100), randint(700,900), randint(1300,1500), randint(80,100), randint(9000,11000), randint(100,130), randint(5000,6000), randint(500,700), randint(40,60), randint(20000,30000), randint(100000,150000), randint(30,70), randint(1,5), randint(30000,50000)]
            #mise en place des frame
            frame3 = Frame(fjeu, bg='purple')
            frame3.pack(side=TOP)
            frame2 = Frame(fjeu)
            frame2.pack(expand=YES)
            infobar = Label(frame2, text="Insérez un nombre puis faites entrer", font=("Showcard Gothic", 10), bg='purple', fg='white')
            infobar.pack(side=BOTTOM, fill=X)
            #mise en place de la première image aléatoire dans le canvas
            global max_img
            global prix_img
            a = randint(0,max_img)
            img = total_image[a]
            prix_img = total_prix[a]
            can=Canvas(frame2, bg='white', width=300, height=300)
            can.pack()
            can.create_image(img.width()/2,img.height()/2,image=img)
            can.image = img
            total_image.remove(img)
            total_prix.remove(prix_img)
            max_img -= 1
            #frame 1
            frame1 = Frame(fjeu, bg='purple')
            #bouton quitter
            quitter_jeu =  Button(frame1, text="Retourner à l'acceuil", font=("Showcard Gothic", 15), bg='red', fg='white', command= lambda : [fjeu.destroy(), acceuil()])
            quitter_jeu.pack(pady=10, side=BOTTOM)
            frame1.pack(side=BOTTOM, pady=10)
            #fonction fin de partie
            def fin_de_partie():
                if len(total_image) == 0 :
                    entrer.config(text="Fin de la partie, retourner à l'écran d'acceuil", command=lambda :[fjeu.destroy(), acceuil()])
                    infobar.config(text="Tout les prix ont étaient trouvés !")
                    quitter_jeu.config(text='Quitter', command = fjeu.destroy)
                    return True
            #fonction plus d'essais restant
            def fin_essai():
                global essai
                if essai == 0 :
                    fjeu.destroy()
                    gameover()
                    return True
            #fonction reliée au bouton entrer
            def bouton_entrer(event=None):
                proposition = résultat.get()
                # proposition.isdigit vérifie si les caractères inserés sont bien des nombres, si oui elle renvoie True sinon False
                if proposition.isdigit():
                    nombre_proposition = int(proposition)
                    global essai
                    global score
                    global max_img
                    global prix_img
                    # verifier si le nombre proposition est plus petit que le nombre à trouver
                    if nombre_proposition < prix_img :
                        infobar.config(text="C'est plus !")
                        essai -= 1
                        nb_essai.config(text="Essais restants : "+str(essai))
                    elif nombre_proposition > prix_img :
                        infobar.config(text="C'est moins !")
                        essai -= 1
                        nb_essai.config(text="Essais restants : "+str(essai))
                    elif nombre_proposition == prix_img :
                        fin_de_partie()
                        if fin_de_partie():
                            score += 1
                            point.config(text="Score : "+str(score))
                            return None
                        infobar.config(text="C'est gagné ! Image suivante")
                        score += 1
                        point.config(text="Score : "+str(score))
                        a = randint(0,max_img)
                        img = total_image[a]
                        prix_img = total_prix[a]
                        can.create_image(img.width()/2,img.height()/2,image=img)
                        can.image = img
                        total_image.remove(img)
                        total_prix.remove(prix_img)
                        max_img -= 1
                else :
                    infobar.config(text="Vous devez inserer un nombre !")
                if fin_essai():
                        return None
            #bouton entrer
            entrer = Button(frame1, text="Entrer", font=("Showcard Gothic", 15), bg='green', fg='white', command=bouton_entrer)
            entrer.pack()
            #case pour inserez les nombres
            résultat = Entry(frame2, font=("Showcard Gothic", 10), bg='purple', fg='white')
            résultat.bind('<Return>', bouton_entrer)
            résultat.focus()
            résultat.pack(side=BOTTOM, fill=X)
            #création des inscriptions du score et du nombres d'essais restant
            global score
            point=Label(frame3, text="Score : "+str(score), font=("Showcard Gothic", 25), bg='purple', fg='white')
            point.pack(fill=X, pady=10)
            global essai
            nb_essai= Label(frame3, text="Essais restants : "+str(essai), font=("Showcard Gothic", 15), bg='purple', fg='white')
            nb_essai.pack(fill=X, pady= 10)

        def fjeu_facile ():
            #création fenetre de jeu
            fchoix_difficultés.destroy()
            fjeu_facile = Tk()
            fjeu_facile.config(background='purple')
            # importation des images nécessaires pour le mode facile
            enceinte = PhotoImage(file="enceinte.gif")
            chaussure_nike = PhotoImage(file="chaussure_nike.gif")
            sac = PhotoImage(file="sac a dos.gif")
            clavier =  PhotoImage(file="clavier.gif")
            bic =  PhotoImage(file="bic.gif")
            #création d'une liste contenant toutes les images du jeu et les prix
            facile = [bic, enceinte, chaussure_nike, sac, clavier]
            total_prix_facile = [3, randint(80,100), randint(100,130), randint(40,60), randint(30,70)]
            #mise en place des frame
            frame3 = Frame(fjeu_facile, bg='purple')
            frame3.pack(side=TOP)
            frame2 = Frame(fjeu_facile)
            frame2.pack(expand=YES)
            infobar = Label(frame2, text="Insérez un nombre puis faites entrer", font=("Showcard Gothic", 10), bg='purple', fg='white')
            infobar.pack(side=BOTTOM, fill=X)
            #mise en place de la première image aléatoire dans le canvas
            global max_img2
            global prix_img
            a = randint(0,max_img2)
            img = facile[a]
            prix_img = total_prix_facile[a]
            can=Canvas(frame2, bg='white', width=300, height=300)
            can.pack()
            can.create_image(img.width()/2,img.height()/2,image=img)
            can.image = img
            facile.remove(img)
            total_prix_facile.remove(prix_img)
            max_img2 -= 1
            #frame 1
            frame1 = Frame(fjeu_facile, bg='purple')
            #bouton quitter
            quitter_jeu =  Button(frame1, text="Retourner à l'acceuil", font=("Showcard Gothic", 15), bg='red', fg='white', command= lambda : [fjeu_facile.destroy(), acceuil()])
            quitter_jeu.pack(pady=10, side = BOTTOM)
            frame1.pack(side=BOTTOM, pady=10)
            #fonction fin de partie
            def fin_de_partie_facile():
                if len(facile) == 0 :
                    entrer.config(text="Fin de la partie, retourner à l'écran d'acceuil", command=lambda :[fjeu_facile.destroy(), acceuil()])
                    infobar.config(text="Tout les prix ont étaient trouvés !")
                    quitter_jeu.config(text='Quitter', command = fjeu_facile.destroy)
                    return True
            #fonction plus d'essais restant
            def fin_essai_facile():
                global essai_facile
                if essai_facile == 0 :
                    fjeu_facile.destroy()
                    gameover()
                    return True
            #fonction reliée au bouton entrer
            def bouton_entrer(event=None):
                proposition = résultat.get()
                # proposition.isdigit vérifie si les caractères inserés sont bien des nombres, si oui elle renvoie True sinon False
                if proposition.isdigit():
                    nombre_proposition = int(proposition)
                    global essai_facile
                    global score
                    global max_img2
                    global prix_img
                    # verifier si le nombre proposition est plus petit que le nombre à trouver
                    if nombre_proposition < prix_img :
                        infobar.config(text="C'est plus !")
                        essai_facile -= 1
                        nb_essai.config(text="Essais restants : "+str(essai_facile))
                    elif nombre_proposition > prix_img :
                        infobar.config(text="C'est moins !")
                        essai_facile -= 1
                        nb_essai.config(text="Essais restants : "+str(essai_facile))
                    elif nombre_proposition == prix_img :
                        fin_de_partie_facile()
                        if fin_de_partie_facile():
                            score += 1
                            point.config(text="Score : "+str(score))
                            return None
                        infobar.config(text="C'est gagné ! Image suivante")
                        score += 1
                        point.config(text="Score : "+str(score))
                        a = randint(0,max_img2)
                        img = facile[a]
                        prix_img = total_prix_facile[a]
                        can.create_image(img.width()/2,img.height()/2,image=img)
                        can.image = img
                        facile.remove(img)
                        total_prix_facile.remove(prix_img)
                        max_img2 -= 1
                else :
                    infobar.config(text="Vous devez inserer un nombre !")
                if fin_essai_facile():
                        return None
            #bouton entrer
            entrer = Button(frame1, text="Entrer", font=("Showcard Gothic", 15), bg='green', fg='white', command=bouton_entrer)
            entrer.pack()
            #case pour inserez les nombres
            résultat = Entry(frame2, font=("Showcard Gothic", 10), bg='purple', fg='white')
            résultat.bind('<Return>', bouton_entrer)
            résultat.focus()
            résultat.pack(side=BOTTOM, fill=X)
            #création des inscriptions du score et du nombres d'essais restant
            global score
            point=Label(frame3, text="Score : "+str(score), font=("Showcard Gothic", 25), bg='purple', fg='white')
            point.pack(fill=X, pady=10)
            global essai_facile
            nb_essai= Label(frame3, text="Essais restants : "+str(essai_facile), font=("Showcard Gothic", 15), bg='purple', fg='white')
            nb_essai.pack(fill=X, pady= 10)

        def fjeu_moyen ():
            #création fenetre de jeu
            fchoix_difficultés.destroy()
            fjeu_moyen = Tk()
            fjeu_moyen.config(background='purple')
            # importation des images nécessaires pour le mode facile
            vélo = PhotoImage(file="vélo.gif")
            téléphone = PhotoImage(file="téléphone.gif")
            télé = PhotoImage(file="télé.gif")
            ordinateur = PhotoImage(file="ordinateur.gif")
            ps5 = PhotoImage(file="ps5.gif")
            #création d'une liste contenant toutes les images du jeu et les prix
            moyen = [vélo, télé, téléphone, ps5, ordinateur]
            total_prix_moyen = [randint(2000,3000), randint(700,900), randint(900,1100), randint(500,700), randint(1300,1500)]
            #mise en place des frame
            frame3 = Frame(fjeu_moyen, bg='purple')
            frame3.pack(side=TOP)
            frame2 = Frame(fjeu_moyen)
            frame2.pack(expand=YES)
            infobar = Label(frame2, text="Insérez un nombre puis faites entrer", font=("Showcard Gothic", 10), bg='purple', fg='white')
            infobar.pack(side=BOTTOM, fill=X)
            #mise en place de la première image aléatoire dans le canvas
            global max_img2
            global prix_img
            a = randint(0,max_img2)
            img = moyen[a]
            prix_img = total_prix_moyen[a]
            can=Canvas(frame2, bg='white', width=300, height=300)
            can.pack()
            can.create_image(img.width()/2,img.height()/2,image=img)
            can.image = img
            moyen.remove(img)
            total_prix_moyen.remove(prix_img)
            max_img2 -= 1
            #frame 1
            frame1 = Frame(fjeu_moyen, bg='purple')
            #bouton quitter
            quitter_jeu =  Button(frame1, text="Retourner à l'acceuil", font=("Showcard Gothic", 15), bg='red', fg='white', command= lambda : [fjeu_moyen.destroy(), acceuil()])
            quitter_jeu.pack(pady=10, side = BOTTOM)
            frame1.pack(side=BOTTOM, pady=10)
            #fonction fin de partie
            def fin_de_partie_moyen():
                if len(moyen) == 0 :
                    entrer.config(text="Fin de la partie, retourner à l'écran d'acceuil", command=lambda :[fjeu_moyen.destroy(), acceuil()])
                    infobar.config(text="Tout les prix ont étaient trouvés !")
                    quitter_jeu.config(text='Quitter', command = fjeu_moyen.destroy)
                    return True
            #fonction plus d'essais restant
            def fin_essai_moyen():
                global essai_moyen
                if essai_moyen == 0 :
                    fjeu_moyen.destroy()
                    gameover()
                    return True
            #fonction reliée au bouton entrer
            def bouton_entrer(event=None):
                proposition = résultat.get()
                # proposition.isdigit vérifie si les caractères inserés sont bien des nombres, si oui elle renvoie True sinon False
                if proposition.isdigit():
                    nombre_proposition = int(proposition)
                    global essai_moyen
                    global score
                    global max_img2
                    global prix_img
                    # verifier si le nombre proposition est plus petit que le nombre à trouver
                    if nombre_proposition < prix_img :
                        infobar.config(text="C'est plus !")
                        essai_moyen -= 1
                        nb_essai.config(text="Essais restants : "+str(essai_moyen))
                    elif nombre_proposition > prix_img :
                        infobar.config(text="C'est moins !")
                        essai_moyen -= 1
                        nb_essai.config(text="Essais restants : "+str(essai_moyen))
                    elif nombre_proposition == prix_img :
                        fin_de_partie_moyen()
                        if fin_de_partie_moyen():
                            score += 1
                            point.config(text="Score : "+str(score))
                            return None
                        infobar.config(text="C'est gagné ! Image suivante")
                        score += 1
                        point.config(text="Score : "+str(score))
                        a = randint(0,max_img2)
                        img = moyen[a]
                        prix_img = total_prix_moyen[a]
                        can.create_image(img.width()/2,img.height()/2,image=img)
                        can.image = img
                        moyen.remove(img)
                        total_prix_moyen.remove(prix_img)
                        max_img2 -= 1
                else :
                    infobar.config(text="Vous devez inserer un nombre !")
                if fin_essai_moyen():
                        return None
            #bouton entrer
            entrer = Button(frame1, text="Entrer", font=("Showcard Gothic", 15), bg='green', fg='white', command=bouton_entrer)
            entrer.pack()
            #case pour inserez les nombres
            résultat = Entry(frame2, font=("Showcard Gothic", 10), bg='purple', fg='white')
            résultat.bind('<Return>', bouton_entrer)
            résultat.focus()
            résultat.pack(side=BOTTOM, fill=X)
            #création des inscriptions du score et du nombres d'essais restant
            global score
            point=Label(frame3, text="Score : "+str(score), font=("Showcard Gothic", 25), bg='purple', fg='white')
            point.pack(fill=X, pady=10)
            global essai_moyen
            nb_essai= Label(frame3, text="Essais restants : "+str(essai_moyen), font=("Showcard Gothic", 15), bg='purple', fg='white')
            nb_essai.pack(fill=X, pady= 10)

        def fjeu_difficile ():
            #création fenetre de jeu
            fchoix_difficultés.destroy()
            fjeu_difficile = Tk()
            fjeu_difficile.config(background='purple')
            # importation des images nécessaires pour le mode facile
            multipla = PhotoImage(file="multipla.gif")
            piscine = PhotoImage(file="piscine.gif")
            rolex =  PhotoImage(file="rolex.gif")
            toilette_or =  PhotoImage(file="or.gif")
            bateau =  PhotoImage(file="bateau.gif")
            #création d'une liste contenant toutes les images du jeu et les prix
            difficile = [rolex, toilette_or, bateau, piscine, multipla]
            total_prix_difficile = [randint(20000,30000), randint(100000,150000), randint(30000,50000), randint(5000,6000), randint(9000,11000)]
            #mise en place des frame
            frame3 = Frame(fjeu_difficile, bg='purple')
            frame3.pack(side=TOP)
            frame2 = Frame(fjeu_difficile)
            frame2.pack(expand=YES)
            infobar = Label(frame2, text="Insérez un nombre puis faites entrer", font=("Showcard Gothic", 10), bg='purple', fg='white')
            infobar.pack(side=BOTTOM, fill=X)
            #mise en place de la première image aléatoire dans le canvas
            global max_img2
            global prix_img
            a = randint(0,max_img2)
            img = difficile[a]
            prix_img = total_prix_difficile[a]
            can=Canvas(frame2, bg='white', width=300, height=300)
            can.pack()
            can.create_image(img.width()/2,img.height()/2,image=img)
            can.image = img
            difficile.remove(img)
            total_prix_difficile.remove(prix_img)
            max_img2 -= 1
            # frame 1
            frame1 = Frame(fjeu_difficile, bg='purple')
            #bouton quitter
            quitter_jeu =  Button(frame1, text="Retourner à l'acceuil", font=("Showcard Gothic", 15), bg='red', fg='white', command= lambda : [fjeu_difficile.destroy(), acceuil()])
            quitter_jeu.pack(pady=10, side = BOTTOM)
            frame1.pack(side=BOTTOM, pady=10)
            #fonction fin de partie
            def fin_de_partie_difficile():
                if len(difficile) == 0 :
                    entrer.config(text="Fin de la partie, retourner à l'écran d'acceuil", command=lambda :[fjeu_difficile.destroy(), acceuil()])
                    infobar.config(text="Tout les prix ont étaient trouvés !")
                    quitter_jeu.config(text='Quitter', command = fjeu_difficile.destroy)
                    return True
            #fonction plus d'essais restant
            def fin_essai_difficile():
                global essai_difficile
                if essai_difficile == 0 :
                    fjeu_difficile.destroy()
                    gameover()
                    return True
            #fonction reliée au bouton entrer
            def bouton_entrer(event=None):
                proposition = résultat.get()
                # proposition.isdigit vérifie si les caractères inserés sont bien des nombres, si oui elle renvoie True sinon False
                if proposition.isdigit():
                    nombre_proposition = int(proposition)
                    global essai_difficile
                    global score
                    global max_img2
                    global prix_img
                    # verifier si le nombre proposition est plus petit que le nombre à trouver
                    if nombre_proposition < prix_img :
                        infobar.config(text="C'est plus !")
                        essai_difficile -= 1
                        nb_essai.config(text="Essais restants : "+str(essai_difficile))
                    elif nombre_proposition > prix_img :
                        infobar.config(text="C'est moins !")
                        essai_difficile -= 1
                        nb_essai.config(text="Essais restants : "+str(essai_difficile))
                    elif nombre_proposition == prix_img :
                        fin_de_partie_difficile()
                        if fin_de_partie_difficile():
                            score += 1
                            point.config(text="Score : "+str(score))
                            return None
                        infobar.config(text="C'est gagné ! Image suivante")
                        score += 1
                        point.config(text="Score : "+str(score))
                        a = randint(0,max_img2)
                        img = difficile[a]
                        prix_img = total_prix_difficile[a]
                        can.create_image(img.width()/2,img.height()/2,image=img)
                        can.image = img
                        difficile.remove(img)
                        total_prix_difficile.remove(prix_img)
                        max_img2 -= 1
                else :
                    infobar.config(text="Vous devez inserer un nombre !")
                if fin_essai_difficile():
                        return None
            #bouton entrer
            entrer = Button(frame1, text="Entrer", font=("Showcard Gothic", 15), bg='green', fg='white', command=bouton_entrer)
            entrer.pack()
            #case pour inserez les nombres
            résultat = Entry(frame2, font=("Showcard Gothic", 10), bg='purple', fg='white')
            résultat.bind('<Return>', bouton_entrer)
            résultat.focus()
            résultat.pack(side=BOTTOM, fill=X)
            #création des inscriptions du score et du nombres d'essais restant
            global score
            point=Label(frame3, text="Score : "+str(score), font=("Showcard Gothic", 25), bg='purple', fg='white')
            point.pack(fill=X, pady=10)
            global essai_difficile
            nb_essai= Label(frame3, text="Essais restants : "+str(essai_difficile), font=("Showcard Gothic", 15), bg='purple', fg='white')
            nb_essai.pack(fill=X, pady= 10)
        #boutons de la fenetre choix des diffcicultés
        difficult = Label(diff, text='Choix de la difficultée :', font=("Showcard Gothic", 65), bg='purple', fg='white')
        difficult.pack(pady=50)
        bouton_facile = Button(diff, text="Facile", font=("Showcard Gothic", 20), bg='green', fg='white', command=fjeu_facile)
        bouton_facile.pack(pady=5)
        bouton_moyen = Button(diff, text="Moyen", font=("Showcard Gothic", 20), bg='orange', fg='white', command= fjeu_moyen)
        bouton_moyen.pack(pady=5)
        bouton_difficile = Button(diff, text="Difficile", font=("Showcard Gothic", 20), bg='grey', fg='white', command= fjeu_difficile)
        bouton_difficile.pack(pady=5)
        bouton_arcade = Button(diff, text="Arcade", font=("Showcard Gothic", 20), bg='black', fg='white', command=fjeu)
        bouton_arcade.pack(pady=5)
        bouton_retour = Button(text="Retour", font=("Showcard Gothic", 13), bg='red', fg='white', command= lambda : [fchoix_difficultés.destroy(), acceuil()])
        bouton_retour.pack(padx=10, pady=10, side=RIGHT)
    #fonction pour afficher les règles
    def regles():
        #commande qui crée une sous page de la page d'acceuil
        fregle = Tk()
        fregle.title("Le Juste Prix - Règles du Jeu")
        fregle.geometry("700x400")
        fregle.config(bg='purple')
        fregle.maxsize(700, 400)
        fregle.minsize(700, 400)
        fregle.iconbitmap("regle.ico")
        #ajout de plusieurs labels les un en dessous des autres pour la présentation des règles
        label_regle1 = Label(fregle, text = "Règles du jeu :", font=("Showcard Gothic", 35),bg = 'purple', fg='white')
        label_regle1.place(x=180, y=0)
        label_regle2 = Label(fregle, text = "- Il faut trouver le Juste Prix des objets qui vont apparaître.", font=("Showcard Gothic", 12),bg = 'purple', fg='white')
        label_regle2.place(x=25, y=100)
        label_regle3 = Label(fregle, text = "- Pour cela vous avez un total d'essais à ne pas dépasser.", font=("Showcard Gothic", 12),bg = 'purple', fg='white')
        label_regle3.place(x=25, y=150)
        label_regle4 = Label(fregle, text = "- Plusieurs difficultés sont à choisir : Facile, Moyen, Difficile.", font=("Showcard Gothic", 12),bg = 'purple', fg='white')
        label_regle4.place(x=25, y=200)
        label_regle5 = Label(fregle, text = "- Un autre mode de jeu existe : Arcade (regroupant tout les objets du jeu).", font=("Showcard Gothic", 12),bg = 'purple', fg='white')
        label_regle5.place(x=25, y=250)
        label_regle7 = Label(fregle, text = "- Facile (50 essais), Moyen (75 essais), Difficile (100 essais), Arcade (150 essais).", font=("Showcard Gothic", 12),bg = 'purple', fg='white')
        label_regle7.place(x=25, y=300)
        quitter =  Button(fregle, text="Fermer", font=("Showcard Gothic", 10), bg='red', fg='white', command=(fregle.destroy))
        quitter.pack(side=BOTTOM, pady=5)
    #boutons de la page d'accueil
    jouer =  Button(frame, text="Jouer", font=("Showcard Gothic", 30), bg="green", fg="white", command= choix_difficultés)
    jouer.pack()
    regles_page =  Button(frame, text="Règles du jeu", font=("Showcard Gothic", 15), bg='grey', fg='white', command=regles)
    regles_page.pack(pady=25)
    quitter =  Button(frame, text="Quitter", font=("Showcard Gothic", 15), bg='red', fg='white', command=(fenetre.destroy))
    quitter.pack()
    frame.pack(expand=YES)
    fenetre.mainloop()

#executer la fonction acceuil des le debut quand le programme se lance
acceuil()
