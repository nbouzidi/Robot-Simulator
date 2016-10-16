#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crée le 03/07/16
Dernière modification le 03/07/16
Author: Najibe BOUZIDI
"""

import Tkinter as Tk
import time
import random

# ----------
# CONSTANTES
# ----------

ROBOT_WIDTH = 50
ROBOT_HEIGHT = 50


class Robot():
    """
    Cette classe permet de créer un robot
    """

    # ------------
    # CONSTRUCTEUR
    # ------------

    def __init__(self, fenetre, canvas, pos_x, pos_y, color):
        '''Constructeur'''
        self.fenetre = fenetre
        self.canvas = canvas
        self.circle = self.canvas.create_oval(
            pos_x, pos_y, pos_x + ROBOT_WIDTH, pos_y + ROBOT_HEIGHT, fill=color)
        self.cancel_id = None

    # ----------------------
    # ACCESSEURS & MUTATEURS
    # ----------------------

    def _get_robot_position(self):
        '''Renvoie les coordonnées du centre du robot dans la fenêtre'''
        x0, y0, x1, y1 = self.canvas.coords(self.circle)
        return x0 + 25, y0 + 25

    def _set_robot_position(self, x, y):
        '''Définit la position du robot dans la fenêtre'''
        self.canvas.move(self.circle, x, y)

    # ----------
    # PROPRIETES
    # ----------

    # def move_random(self):
    #     '''Déplace le robot aléatoirement'''

    #     # Coordonnées du robot
    #     x0, y0, x1, y1 = self.canvas.coords(self.circle)

    #     self.canvas.move(self.circle, 1, 0)

    #     # Boucle toutes les 20ms
    #     self.cancel_id = self.fen.after(20, self.move_random)

    def move_to(self, x_goal, y_goal):
        '''Déplace le robot vers un point donné'''

        # On récupère les coordonnées courantes du robot
        x0, y0, x1, y1 = self.canvas.coords(self.circle)

        # On calcule le déplacement à effectuer
        delta_x = x_goal - (x0 + (ROBOT_WIDTH / 2))
        delta_y = y_goal - (y0 + (ROBOT_HEIGHT / 2))

        # On décompose le déplacement total en déplacements élémentaires
        delta_x_elem = delta_x
        delta_y_elem = delta_y

        # # On déplace le robot
        # while x0 != x_goal and y0 != y_goal:
        #     self.canvas.move(self.circle, delta_x_elem, delta_y_elem)
        #     # Màj coordonnées du robot
        #     x0, y0, x1, y1 = self.canvas.coords(self.circle)

        # On déplace le robot
        self.canvas.move(self.circle, delta_x_elem, delta_y_elem)

        # On récupère ses nouvelles coordonnées
        x0, y0, x1, y1 = self.canvas.coords(self.circle)

        # Si l'objectif n'est pas encore atteint, on boucle
        if x0 != x_goal and y0 != y_goal:
            # Màj coordonnées du robot
            self.cancel_id = self.fenetre.after(20, self.move_to(x_goal, y_goal))

    def stop(self):
        '''Stoppe le robot'''
        if self.cancel_id is not None:
            self.fenetre.after_cancel(self.cancel_id)
            self.cancel_id = None
