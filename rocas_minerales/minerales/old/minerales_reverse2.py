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

# Función para mostrar una nueva pregunta
def new_question():
    global question_count
    question_count += 1

    if question_count > total_questions:
        messagebox.showinfo("Fin del Juego", f"Has terminado el juego.\nPuntaje final: {score} de {total_questions}")
        root.destroy()
        return
    
    global current_mineral
    current_mineral = random.choice(minerals)
    
    # Mostrar el nombre de la roca en la etiqueta
    question_label.config(text=f"¿Qué imagen corresponde a {current_mineral['name']}?")
    
    # Seleccionar la imagen correcta y otras dos opciones aleatorias
    correct_image = current_mineral['image']
    incorrect_images = [mineral['image'] for mineral in random.sample(minerals, 2) if mineral['name'] != current_mineral['name']]
    options = [correct_image] + incorrect_images
    random.shuffle(options)
    
    # Actualizar las imágenes de los botones de respuesta
    for i in range(3):
        image = Image.open(options[i])
        image = image.resize((200, 200), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        answer_buttons[i].config(image=photo, command=lambda opt=options[i]: check_answer(opt))
        answer_buttons[i].image = photo  # Conservar una referencia a la imagen para evitar que se borre

# Función para verificar la respuesta
def check_answer(selected_image):
    global score
    if selected_image == current_mineral['image']:
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

# Crear la etiqueta de pregunta
question_label = tk.Label(root, text="", font=("Arial", 16))
question_label.pack(pady=20)

# Crear botones de respuesta
answer_buttons = [tk.Button(root, font=("Arial", 12), height=2, width=20) for _ in range(3)]
for button in answer_buttons:
    button.pack(pady=10)  # Aumentar el padding

# Crear la etiqueta de puntaje
score_label = tk.Label(root, text=f"Puntaje: {score}", font=("Arial", 16))
score_label.pack(pady=10)

# Iniciar el juego con una nueva pregunta
new_question()

# Iniciar el bucle principal de la aplicación
root.mainloop()

