import tkinter as tk
from tkinter import PhotoImage
from helpers import obtenir_message
import sys, os

def montrer_message():
    message = obtenir_message()
    message_label.config(text=message)

app = tk.Tk()
app.title("Démo PyInstaller")

# Déterminez si l'application est "gelée" (compilée)
if getattr(sys, 'frozen', False):
    # Le chemin d'accès lors de l'exécution de l'exécutable
    base_path = sys._MEIPASS
else:
    # Le chemin d'accès lors de l'exécution du script
    base_path = os.path.dirname(__file__)

# Chemin vers le dossier d'images
images_folder = os.path.join(base_path, "Images")

# Utilisation d'une image spécifique
image_path = os.path.join(images_folder, "logo_yt.png")
img = PhotoImage(file=image_path)
img_label = tk.Label(app, image=img)
img_label.pack()

# Ajout d'un bouton qui affiche un message lorsqu'il est cliqué
btn = tk.Button(app, text="Afficher Message", command=montrer_message)
btn.pack()

# Label pour afficher le message
message_label = tk.Label(app, text="")
message_label.pack()

app.mainloop()