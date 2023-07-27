import random
import tkinter as tk
from PIL import Image, ImageTk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Pierre - Papier - Ciseaux")
fenetre.configure(bg="#ffc8dd")
fenetre.geometry("1024x768")

# Fonction qui choisi au hasard pour l'ordinateur
def computer_choice():
    choices = ["Pierre", "Papier", "Ciseaux"]
    return random.choice(choices)

# Fonction qui permet de lancer le jeu
def play(user_choice):
    nbDeCoups.set(nbDeCoups.get() + 1) #Ajoute 1 au nombre de coups
    computer = computer_choice() #Fait appel à la fonction qui choisi aléatoirement pour le PC

    # Logique pour déterminer le gagnant
    if user_choice == computer:
        result_var.set("Egalité !")
    elif (
        (user_choice == "Pierre" and computer == "Ciseaux") 
        or (user_choice == "Papier" and computer == "Pierre")
        or (user_choice == "Ciseaux" and computer == "Papier")
        ): 
        result_var.set("Vous avez gagné !")
        player_score_var.set(player_score_var.get() + 1)
    else:
        result_var.set("Vous avez perdu !")
        computer_score_var.set(computer_score_var.get() + 1)

    # Charger les images correspondantes aux choix
    user_img_label.config(image=get_image(user_choice))
    computer_img_label.config(image=get_image(computer))

    # Ajouter les choix à l'historique (du plus récent au plus ancien)
    history_listbox.insert(0, f"Vous : {user_choice} - Ordinateur : {computer}")

    verify_victory()

# fonction qui permet de savoir si l'utilisateur peut continuer à jouer
def verify_victory():
    # Test si le nombre de coups est > 10
    if nbDeCoups.get() >= 10:
        # Comparer les scores pour déterminer le gagnant
        if player_score_var.get() > computer_score_var.get():
            result_var.set("Félicitations, vous avez gagné la partie !")
        elif player_score_var.get() < computer_score_var.get():
            result_var.set("Dommage, l'ordinateur a gagné")
        else: 
            result_var.set("Match nul !")

        #Désactiver les boutons pour empêcher de jouer
        rock_button.config(state=tk.DISABLED)
        paper_button.config(state=tk.DISABLED)
        scissors_button.config(state=tk.DISABLED)

        bouton_re.place(x=100, y=450)


# fonction qui permet de réinitialiser le jeu

def reinit():
    nbDeCoups.set(0)
    computer_score_var.set(0)
    player_score_var.set(0)
    result_var.set(0)
    history_listbox.delete(0, tk.END)
    user_img_label.config(image=empty_img)
    computer_img_label.config(image=empty_img)
    # Réactiver les boutons
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)
    bouton_re.place_forget()
def quit():
    fenetre.destroy()

# Afficher une image en fonction du choix
def get_image(choice):
    if choice == "Pierre":
        return rock_img
    elif choice == "Papier":
        return paper_img
    else:
        return scissors_img

# Définition des variables
result_var = tk.StringVar()
player_score_var = tk.IntVar()
computer_score_var = tk.IntVar()
nbDeCoups = tk.IntVar(value=0) #Permet d'arrêter le jeu après X coups
    
# Charger les images
rock_img = ImageTk.PhotoImage(Image.open("./jeu/pierre.gif"))
paper_img = ImageTk.PhotoImage(Image.open("./jeu/papier.gif"))
scissors_img = ImageTk.PhotoImage(Image.open("./jeu/Ciseaux.gif"))
empty_img = ImageTk.PhotoImage(Image.new("RGBA", (0, 0), (0, 0, 0, 0))) #Création image vide en taille 0x0 et totalement transparente

# Création des widget avec les images
user_label = tk.Label(fenetre, text="Choisissez : ", bg="#cdb4db", fg="white", font=("Helvetica", 16, "bold"))
user_label.pack(pady=10)

rock_button = tk.Button(fenetre, image=rock_img, command=lambda : play("Pierre"))
rock_button.place(x=10, y=10)
              
paper_button = tk.Button(fenetre, image=paper_img, command=lambda : play("Papier"))
paper_button.place(x=10, y=150)

scissors_button = tk.Button(fenetre, image=scissors_img, command=lambda : play("Ciseaux"))
scissors_button.place(x=10, y=290)

# Etiqueetes pour afficher les images jouées
user_img_label = tk.Label(fenetre, image=None, bg="#ffc8dd") # Pas d'image de départ
user_img_label.place(x=200, y=50)

computer_img_label = tk.Label(fenetre, image=None, bg="#ffc8dd") # Pas d'image de départ
computer_img_label.place(x=700, y=50)

result_label = tk.Label(fenetre, textvariable=result_var, bg="#ffc8dd", fg="white", font=("Helvetica", 16, "bold"))
result_label.pack(pady=20)

# Création d'une frame pour les score
score_frame = tk.Frame(fenetre)
score_frame.configure(bg="#a2d2ff")
score_frame.pack()

player_score_label = tk.Label(score_frame, text="Score J1 :", bg="#a2d2ff", fg="white", font=("Helvetica", 14))
player_score_label.pack(side=tk.LEFT, padx=10)

player_score_display = tk.Label(score_frame, textvariable=player_score_var, bg="#a2d2ff", fg="white", font=("Helvetica", 14))
player_score_display.pack(side=tk.LEFT, padx=10)

computer_score_label = tk.Label(score_frame, text="Score Ordinateur :", bg="#a2d2ff", fg="white", font=("Helvetica", 14))
computer_score_label.pack(side=tk.LEFT, padx=10)

computer_score_display = tk.Label(score_frame, textvariable=computer_score_var, bg="#a2d2ff", fg="white", font=("Helvetica", 14))
computer_score_display.pack(side=tk.LEFT, padx=10)

# Gestion de l'historique et de l'affichage
history_label = tk.Label(fenetre, text="Historique des coups : ", bg="#cdb4db", fg="white", font=("Helvetica", 14))
history_label.pack(pady=10)

history_listbox = tk.Listbox(fenetre, width=50, height=15)
history_listbox.configure(bg="#ffc8dd", fg="white", font=("Helvetica", 14), bd=0)
history_listbox.pack()

# Ajout d'un bouton réinitialiser

bouton_re = tk.Button(fenetre,text='Recommencer',command=lambda:reinit())
bouton_re.configure(bg="#cdb4db", fg="white", height=2, width=12)
bouton_quit = tk.Button(fenetre, text="Quitter", command=lambda:quit())
bouton_quit.configure(bg="#cdb4db", fg="white")
bouton_quit.place(x=100, y=500)
fenetre.mainloop()