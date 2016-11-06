#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crée le 03/07/16
Dernière modification le 06/11/16
Author: Najibe BOUZIDI
"""

import Tkinter as Tk
import Robot

# ----------
# CONSTANTES
# ----------

TARGET_X = 100
TARGET_Y = 100
TARGET_WIDTH = 50
TARGET_HEIGHT = 50


class Environnement():
    """
    Cette classe permet de créer l'environnement de simulation
    """

    def __init__(self):
        '''Constructeur'''

        # Fenêtre principale
        self.fen = Tk.Tk()
        self.fen.geometry("500x500")
        self.fen.title('Simulation')

        # Menu principal
        self.menu = Tk.Menu(self.fen)

        # Sous-menu
        self.menu1 = Tk.Menu(self.menu, tearoff=0)
        self.menu1.add_command(label="Atteindre l'objectif",
                               command=self.move_robot_to_objective)
        self.menu1.add_command(label="Stopper le robot",
                               command=self.stop_robot)
        self.menu1.add_command(label="Quitter", command=self.fen.quit)

        # Ajout du sous-menu au menu principal
        self.menu.add_cascade(label="Menu", menu=self.menu1)
        self.fen.config(menu=self.menu)

        # Ajout d'un canvas (= zone de dessin) dans la fenêtre
        self.canvas = Tk.Canvas(self.fen, width=500, height=500)
        self.canvas.pack()

        # Ajout d'un robot
        self.robot = Robot.Robot(self.fen, self.canvas, 225, 225, "blue")

        # Ajout d'un objectif
        self.objectif = self.canvas.create_oval(
            TARGET_X, TARGET_Y, TARGET_X + TARGET_WIDTH, TARGET_Y + TARGET_HEIGHT, fill="red")

    def move_robot_to_objective(self):
        '''Déplace le robot vers l'objectif'''
        self.robot.move_to(TARGET_X + (TARGET_WIDTH / 2),
                           TARGET_Y + (TARGET_HEIGHT / 2))

    def stop_robot(self):
        '''Stoppe le robot'''
        self.robot.stop()

    def run(self):
        '''Lance la simulation'''
        self.fen.mainloop()
