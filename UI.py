from tkinter import *
from tkinter import messagebox
from SpamDetection import predict_and_save  # Importer la fonction corrigée

# Configuration principale de la fenêtre
root = Tk()
root.title("Spam Detection App")
root.geometry("500x300")
root.configure(bg="#1e1e2e")  # Fond sombre
root.resizable(False, False)

# Styles de police
font_label = ("Arial", 12, "bold")
font_entry = ("Arial", 12)
font_button = ("Arial", 11, "bold")

# Cadre principal
frame = Frame(root, bg="#2a2a40", padx=20, pady=20, relief=GROOVE, bd=2)
frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

# Titre
title_label = Label(frame, text="📩 Spam Detection App 📩", font=("Arial", 15, "bold"), bg="#2a2a40", fg="#ffcc00")
title_label.pack(pady=5)

# Label pour l'entrée utilisateur
Label(frame, text="📩 Entrez votre message :", font=font_label, bg="#2a2a40", fg="#ff66b2").pack(anchor="w")

# Zone de saisie
entry = Entry(frame, width=50, font=font_entry, bd=2, relief=SOLID, bg="#3b3b58", fg="white", insertbackground="white")
entry.pack(pady=5, ipady=5)

# Fonction de prédiction
def on_predict():
    message = entry.get().strip()
    if message:
        try:
            result = predict_and_save(message)  # Appelle la fonction de prédiction
            messagebox.showinfo("Résultat de la prédiction", f"Le message est : {result}")
        except Exception as e:
            messagebox.showerror("Erreur", f"❌ Une erreur est survenue : {e}")
    else:
        messagebox.showwarning("Erreur de saisie", "⚠️ Veuillez entrer un message.")

# Effets visuels pour le bouton
def on_enter(e):
    btn_predict.config(bg="#ff66b2", fg="white")

def on_leave(e):
    btn_predict.config(bg="#00bfff", fg="white")

# Bouton de prédiction
btn_predict = Button(frame, text="🔍 Prédire", command=on_predict, font=font_button, bg="#00bfff", fg="white", bd=3, relief=RAISED, padx=10, pady=5)
btn_predict.pack(pady=15)
btn_predict.bind("<Enter>", on_enter)
btn_predict.bind("<Leave>", on_leave)

# Lancement de l'application
root.mainloop()
