# Abalone_client
Pour lancer le serveur de jeu : cloner le répertoire de l'enseignant : https://github.com/qlurkin/PI2CChampionshipRunner

Exécuter la commande suivante dans le répertoire cloné :

$ python server.py abalone

Pour lancer le client : (dans le bon dossier)

$ python abalon-client.py [port]  [pseudo] (sans espaces)

Exemple : 

$ python abalon-client.py 5200 Player1

A noter :

Pour que la partie commence il faut aux moins 2 joueurs. Il faudra donc lancer le client dans 2 terminaux différents (sans utiliser le me même port).

$ python abalon-client.py 5200 Player1

$ python abalon-client.py 5300 Player2

Stratégie :

Calculer tous les moves possibles. Eliminer un pion ennemi si c'est possible et qu’au coup suivant l'adversaire ne peut pas gagner la partie. Si ce n'est pas possible on regarde si un pion allié peut être éliminé au prochain tour s’il ne bouge pas. Dans le cas ou un/des pion(s) est/sont en danger, on essaye de défendre (l')un des pion(s). Autrement (sinon) on calcule les coups qui ne mettent pas de pions en position de danger pour le prochain tour, la liste de moves étant appellée neutralmoves. Dans les neutralmoves on regarde s’il est possible de dégager les bordures du plateau sinon on dirige les pions vers le centre du plateau. S’il y a un bug dans la recherche du meilleur move, un move aléatoire est envoyé. Si aucun move n'est possible, on abandone.
Dernièrement on essaye d'éviter les moves qui provoquent un jeu qui tourne en boucle.

Bibliothèques utilisées :

socket : afin de faire les communications avec le serveur

JSON : afin d'envoyer du JSON au serveur

sys : afin d'utiliser d'éventuels arguments lors de l'exécution du client et définir un port et/ou un pseudo

time : afin de pouvoir calculer le temps pour trouver le meilleur move

random : afin de trouver un move aléatoire dans une liste de moves

copy : afin de copier une variable globale dans une fonction pour la modifier en local
