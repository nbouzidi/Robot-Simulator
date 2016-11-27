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

TARGET_X_1 = 100
TARGET_Y_1 = 100

TARGET_X_2 = 150
TARGET_Y_2 = 200

TARGET_X_3 = 200
TARGET_Y_3 = 300

# Chemin à parcourir
PATH = [(TARGET_X_1, TARGET_Y_1),
        (TARGET_X_2, TARGET_Y_2),
        (TARGET_X_3, TARGET_Y_3)]

# PATH = [(TARGET_X_1, TARGET_Y_1)]

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
                               command=lambda: self.follow_path(PATH))

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
        self.robot = Robot.Robot(self.fen, self.canvas, 50, 50, "blue")

        # Ajout des objectifs
        self.objectif = self.canvas.create_oval(
            TARGET_X_1, TARGET_Y_1, TARGET_X_1 + TARGET_WIDTH, TARGET_Y_1 + TARGET_HEIGHT, fill="red")

        self.objectif2 = self.canvas.create_oval(
            TARGET_X_2, TARGET_Y_2, TARGET_X_2 + TARGET_WIDTH, TARGET_Y_2 + TARGET_HEIGHT, fill="red")

        self.objectif3 = self.canvas.create_oval(
            TARGET_X_3, TARGET_Y_3, TARGET_X_3 + TARGET_WIDTH, TARGET_Y_3 + TARGET_HEIGHT, fill="red")

    def follow_path(self, PATH):
        '''Déplace le robot selon le chemin PATH'''
        # for point in enumerate(PATH):
        #     print "Point cible: ",point
        #     self.move_robot_to_point(*point)

        self.move_robot_to_point(TARGET_X_1, TARGET_Y_1)

        self.move_robot_to_point(TARGET_X_2, TARGET_Y_2)

        self.move_robot_to_point(TARGET_X_3, TARGET_Y_3)

    def move_robot_to_point(self, x_goal, y_goal):
        '''Déplace le robot vers l'objectif'''
        # self.robot.move_to(y_goal[0], y_goal[1])
        self.robot.move_to(y_goal, y_goall)

    def stop_robot(self):
        '''Stoppe le robot'''
        self.robot.stop()

    def run(self):
        '''Lance la simulation'''
        self.fen.mainloop()
