# Abalone_client
Pour lancer le client : (dans le bon dossier)

$ python abalon-client.py port(éventuel) pseudo(éventuel et sans espaces)
 
Stratégie :


Calculer tous les moves possible.
Eliminer un pion énemi si c'est possible et que au coup suivant l'adversaire ne peu pas gagner la partie.
Si ce n'est pas possible on regarde si un pion alié peut être éiminé au prochain tour si il ne bouge pas.
Dans le cas ou un/des pion(s) est/sont en danger on essaye de défendre (l')un des pion(s).
Autrement on calcule les coups qui ne mette pas de pions en position de danger pour le prochain tour, la liste de moves étant appellé neutralmoves.
Dans les neutralmoves on regarde si il est possible de dégager les bordures du plateau sinon on dirige les pions vers le centre du plateau.

bibliothèques utilisées :


socket : afin de faire les communications avec le serveur

JSON : afin d'envoyer du JSON au serveur

sys : afin d'utiliser d'éventuel arguments lors de l'exécution du client et définir un port et/ou un pseudo

time : afin de pouvoir calculer le temps pour trouver le meilleur move

random : afin de trouver un move aleatoire dans une liste de moves

copy : afin de copier une variable grobal dans une fonction pour la modifier en local
