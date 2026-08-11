# 🏢 Projet 1 — Mini-CRM de gestion des clients

> Projet individuel · Python (ligne de commande)
> 📎 Lis d'abord les [règles communes](../README.md#️-règles-communes-à-tous-les-projets).

---

## 🎬 Le contexte (le vrai besoin)

L'entreprise gère ses clients dans un **fichier Excel** partagé qui devient vite ingérable :
tout le monde écrit dedans, on ne retrouve plus qui a été relancé, ni quand. L'équipe
commerciale a besoin d'un **outil simple** pour :
- garder la **liste des clients** et leurs coordonnées,
- noter les **interactions** (appels, e-mails, rendez-vous),
- savoir **qui relancer** et quand.

**Ta mission** : développer un **mini-CRM** (*Customer Relationship Management*) en Python,
utilisable au terminal, qui remplace ce fichier Excel bancal.

---

## 🎯 But du projet

> Concevoir une application de **gestion de clients** robuste et persistante, capable de
> stocker, rechercher, mettre à jour des clients et de **signaler les relances à faire**.

---

## ✅ Fonctionnalités OBLIGATOIRES

Un **menu** principal en boucle donnant accès à :

1. **Ajouter un client** : nom de l'entreprise, contact, e-mail, téléphone, statut
   (`prospect`, `client`, `inactif`). Vérifier qu'aucun champ obligatoire n'est vide.
2. **Afficher tous les clients** sous forme de tableau lisible. Gérer le cas « aucun client ».
3. **Rechercher un client** par nom (ou partie du nom) et afficher sa fiche complète.
4. **Modifier** les informations d'un client existant.
5. **Supprimer** un client (avec **confirmation** avant suppression).
6. **Ajouter une interaction** à un client : date + type (`appel`/`email`/`rdv`) + note.
   Un client peut avoir **plusieurs** interactions (historique).
7. **Voir les relances à faire** : lister les clients qui n'ont **aucune interaction depuis
   plus de 30 jours** (les « oubliés » qu'il faut recontacter).
8. **Sauvegarde automatique** dans un fichier `clients.json` : les données sont **rechargées**
   au démarrage. Rien ne se perd.

> 💡 **Structure de données suggérée** (à toi de l'affiner) : une **liste de dictionnaires**,
> chaque client étant un dictionnaire contenant lui-même une **liste** d'interactions.
> ```python
> {
>   "nom": "ACME SARL", "contact": "M. Diallo", "email": "...", "tel": "...",
>   "statut": "client",
>   "interactions": [
>       {"date": "2026-07-15", "type": "appel", "note": "Devis envoyé"}
>   ]
> }
> ```

---

## 🌟 Fonctionnalités BONUS (recherche encouragée)

- **Statistiques** : nombre de clients par statut, nombre total d'interactions ce mois-ci.
- **Filtrer** l'affichage par statut (ex : ne voir que les `prospect`).
- **Export** de la liste des clients en fichier **CSV** (ouvrable dans Excel) → module `csv`.
- **Tri** des clients par nom ou par date de dernière interaction.
- **Dates intelligentes** : calculer « il y a X jours » avec le module `datetime`.
- **Recherche avancée** : par e-mail, par statut, ou combinée.

---

## 🧪 Cas à gérer sans planter (robustesse — évalué !)

- L'utilisateur tape une lettre là où un numéro de menu est attendu.
- Recherche/modification/suppression d'un client **qui n'existe pas**.
- **Premier lancement** : le fichier `clients.json` n'existe pas encore.
- Un champ laissé **vide** à la saisie.
- Suppression : demander **confirmation** (`o/n`) avant d'effacer définitivement.

---

## 📦 Livrables

Voir la [liste commune](../README.md#-livrables-attendus-identiques-pour-les-3-projets).
En particulier : dépôt GitHub, `README.md`, fichier `clients.json` d'exemple avec **au moins
5 clients** de démonstration, et une démo orale.

---

## 🧮 Ce qui sera évalué en priorité

| Point d'attention | Pourquoi |
|---|---|
| La **fonction « relances à faire »** marche vraiment (calcul des 30 jours) | C'est le cœur métier du CRM |
| Les **interactions** sont bien liées au bon client et sauvegardées | Test de la structure imbriquée liste/dictionnaire |
| Le programme **ne plante pas** sur une recherche vide ou un client absent | Robustesse |
| Le code est **découpé en fonctions** (`ajouter_client`, `chercher_client`…) | Organisation |

> Barème détaillé : voir la [grille d'évaluation commune](../README.md#-grille-dévaluation-sur-20).
> 🧑‍🏫 Une **correction de référence** est disponible dans le dossier
> [`correction/`](./correction/) (réservée à l'encadrant).

---

## 💡 Conseils

1. **Commence petit** : d'abord « ajouter » + « afficher » + sauvegarde. Teste que ça marche.
2. Ajoute **une** fonctionnalité à la fois, en commitant à chaque étape.
3. Occupe-toi des **relances** (dates) **en dernier** parmi les obligatoires : c'est le plus dur.
4. 🔎 À chercher : « python lire écrire json », « python datetime différence entre deux dates ».
5. Garde des **données de test** pour ne pas ressaisir à chaque essai.
