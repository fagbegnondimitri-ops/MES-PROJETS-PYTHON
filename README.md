# MINI_APP— README

Description
-----------

Petit projet pédagogique contenant des exercices Python et une application interactive de gestion de clients : `mini_app.py`.

Prérequis
----------

- Python 3.8+ (bibliothèque standard uniquement).

Utilisation
-----------

1. Ouvrez un terminal dans le dossier du projet.
2. Lancez :

```bash
python mini_app.py
```

Le programme affiche un menu interactif. Entrez le numéro de l'option puis appuyez sur Entrée.

Menu et fonctionnalités
------------------------

1. Ajouter un client
   - Champs obligatoires (non vides) : `ENTREPRISE`, `CONTACT`, `E_MAIL`, `TEL`, `STATUT`.
   - `STATUT` doit être `client`, `inactif` ou `prospect` (insensible à la casse).
2. Afficher tous les clients
3. Rechercher un client (par `CONTACT`)
4. Modifier un client (met à jour `DATE_DE_MODIFICATION`)
5. Modifier une interaction (date/type/note)
6. Supprimer un client (confirmation `oui`/`non` requise)
7. Ajouter une interaction (date vérifiée pour ne pas être future)
8. Relances à faire (clients sans interaction depuis ≥ 30 jours)
9. QUITTER

Comportement du code
--------------------

- Le script initialise ou lit le fichier `mini.json` avec `DOSSIER = Path(__file__).parent / "mini.json"`.
- Les champs obligatoires sont contraints à ne pas être vides : le programme redemande la saisie tant que l'utilisateur n'entre rien.
- Les dates d'interaction sont vérifiées et ne peuvent pas être supérieures à la date du jour.
- Aucune validation stricte d'email ou de numéro de téléphone n'est implémentée.

Fichier de données et remarque importante
------------------------------------------

- `mini.json` est créé automatiquement si absent.
- Écriture finale effectuée avec `DOSSIER = Path(__file__).parent / "mini.json"`.

Exemple de structure d'un client (JSON)
---------------------------------------

```json
{
  "ENTREPRISE": "Exemple SARL",
  "CONTACT": "Dupont",
  "E_MAIL": "dupont@example.com",
  "TEL": "0123456789",
  "STATUT": "prospect",
  "DATE_DE_CREATION": "2026-08-14",
  "DATE_DE_MODIFICATION": null,
  "INTERACTIONS": [
    {"DATE": "2026-07-01", "TYPE": "appel", "NOTE": "Premier contact"}
  ]
}
```

Dépannage rapide
-----------------

- Si `mini.json` est corrompu : renommez-le ou supprimez-le, le script en recréera un vide.
