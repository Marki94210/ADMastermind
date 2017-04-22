#----fonctions----

"""def image(p_case,p_casesprite,p_xstart):
	p_case += 1
	if p_case > 6:
		p_case = 0
	for ligne in gameGrid:
		num_case = 0
		for sprite in ligne:
			x =  p_xstart * taille_sprite
			y = 12 * taille_sprite
			if sprite == p_casesprite:
				fenetre.blit(colorsList[p_case],(x,y))"""

#-----------------


from random import randint
import pygame
from pygame.locals import*

pygame.init()

fenetre = pygame.display.set_mode((270,320),RESIZABLE)

taille_sprite = 20

#On crée l'interface du jeu en placant un fichier texte dans un tableau (liste de liste)
with open("GameGrid.txt") as fichier:
	gameGrid = []
	for ligne in fichier:
		trial_line = []
		for sprite in ligne:
			if sprite != "\n":
				trial_line.append(sprite)
		gameGrid.append(trial_line)

#Chargement de tous les carrés du jeu 
rouge = pygame.image.load("red.png").convert()
bleu = pygame.image.load("blue.png").convert()
orange = pygame.image.load("orange.png").convert()
blanc = pygame.image.load("white.png").convert()
violet = pygame.image.load("purple.png").convert()
jaune = pygame.image.load("yellow.png").convert()
vert = pygame.image.load("green.png").convert()
noir = pygame.image.load("black.png").convert()

#création d'une liste contenant toutes les couleurs
colorsList = (rouge,bleu,orange,blanc,violet,jaune,vert)

#variable de la boucle principale
continuer=1

