#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
import random

# Lista de preguntas
preguntas = [
    {
        "pregunta": "¿Cuáles eran los límites de Egipto?",
        "opciones": [
            "norte: mar Mediterráneo, este: mar negro, sur: pueblo de nubia, oeste: desierto de sahara",
            "este: mar negro, sur: pueblo de nubia, norte: mar Mediterráneo, oeste: desierto de sahara",
            "oeste: desierto de sahara, este: mar rojo, sur: pueblo de nubia, norte: mar Mediterráneo",
            "norte: Mar Mediterráneo, este: desierto de sahara, sur: pueblo de nubia, oeste: mar rojo"
        ],
        "respuesta_correcta": "oeste: desierto de sahara, este: mar rojo, sur: pueblo de nubia, norte: mar Mediterráneo"
    },
    {
        "pregunta": "¿En qué dos zonas se delimitaba Egipto?",
        "opciones": [
            "Egipto Bajo o Delta, Egipto Alto o Valle",
            "Bajo Egipto o Valle, Alto Egipto o Delta",
            "Egipto Bajo o Valle, Egipto Alto o Delta",
            "Bajo Egipto o Delta, Alto Egipto o Valle"
        ],
        "respuesta_correcta": "Bajo Egipto o Delta, Alto Egipto o Valle"
    },
    # ... (Más preguntas)
]

class JuegoPreguntas:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Preguntas sobre Egipto")
        self.puntaje = 0
        self.indice_pregunta = 0
        random.shuffle(preguntas)
        self.preguntas = preguntas

        self.pregunta_var = tk.StringVar()
        self.opcion_var = tk.StringVar()
        self.resultado_var = tk.StringVar()

        self.pregunta_label = tk.Label(root, textvariable=self.pregunta_var, wraplength=400)
        self.pregunta_label.pack(pady=20)

        self.opciones = []
        for i in range(4):
            radio_button = tk.Radiobutton(root, text="", variable=self.opcion_var, value="", wraplength=400)
            radio_button.pack(anchor='w')
            self.opciones.append(radio_button)

        self.resultado_label = tk.Label(root, textvariable=self.resultado_var, wraplength=400)
        self.resultado_label.pack(pady=10)

        self.siguiente_btn = tk.Button(root, text="Siguiente", command=self.siguiente_pregunta)
        self.siguiente_btn.pack(pady=20)

        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        pregunta = self.preguntas[self.indice_pregunta]
        self.pregunta_var.set(f"Pregunta {self.indice_pregunta + 1} de {len(self.preguntas)}: {pregunta['pregunta']}")
        opciones = pregunta["opciones"]
        random.shuffle(opciones)
        for i, opcion in enumerate(opciones):
            self.opciones[i].config(text=opcion, value=opcion)
        self.opcion_var.set(None)
        self.resultado_var.set("")
        self.siguiente_btn.config(state=tk.NORMAL)

    def siguiente_pregunta(self):
        if not self.opcion_var.get():
            messagebox.showwarning("Advertencia", "Por favor selecciona una respuesta")
            return

        self.siguiente_btn.config(state=tk.DISABLED)

        pregunta = self.preguntas[self.indice_pregunta]
        if self.opcion_var.get() == pregunta["respuesta_correcta"]:
            self.resultado_var.set("¡Correcto!")
            self.resultado_label.config(fg="green")
            self.puntaje += 1
        else:
            self.resultado_var.set(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta_correcta']}")
            self.resultado_label.config

