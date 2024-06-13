#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
import random

# Lista de preguntas
preguntas = [
    {
        "pregunta": "¿Cuales eran los limites de Egipto?",
        "opciones": [
                      "norte: mar mediterraneo, este: mar negro, sur: pueblo de nubia, oeste: desierto de sahara",
                      "este: mar negro, sur: pueblo de nubia, norte: mar mediterraneo, oeste: desierto de sahara",
                      "oeste: desierto de sahara, este: mar rojo, sur: pueblo de nubia, norte: mar mediterraneo",
                      "norte: mar Mediterraneo, este: desierto de sahara, sur: pueblo de nubia, oeste: mar rojo"
                      ],
        "respuesta_correcta": "oeste: desierto de sahara, este: mar rojo, sur: pueblo de nubia, norte: mar mediterraneo"
    },
    {
        "pregunta": "¿En que dos zonas se delimitaba Egipto?",
        "opciones": [
                      "Egipto Bajo o Delta, Egipto Alto o Valle",
                      "Bajo Egipto o Valle, Alto Egipto o Delta",
                      "Egipto Bajo o Valle, Egipto Alto o Delta",
                      "Bajo Egipto o Delta, Alto Egipto o Valle"
                      ],
        "respuesta_correcta": "Bajo Egipto o Delta, Alto Egipto o Valle"
    },
    {
        "pregunta": "¿Donde estan las piramides?",
        "opciones": [
                      "Bajo Egipto",
                      "Alto Egipto",
                      "Alto y Bajo Egipto",
                      "Delta y Valle"
                      ],
        "respuesta_correcta": "Bajo Egipto"
    },

    {
        "pregunta": "El nilo era fuente de vida por dos motivos:",
        "opciones": [
                      "1. Daba la agricultura. 2. Era la principal fuente de vida",
                      "1. Daba la pesca y el transporte. 2. Era la principal fuente de agua potable.",
                      "1. Daba la fertilidad a la tierra. 2. Era la principal fuente de energía.",
                      "1. Permitía la comunicación entre diferentes regiones. 2. Era la principal fuente de defensa militar."
                      ],
         "respuesta_correcta": "1. Daba la agricultura. 2. Era la principal fuente de vida"
    },

    {
        "pregunta": "Los principales cereales que cultivaban en Egipto eran:",
        "opciones": [
                      "Trigo y cebada",
                      "Centeno y avena.",
                      "Lentejas y habas.",
                      "Dátiles e higos."
                      ],
         "respuesta_correcta": "Trigo y cebada"
    },

    {
        "pregunta": "El principal ganado criado en Egipto era:",
        "opciones": [
                      "Camellos. Aunque tambien cabras, ovejas, patos y gansos",
                      "Cerdos. Aunque tambien cabras, ovejas, jabalies y gansos",
                      "Bovino. Aunque tambien cabras, ovejas, patos y gansos",
                      "Aves de corral. Aunque tambien vacas, ovejas, patos y gansos"
                      ],
         "respuesta_correcta": "Bovino. Aunque tambien cabras, ovejas, patos y gansos"
    },

    {
        "pregunta": "En ganadería los animales que se criaban  y eran  novedosos y exclusivos de Egipto eran",
        "opciones": [
                      "Patos y gansos",
                      "Búfalos y cebras.",
                      "Leónes y leopardos.",
                      "Antílopes y gacelas."
                      ],
         "respuesta_correcta": "Patos y gansos"
    },

    {
        "pregunta": "Cinco nombres de grandes faraones",
        "opciones": [
                      "Ramses II, Amenofis III, Cleopatra, Keops, Tutankamon",
                      "Hatshepsut, Akhenatón, Tutmosis III, Menes, Narmer.",
                      "Nefertiti, Seti I, Ramsés I, Ramsés III, Tutmosis I.",
                      "Ahmose I, Amenhotep I, Amenhotep II, Thutmose IV, Thutmose I."
                      ],
         "respuesta_correcta": "Ramses II, Amenofis III, Cleopatra, Keops, Tutankamon"
    },

    {
        "pregunta": "Dios/a RA",
        "opciones": [
                      "Guardian de tumbas",
                      "Dios del sol",
                      "Dios de los muertos",
                      "Protector del faraon"
                      ],
         "respuesta_correcta": "Dios del sol"
    },

    {
        "pregunta": "Dios/a ANUBIS",
        "opciones": [
                      "Guardian de tumbas",
                      "Dios del sol",
                      "Dios de los muertos",
                      "Protector del faraon"
                      ],
         "respuesta_correcta": "Guardian de tumbas"
    },

    {
        "pregunta": "Dios/a OSIRIS",
        "opciones": [
                      "Guardian de tumbas",
                      "Dios del sol",
                      "Dios de los muertos",
                      "Protector del faraon"
                      ],
         "respuesta_correcta": "Dios de los muertos"
    },

    {
        "pregunta": "Dios/a HORUS",
        "opciones": [
                      "Guardian de tumbas",
                      "Dios del sol",
                      "Dios de los muertos",
                      "Protector del faraon"
                      ],
         "respuesta_correcta": "Protector del faraon"
    },

    {
        "pregunta": "Dios/a THOT",
        "opciones": [
                      "Dios del desierto",
                      "Cabeza de carnero",
                      "Gran maga",
                      "Dios de la ciencia"
                      ],
         "respuesta_correcta": "Dios de la ciencia"
    },

    {
        "pregunta": "Dios/a AMON",
        "opciones": [
                      "Dios del desierto",
                      "Cabeza de carnero",
                      "Gran maga",
                      "Dios de la ciencia"
                      ],
         "respuesta_correcta": "Cabeza de carnero"
    },

    {
        "pregunta": "Dios/a SETH",
        "opciones": [
                      "Dios del desierto",
                      "Cabeza de carnero",
                      "Gran maga",
                      "Dios de la ciencia"
                      ],
         "respuesta_correcta": "Dios del desierto"
    },

    {
        "pregunta": "Dios/a ISIS",
        "opciones": [
                      "Dios del desierto",
                      "Cabeza de carnero",
                      "Gran maga",
                      "Dios de la ciencia"
                      ],
         "respuesta_correcta": "Gran maga"
    },

    {
        "pregunta": "Razones para ser esclavo",
        "opciones": [
                      "Hijo de esclavo, no pagar las deudas, trabajar en las minas",
                      "Prisionero de guerra, pegar a tu mujer, hijo de esclavo",
                      "Trabajar en minas, no pagar las deudas, prisionero de guerra",
                      "Prisionero de guerra, no pagar las deudas, hijo de esclavo"
                      ],
         "respuesta_correcta": "Prisionero de guerra, no pagar las deudas, hijo de esclavo"
    },

    {
        "pregunta": "Clase dirigiente",
        "opciones": [
                      "soldados, jefes del ejercito, sacerdotes, escribas, artesanos, visires",
                      "gobernadores, soldados, sacerdotes, escribas, tesoreros, visires",
                      "gobernadores, jefes del ejercito, sacerdotes, escribas, tesoreros, visires",
                      "jefes del ejercito, sacerdotes, escribas, artesanos, visires, gobernadores"
                      ],
         "respuesta_correcta": "gobernadores, jefes del ejercito, sacerdotes, escribas, tesoreros, visires"
    },

    {
        "pregunta": "Personas libres",
        "opciones": [
                      "campesinos, sacerdotes, ganaderos, artesanos",
                      "ganaderos, soldados, campesinos, escribas",
                      "campesinos, soldados, gobernadores, escribas",
                      "campesinos, soldados, ganaderos, artesanos"
                      ],
         "respuesta_correcta": "campesinos, soldados, ganaderos, artesanos"
    },

    {
        "pregunta": "Dos deberes del Faraon",
        "opciones": [
                      "1. Mantener a la población y darle seguridad y defensa. 2. dirigir las campañas militares",
                      "1. Recaudar impuestos. 2. Hacer los ritos sagrados en los templos",
                      "1. Dirigir las campañas militares. 2. Mantener los canales de riego perfectamente libres",
                      "1. Diseñar los grandes edificios y construcciones. 2. mantener a la población y darle seguridad y defensa"
                      ],
         "respuesta_correcta": "1. Mantener a la población y darle seguridad y defensa. 2. dirigir las campañas militares"
    },

    {
        "pregunta": "Señala la respuesta correcta sobre las estaciones",
        "opciones": [
                      "Las crecidas eran desde Enero hasta Marzo",
                      "La siembra era desde Noviembre hasta Marzo",
                      "La recogida era durante todo el verano desde Julio hasta Noviembre",
                      "Las inundaciones eran desde Diciembre a Marzo"
                      ],
         "respuesta_correcta": "La siembra era desde Noviembre hasta Marzo"
    },

    {
        "pregunta": "La ciudad de Alejandría pertenece al",
        "opciones": [
                      "Bajo Egipto",
                      "Alto Egipto",
                      "Medio Egipto",
                      "Grecia"
                      ],
         "respuesta_correcta": "Bajo Egipto"
    },

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
            self.resultado_label.config(fg="red")
            self.resultado_label.config

        self.indice_pregunta += 1
        if self.indice_pregunta < len(self.preguntas):
            self.root.after(2000, self.mostrar_pregunta)
        else:
            self.root.after(2000, self.mostrar_resultado)

    def mostrar_resultado(self):
        messagebox.showinfo("Resultado", f"Tu puntaje final es: {self.puntaje} de {len(self.preguntas)}")
        self.root.destroy()

if __name__ == "__main__":
    root_game = tk.Tk()
    app = JuegoPreguntas(root_game)
    root_game.mainloop()