#BOUCLE DU JEU ENTIER
while continuer:
	
	#chargement et affichage de l'image
	fond = pygame.image.load("fond_accueil.png").convert()
	fenetre.blit(fond,(0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle pour reset le jeu
	continuer_jeu = 1
	continuer_accueil = 1
	continuer_regles = 1
	continuer_fin = 1
	
	numberGenerator = []
	
	case_1 = 0
	case_2 = 0
	case_3 = 0
	case_4 = 0

	life = 10
	line = 1

	#BOUCLE D'ACCUEIL
	while continuer_accueil:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		#Prise en compte des commandes de l'utilisateur durant le jeu
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == pygame.QUIT:
				
				continuer_accueil = 0
				continuer_jeu = 0
				continuer_regles=0
				continuer_fin = 0
				continuer = 0
				
			elif event.type == KEYDOWN:				
				#Lancement du jeu
				if event.key == K_p:
					continuer_accueil = 0
					continuer_regles = 0
					fond = pygame.image.load("fondmastermind.png").convert()
					fenetre.blit(fond, (0,0))
				
				#Lancement des regles
				elif event.key == K_r:
					continuer_accueil=0
					fond = pygame.image.load("fond_regles.png").convert()
					fenetre.blit(fond, (0,0))

	#BOUCLE DE REGLE
	while continuer_regles:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
		
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == pygame.QUIT:
				
				continuer_accueil = 0
				continuer_jeu = 0
				continuer_fin = 0
				continuer = 0
				
			elif event.type == KEYDOWN:				
				#Lancement du jeu
				if event.key == K_p:
					
					continuer_accueil = 0
					continuer_regles = 0
					
					fond = pygame.image.load("fondmastermind.png").convert()
					fenetre.blit(fond, (0,0))		
				
				#Lancement du menu
				if event.key == K_ESCAPE:
					
					continuer_regles=0
					continuer_jeu = 0 	
					continuer_fin = 0

		pygame.display.flip()				


	#BOUCLE DE JEU
	while continuer_jeu:

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		#Generation de la solution à trouver
		while len(numberGenerator)<4:
			randomNumber=str(randint(0,6))
			if randomNumber not in numberGenerator:
				numberGenerator.append(randomNumber)
		masterCode = numberGenerator[0] + numberGenerator[1] + numberGenerator[2] + numberGenerator[3]

		num_ligne = 0
		for ligne in gameGrid:
			num_case = 0
			for sprite in ligne:
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				num_case +=1
			num_ligne +=1

		#Prise en compte des commandes de l'utilisateur durant le jeu
		for event in pygame.event.get():
				
				#Fait quitter le jeu (croix rouge)
				if event.type == pygame.QUIT:
					
					continuer_accueil=0
					continuer_jeu = 0
					continuer_fin = 0
					continuer = 0
				
				elif event.type == KEYDOWN:

					#Fait revenir au menu
					if event.key == K_ESCAPE:
						
						continuer_jeu = 0
						continuer_fin = 0

					#Fait changer la couleur de la premiere case
					elif event.key == K_e:
						case_1 += 1
						if case_1 > 6:
							case_1 = 0
						for ligne in gameGrid:
							num_case = 0
							for sprite in ligne:
								x = 4 * taille_sprite
								y = 12 * taille_sprite
								if sprite == "6":
									fenetre.blit(colorsList[case_1],(x,y))

					#Fait changer la couleur de la deuxieme case				
					elif event.key == K_r:
						case_2 += 1
						if case_2 > 6:
							case_2 = 0
						for ligne in gameGrid:
							num_case = 0
							for sprite in ligne:
								x = 5 * taille_sprite
								y = 12 * taille_sprite
								if sprite == "7":
									fenetre.blit(colorsList[case_2],(x,y))

					#Fait changer la couleur de la troisieme case
					elif event.key == K_t:
						case_3 += 1
						if case_3 > 6:
							case_3 = 0
						for ligne in gameGrid:
							num_case = 0
							for sprite in ligne:
								x = 6 * taille_sprite
								y = 12 * taille_sprite
								if sprite == "8":
									fenetre.blit(colorsList[case_3],(x,y))

					#Fait changer la couleur de la quatrieme case
					elif event.key == K_y:
						case_4 += 1
						if case_4 > 6:
							case_4 = 0
						for ligne in gameGrid:
							num_case = 0
							for sprite in ligne:
								x = 7 * taille_sprite
								y = 12 * taille_sprite
								if sprite == "9":
									fenetre.blit(colorsList[case_4],(x,y))

					#Enclenche la vérification de la combinaison du joueur et son affichage
					elif event.key == K_RETURN:
						
						right = 0
						wrong = 0

						#On réunit les valeurs dans les cases afin de constituer un code à 4 chiffres (pouvant être identiques)
						challengerCode = str(case_1)+str(case_2)+str(case_3)+str(case_4)

						fenetre.blit(colorsList[case_1],(4*taille_sprite,line*taille_sprite))
						fenetre.blit(colorsList[case_2],(5*taille_sprite,line*taille_sprite))
						fenetre.blit(colorsList[case_3],(6*taille_sprite,line*taille_sprite))
						fenetre.blit(colorsList[case_4],(7*taille_sprite,line*taille_sprite))

						#Vérification du code entré
						for g in range(4):
							if challengerCode[g] in masterCode and challengerCode[g] is not masterCode[g]:
								wrong += 1

							if challengerCode[g] is masterCode[g]:
								right += 1

						#Affichage des carrés noirs/blancs
						for black in range(wrong):
							fenetre.blit(noir,((9+black)*taille_sprite,line*taille_sprite))

						for white in range(right):
							fenetre.blit(blanc,((9+wrong+white)*taille_sprite,line*taille_sprite))

						if right < 4:
							line += 1
							life -= 1
						else:
							
							#fermer la boucle jeu et retourner au menu
							continuer_jeu = 0
							
							#chargement et affichage de l'image de victoire
							fond = pygame.image.load("fond_gagne.png").convert()
							fenetre.blit(fond,(0,0))


						if life == 0:
							
							continuer_jeu = 0
							
							#chargement et affichage de l'image de défaite
							fond = pygame.image.load("fond_perdu.png").convert()
							fenetre.blit(fond,(0,0))


		pygame.display.flip()


	#BOUCLE DE FIN
	while continuer_fin: 

		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == pygame.QUIT:
				
				continuer_accueil = 0
				continuer_jeu = 0
				continuer_fin=0
				continuer = 0
				
			elif event.type == KEYDOWN:				
				#Retour au menu		
				if event.key == K_ESCAPE:
					

					continuer_fin = 0	

		pygame.display.flip()		



pygame.quit()