# coding:utf-8

### BONJOUR, ICI JHR ###
### Mes notes et corrections sont précédées de trois dièses ###

### Il fallait tout d'abord conserver la variable «publications».
### Cela dit, on pouvait aussi s'en passer! :)
### Mais si on faisait ça, il fallait la laisser dans un autre fichier.
### J'ai appelé cet autre fichier «devoir1JHR.py» (et je l'ai rajouté à ton répertoire).
### Il était ensuite possible d'importer la variable «publications» avec le code suivant:

from devoir1JHR import publications ### Remarque: on ne met pas, ici, le «.py» au nom du fichier où se trouve le code qu'on importe

### Une fois cela fait; le code fonctionne très bien!
### C'est simple et efficace! Bravo!

### Je n'ai qu'une seule suggestion constructive à faire:
### Intéressant, ce que tu propose dans les 4 premières lignes, ci-dessous,
### mais ce n'est pas nécessaire; ça alourdit, même, un peu, ton code :)

#définition de la position des différents éléments 

nom_du_media=0
nb_de_partages=3
nb_de_reactions=4
nb_de_commentaires=5

#définition des variables

partages=0
reactions=0
commentaires=0
engagements=0

#on définit le premier média

media_actuel=publications[0][nom_du_media]

#création de la boucle

for i in range(0,len(publications)):
	if publications[i][nom_du_media]==media_actuel:
		partages+=publications[i][nb_de_partages]
		reactions+=publications[i][nb_de_reactions]
		commentaires+=publications[i][nb_de_commentaires]
	else:
		engagements=partages+reactions+commentaires

		print("Les publications du média",media_actuel,"ont été partagées",partages,"fois, ont provoqué",reactions,"réactions et ont généré",commentaires,"commentaires, pour un engagement total de",engagements,"en 2017.")

#le dernier élément n'est pas inclus dans la boucle puisque le code imprime les résultats d'une ligne seulement si un autre média se trouve après celle-ci, donc on recopie la séquence pour imprimer Vice Québec

		media_actuel=publications[i][nom_du_media]

		partages=0
		reactions=0
		commentaires=0
		engagements=0

		partages+=publications[i][nb_de_partages]
		reactions+=publications[i][nb_de_reactions]
		commentaires+=publications[i][nb_de_commentaires]
		
engagements=partages+reactions+commentaires
		
print("Les publications du média",media_actuel,"ont été partagées",partages,"fois, ont provoqué",reactions,"réactions et ont généré",commentaires,"commentaires, pour un engagement total de",engagements,"en 2017.")

