#-*-coding:UTF-8 -*
import os
from random import randrange
from math import ceil

continuer_partie=True
argent=1000
print("Vous vous installer à la table de roulette avec",argent,"$")

while continuer_partie:
	
	argent_mise=-9
	try:
		argent_mise=input("Quel somme d'argent souhaitez vous miser?:")
		argent_mise=int(argent_mise)
	except ValueError:
		print("Le somme saisit n'est pas valide")
		continue
	if argent_mise>argent:
		print("Vous ne pouvez pas miser autant, vous avez seulement",argent,"$")
		continue
	if argent_mise<=0:
		print("Vous avez misé une somme inferieur ou égale à 0")
		continue
	a=True
	nombre_mise=-2
	while a==True:
		try:
			nombre_mise=input("Quel nombre souhaitez vous miser?(entre 1 et 30 compris):")
			nombre_mise=int(nombre_mise)
			a=False
		except:
			print("Le nombre saisit n'est pas valide")
			continue
		if nombre_mise<=0:
			print("Vous avez miser une somme inférieur ou égale à 0")
			a=True
			continue
		if nombre_mise>30:
			print("Vous avez misé un nombre suppérieur à 30")
			a=True
			continue
	nombre_choisit=randrange(1,30)
	if nombre_mise==nombre_choisit:
		argent+=argent_mise*3
		print("Vous avez misé sur le bon nombre, vous gagnez le montant de votre mise multiplié par 3:",argent_mise*3)
	elif nombre_mise%2==nombre_choisit%2: 
		argent+=ceil(argent_mise/2)
		print("Vous avez misé sur la bonne couleur, vous gagnez le montant de votre mise divisé par 2:",ceil(argent_mise/2))
	else:
		print("Vous n'avez ni misé sur le bon nombre, ni sur la bonne couleur, vous perdez votre mise.")
		argent-=argent_mise

	print("Vous avez maintenant",argent,"$")

	if argent==0:
		print("C'est perdu, dommage...")
		os.system("pause")
		a=True
		continuer_partie=False

	while a==False:
		continuer_partie=input("Voulez vous continez la partie?(Oui/Non)")
		if continuer_partie.lower()=="oui":
			continuer_partie=True
			a=True
		elif continuer_partie.lower()=="non":
			continuer_partie=False
			print("Vous quittez la table de roulette avec",argent,"$")
			a=True
		else:
			print("Vous n'avez pas saisit de réponse valide")
os.system("pause")

	















































































































































