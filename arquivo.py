import sys

def caminho_recurso(relativo):
    try:
        base = sys._MEIPASS
    except:
        base = os.path.abspath(".")
    return os.path.join(base, relativo)
import tkinter as tk
from tkinter import messagebox
import random
import turtle
import pygame
import os
from PIL import Image, ImageTk, ImageSequence





class PedidoNamoroApp:
    def __init__(self):
        self.iniciar_musica()

        self.janela = tk.Tk()
        self.janela.title("Pedido de Namoro ❤️")
        self.janela.geometry("400x300")
        self.janela.resizable(False, False)

        self.canvas = tk.Canvas(self.janela, width=400, height=300, highlightthickness=0)
        self.canvas.pack()

        self.carregar_gif(caminho_recurso("fundo.gif"))
        self.criar_interface()

        self.janela.mainloop()

    # ---------- Música ----------
    def iniciar_musica(self):
        pygame.mixer.init()
        if os.path.exists("musica.mp3"):
            pygame.mixer.music.load(caminho_recurso("musica.mp3"))
            pygame.mixer.music.play(-1)

    # ---------- GIF ----------
    def carregar_gif(self, path):
        self.frames = []
        gif = Image.open(path)

        for frame in ImageSequence.Iterator(gif):
            frame = frame.resize((400, 300), Image.NEAREST)
            self.frames.append(ImageTk.PhotoImage(frame))

        self.frame_atual = 0
        self.bg = self.canvas.create_image(0, 0, anchor="nw", image=self.frames[0])
        self.animar_gif()

    def animar_gif(self):
        self.canvas.itemconfig(self.bg, image=self.frames[self.frame_atual])
        self.frame_atual = (self.frame_atual + 1) % len(self.frames)
        self.canvas.after(100, self.animar_gif)

    # ---------- Interface ----------
    def criar_interface(self):
        self.canvas.create_text(
            200, 90,
            text="Você aceita namorar comigo?",
            fill="white",
            font=("Arial", 16, "bold")
        )

        self.botao_sim = tk.Button(
            self.janela,
            text="Sim 💖",
            font=("Arial", 12, "bold"),
            bg="#FF69B4",
            fg="white",
            cursor="hand2",
            command=self.aceitou
        )
        self.botao_sim.place(x=110, y=180)

        self.botao_nao = tk.Button(
            self.janela,
            text="Não 😅",
            font=("Arial", 12, "bold"),
            bg="#FF69B4",
            fg="white",
            cursor="hand2",
            command=self.botao_nao_click
        )
        self.botao_nao.place(x=240, y=180)

    # ---------- Botão NÃO ----------
    def botao_nao_click(self):
        self.botao_nao.config(text=random.choice(["OPS!", "ERROU!", "HAHA!"]))

        self.janela.update_idletasks()

        x = random.randint(10, 300)
        y = random.randint(140, 240)

        self.botao_nao.place(x=x, y=y)

    # ---------- Aceitou ----------
    def aceitou(self):
        pygame.mixer.music.stop()
        messagebox.showinfo("Pedido Aceito ❤️", "Eu te amo!")

        self.janela.quit()
        self.janela.destroy()

        self.desenhar_coracao()

    # ---------- Coração ----------
    def desenhar_coracao(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("white")
        self.screen.title("❤️ Eu te amo ❤️")
        self.screen.tracer(0)

        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.width(2)

        self.particulas = []

        self.pulsar = 1.0
        self.direcao = 1

        self.animar()
        turtle.done()

    def animar(self):
        self.pen.clear()

        # pulsação
        if self.pulsar >= 1.1:
            self.direcao = -1
        elif self.pulsar <= 0.9:
            self.direcao = 1

        self.pulsar += 0.01 * self.direcao

        self.desenhar_texto()
        self.desenhar_coracao_pulsante(self.pulsar)
        self.atualizar_particulas()

        self.screen.update()
        self.screen.ontimer(self.animar, 30)
    
    def desenhar_coracao_pulsante(self, escala):
        self.pen.color("#E63946", "#FF6B81")
        self.pen.penup()
        self.pen.goto(0, -40 * escala)
        self.pen.pendown()

        self.pen.begin_fill()
        self.pen.left(140)
        self.pen.forward(120 * escala)

        for _ in range(200):
            self.pen.right(1)
            self.pen.forward(1 * escala)

        self.pen.left(120)

        for _ in range(200):
            self.pen.right(1)
            self.pen.forward(1 * escala)

        self.pen.forward(120 * escala)
        self.pen.end_fill()
        self.pen.setheading(0)

    def atualizar_particulas(self):
        if random.random() < 0.2:
            p = turtle.Turtle()
            p.hideturtle()
            p.penup()
            p.color("#FF69B4")
            p.goto(random.randint(-80, 80), random.randint(-20, 40))
            p.dot(random.randint(8, 12))
            self.particulas.append(p)

        for p in self.particulas[:]:
            p.sety(p.ycor() + random.randint(1, 3))
            if p.ycor() > 120:
                p.clear()
                p.hideturtle()
                self.particulas.remove(p)

    def desenhar_texto(self):
        self.pen.penup()
        self.pen.goto(0, 120)
        self.pen.color("#FF69B4")
        self.pen.write(
            "EU TE AMO",
            align="center",
            font=("Courier New", 24, "bold")
        )

PedidoNamoroApp()
