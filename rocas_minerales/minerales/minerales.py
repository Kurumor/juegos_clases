#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

# Datos de las rocas (nombres e imágenes)
minerals = [
    {"name": "Apatito", "image": "images/apatito.jpg"},
    {"name": "Biotita", "image": "images/biotita.jpg"},
    {"name": "Calcita", "image": "images/calcita.jpg"},
    {"name": "Corindon", "image": "images/corindon.jpg"},
    {"name": "Cuarzo", "image": "images/cuarzo.jpg"},
    {"name": "Diamante", "image": "images/diamante.jpg"},
    {"name": "Feldespato", "image": "images/feldespato.jpg"},
    {"name": "Fluorita", "image": "images/fluorita.jpg"},
    {"name": "Granito", "image": "images/granito.jpg"},
    {"name": "Halita", "image": "images/halita.jpg"},
    {"name": "Moscovita", "image": "images/moscovita.jpg"},
    {"name": "Olivino", "image": "images/olivino.jpg"},
    {"name": "Ortosa", "image": "images/ortosa.jpg"},
    {"name": "Talco", "image": "images/talco.jpg"},
    {"name": "Topacio", "image": "images/topacio.jpg"},
    {"name": "Yeso", "image": "images/yeso.jpg"}
]

# Inicializa el puntaje y el contador de preguntas
score = 0
question_count = 0
total_questions = 16

# Lista de índices para hacer un seguimiento de las imágenes mostradas en la partida actual
image_indices = []

# Función para mostrar una nueva pregunta
def new_question():
    global question_count
    question_count += 1

    if question_count > total_questions:
        messagebox.showinfo("Fin del Juego", f"Has terminado el juego.\nPuntaje final: {score} de {total_questions}")
        root.destroy()
        return
    
    global current_mineral
    if not image_indices:
        image_indices.extend(range(len(minerals)))  # Si la lista está vacía, llenarla con todos los índices
        random.shuffle(image_indices)
    
    index = image_indices.pop()  # Seleccionar y eliminar un índice de la lista
    current_mineral = minerals[index]
    
    # Cargar y mostrar la imagen
    image = Image.open(current_mineral["image"])
    image = image.resize((300, 300), Image.LANCZOS)  # Aumentar tamaño a 300x300
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo
    
    # Crear opciones de respuesta
    options = [current_mineral["name"]]
    while len(options) < 3:
        option_index = random.randint(0, len(minerals) - 1)
        option = minerals[option_index]["name"]
        if option not in options:
            options.append(option)
    random.shuffle(options)
    
    # Actualizar los botones de respuesta
    for i in range(3):
        answer_buttons[i].config(text=options[i], command=lambda opt=options[i]: check_answer(opt))

# Función para verificar la respuesta
def check_answer(selected_option):
    global score
    if selected_option == current_mineral["name"]:
        score += 1
        messagebox.showinfo("Correcto", "¡Respuesta correcta!")
    else:
        messagebox.showerror("Incorrecto", f"Respuesta incorrecta. Era {current_mineral['name']}.")

    # Actualizar la etiqueta de puntaje
    score_label.config(text=f"Puntaje: {score}")
    new_question()

# Crear la ventana principal
root = tk.Tk()
root.title("Juego de Minerales")

# Crear el widget de imagen
image_label = tk.Label(root)
image_label.pack(pady=20)

# Crear la etiqueta de puntaje
score_label = tk.Label(root, text=f"Puntaje: {score}", font=("Arial", 16))
score_label.pack(pady=10)

# Crear botones de respuesta
answer_buttons = [tk.Button(root, font=("Arial", 16), height=2, width=20) for _ in range(3)]
for button in answer_buttons:
    button.pack(pady=10)  # Aumentar el padding

# Iniciar el juego con una nueva pregunta
new_question()

# Iniciar el bucle principal de la aplicación
root.mainloop()

