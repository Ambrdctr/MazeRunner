# MazeRunner

MazeRunner est un jeu d'aventure en vue de dessus où le but est de trouver un trésor caché dans un labyrinthe de plusieurs pièces.

## Installation

Pour utiliser MazeRunner il faut :
* installer [Python](https://www.python.org/downloads/release/python-337/)
* s'assurer d'avoir la bibliothèque [Pygame](http://www.pygame.org/download.shtml) fonctionnelle avec la version de python.
* Dans le fichier 'mazerunner.py', vous pouvez définir la taille de la fenêtre par rapport à la résolution de votre écran au début de la procedure 'principal'.
* Il suffit ensuite d'interpréter le fichier 'mazerunner.py' avec votre interpréteur favoris.
* Pour enlever le prompt au lancement il faut commenter le premier appel et decommenter le second tout en bas du fichier 'mazerunner.py'
* Une fois lancé, vous pouvez changer la difficulté dans 'OPTIONS'

## Instructions

### Règles du jeu
* À l'extérieur :
	Vous apparraissez à l'extérieur du donjon. Ici vous pouvez voir l'entrée de celui si ![Escalier vers le bas](/images/entreeDonjon.png), et quelques marchands ![Epée et Hache](/images/forgeron.png) ![Eprouvettes](/images/sorciere.png)plus un acheteur d'objets![Sac de pièces](/images/acheteur.png).
	Vous pouvez faire des échanges avec ces derniers, les marchands vendent des objets contre vos pièces, l'acheteur achete vos objets contre des pièces.
	Plus vous achetez plus vous revendez vos objets chers mais plus vous revendez plus vous achetez les objets des marchands chers, à vous d'être bon commerçant. 
	Pour entrer dans le donjon il suffit de se deplacer sur l'entrée.
* Dans le donjon :
	Vous vous trouvez à l'entrée du labyrinthe ![Escalier](/images/entree.png), il faut vous déplacer dans les couloir de celui-ci et pourquoi pas tomber sur une salle.
	* Une salle :
		Elle contient des monstres ![Chevalier rouge](/images/m_bas.png) qui apparraissent seulement lors de la première visite de la salle.
		Les tuer est assez délicat car il vous faut avancer vers eux tout en prenant en compte votre vitesse d'attaque. Il vous font perdre leur force +- 2 points de vie à chaque attaque
		Elle contient aussi un coffre ![Coffre bois](/images/c_haut.png) qui contient lui même des objets ![Pieces](/images/piece50.png) ![Heaume](/images/heaume.png) ![Couteau](/images/couteau.png)![Potion](/images/pt1.png).
		Lorsque vous vous avancez vers un coffre celui-ci s'ouvre et vous pouvez prendre son contenu en cliquant sur les objets, 
		Attention vous ne pouvez transporter que 10 objets non équipés seulement.
		Vous pouvez aussi vous servir des coffre comme stockage pour les objets qui vous ne servent pas.
	La sortie du labyrinthe est sois une trappe ![Trappe bois](/images/trappe.png)sois le trésor ![Trésor](/images/tresor.png). Dans les deux cas il vous faut une clé ![Clé dorée](/images/cle.png)pour sortir, celle si disparaitra à la première utilisation,
	Il vous en faudra donc une nouvelle pour sortir d'un autre niveau.
	Une fois la sortie trouvée la minimap en bas à droite affichera le chemin que vous avez parcouru pour la trouver
* Statistiques :
	En haut à droite de l'écran vous pouvez voir des barres de couleurs, chacune correspond à une caractéristique du personnage.
	Ce code couleur est repris par les potions, par exemple la potion rouge augmentera la vie du personnage (pas plus de 100)
	La mémoire correspond au temps pendant lequel vous mémorisez les cases que vous voyez.
	La vitesse : le temps minimale entre deux attaque = 1.5/vitesse
	La force, les dégats +- 2 que vous infligez aux monstres
	Lorsque vous avez un casque équipé une barre de protection apparait, cette barre remplace la vie temps que vous portez le casque (une fois la protection à 0 le casque disparait, il est cassé)
* Equipements :
	Pour équiper un objet ouvrez votre inventaire ('i') et cliquez sur l'objet en question, il sera placer automatiquement au bon endroit
	Vous pouvez équiper jusqu'à 3 objets différents, un casque (casque viking ou heaume), une potion (qui disparetra une fois l'effet épuisé (en actualisant les stats), et une arme (couteau, épée)
	Ces équipements feront évoluer vos statistiques (seulement lorsqu'il sont équipés)
* Minimap :
	Représentation globale du monde dans lequel vous vous trouvez
	Dans le donjon l'entrée est en vers et la sortie en rouge
	Votre position est représentée par le carré jaune
* Messages :
	Des messages apparaitrons pour vous guider
	Pour les fermer il suffit de cliquer, presser echap ou appuyer sur la croix de la fenêtre

### Commandes
Les déplacements et les choix du menu se font à l'aide des flèches directionnelles. Pour valider un choix faites 'Entrée'.
Pour ouvrir l'inventaire il faut appuyer sur la touche 'i'.
On peut mettre le jeu en pause à l'aide de la touche 'echap'.
Pour rammasser des objets dans les coffres ou faire des échanges avec les marchands, il suffit de cliquer (en relacher le clic) sur les objets avec la souris.


## Crédits
Raphaël Tournafond
Ambroise Decouttere
L2 CMI INFO USMB

## License
OpenSource

Projet Developpement VISI301