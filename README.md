# Résolution du problème du sac à dos à l'aide de plusieurs solutions (Bruteforce vs programmation dynamique)

## Scénario
Nous sommes en charge de déterminer le meilleur portefeuille d'actions dans une entreprise parmi une liste d'action et dont le cout cumulé total est fixé.
Le résultat doit être calculé parmi une liste d'un grand nombre d'action et être fourni en moins d'une seconde.

## 1 - Bruteforce
L'approche bruteforce teste toutes les combinaisons possibles et détermine la meilleure

Pour exécuter le script, télécharger/cloner le repository, naviguez vers le dossier contenant le code puis exécuter dans un terminal :
```
python bruteforce.py
```

La solution bruteforce ne testera que le contenu du fichier test_shares.csv (20 actions) pour limiter le temps d'exécution.

## 2 - Optimized
La résolution du problème posé par le scenario peut être découpé en sous problèmes plus petits, nous pouvons donc utiliser la programmation dynamique.

Pour exécuter le script, télécharger/cloner le repository, naviguez vers le dossier contenant le code puis exécuter dans un terminal :
```
python optimized.py nom_fichier
```
Par défaut si **nom_fichier** n'est pas spécifié le script lira le fichier test_share.csv.
