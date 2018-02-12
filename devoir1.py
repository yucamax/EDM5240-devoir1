# coding:utf-8
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

