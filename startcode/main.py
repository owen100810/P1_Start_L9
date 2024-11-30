import pygame, sys
from pygame.locals import QUIT
import tkinter as tk
from tkinter import messagebox


pygame.init()
venster = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Paint")
venster.fill((255, 255, 255))
kleur = (0, 0, 0)
radius = (1)


while True:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed() == (True, False, False):
            pygame.draw.circle(venster, kleur, pygame.mouse.get_pos(), radius)
        if pygame.mouse.get_pressed() == (False, False, True):
            pygame.draw.circle(venster, (255, 255, 255), pygame.mouse.get_pos(), radius)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                kleur = (7, 60, 249)
            if event.key == pygame.K_UP:
                radius += 1
                print("Radius: ", radius)
            if event.key == pygame.K_DOWN:
                radius -= 1
                print("Radius: ", radius)
            if event.key == pygame.K_g:
                kleur = (47, 249, 7)
            if event.key == pygame.K_r:
                kleur = (255, 0, 0)
            if event.key == pygame.K_p:
                kleur = (255, 5, 209)
            if radius == (0):
                radius += 1
                def showmessage():
                    messagebox.showinfo("Error!", "Je radius kan niet onder 0 zijn!")
                root = tk.Tk()
                root.withdraw()
                showmessage()
                print("Radius: ", radius)
            if event.key == pygame.K_s:
                pygame.image.save(venster, "tekening" + ".jpg")




    pygame.display.update()

