#!/usr/bin/python3

import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Nombres de las rocas
rock_names = [
    "Obsidiana", "Lava", "Granito", "Sienita", "Pumita", 
    "Gabro", "Riolita", "Peridotita", "Basalto", "Pegmatita", "Pórfido" 
]

# Respuestas correctas para cada roca (en orden de las flechas)
correct_answers = [
    "Obsidiana", "Lava", "Granito", "Sienita", "Pumita", 
    "Gabro", "Riolita", "Peridotita", "Basalto", "Pegmatita", "Pórfido" 
]

# Crear la ventana principal
root = tk.Tk()
root.title("Identificación de Rocas")

# Crear un marco principal
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

# Cargar la imagen
image_path = "images/rocas_con_numeros.jpg"
image = Image.open(image_path)
image = image.resize((600, 600), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Crear un widget para la imagen
image_label = tk.Label(main_frame, image=photo)
image_label.pack(side=tk.LEFT)

# Crear un marco para las entradas y la lista de nombres
right_frame = tk.Frame(main_frame)
right_frame.pack(side=tk.LEFT, padx=10)

# Crear etiquetas y entradas para cada roca
entries = []
for i in range(11):
    frame = tk.Frame(right_frame)
    frame.pack(padx=10, pady=5)

    label = tk.Label(frame, text=f"Roca {i + 1}")
    label.pack(side=tk.LEFT)

    entry = tk.Entry(frame)
    entry.pack(side=tk.LEFT)
    entries.append(entry)


# Función para verificar las respuestas
def check_answers():
    correct = 0
    for i, entry in enumerate(entries):
        if entry.get().strip().lower() == correct_answers[i].lower():
            correct += 1
    messagebox.showinfo("Resultados", f"Has identificado correctamente {correct} de 11 rocas.")

# Botón para verificar respuestas
check_button = tk.Button(right_frame, text="Verificar Respuestas", command=check_answers)
check_button.pack(pady=10)

# Lista de nombres de rocas disponibles para copiar
names_label = tk.Label(right_frame, text="Nombres de rocas disponibles:")
names_label.pack(pady=5)
names_list = tk.Listbox(right_frame)
names_list.pack()
random.shuffle(rock_names)
for name in rock_names:
    names_list.insert(tk.END, name)

# Ejecutar la aplicación
root.mainloop()

