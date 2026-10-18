EXERCICE 2
* Calculer coût total
* crée une solution de départ au hasard : pour chaque container de chaque dépôt, elle choisit un magasin qui a encore besoin de containers, et elle l'y envoie, de façon à respecter les stocks et les demandes.
* génère tous les petits changements possibles de la solution actuelle : elle déplace 1 container entre deux dépôts et deux magasins, de façon à garder les stocks et les demandes corrects.
* teste tous les petits changements, choisit toujours le meilleur voisin qui n'est pas interdit, interdit le retour en arrière pendant 3 itérations, et garde en mémoire la meilleure solution trouvée en 30 itérations. À la fin, elle affiche ce que D1 et D2 envoient à chaque magasin, avec le coût minimal (52).
* <img width="720" height="367" alt="Screenshot_20261018_081015_Drive~2 (1)" src="https://github.com/user-attachments/assets/4afa6775-9cbc-44fc-bd94-87837416045f" />

Exercice 3 

trouver le circuit le plus court qui passe une seule fois par chacune des 8 villes et revient à la ville 1 (problème du voyageur de commerce).
On compare 3 méthodes :
Recherche tabou (solution initiale 1-2-3-4-5-6-7-8-1, de coût 103)
Recuit simulé (5 itérations, avec une variation empirique de la température T)
Algorithme génétique
Résultat : le circuit le plus court coûte 98, par exemple 1-8-3-7-6-5-4-2-1. 
