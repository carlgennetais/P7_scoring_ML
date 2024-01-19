# TODO
## 2023-12-08
- [x] MVP EDA, feature engineering et modeling
## 2023-12-15
- [x] vscode
- [x] github
- [x] dir data, notebooks, requirement, readme, src/init.py fonctions
- [x] problème imbalanced classes for training : manuellement équilibrer classes
## 2023-12-22
- [x] split notebooks EDA, preprocessing, modeling
- [x] pipeline
    - limite data leakage
    - imblearn
- [x] GridSearch(plusieurs pipelines avec param differents)
- [ ] regarder machinelearnia video pipeline
- [x] regarder 1e heure de [Scikit-Learn Crash course](https://yewtu.be/watch?v=0B5eIE_1vpU) 
- [ ] faire vrai changelog ?
- [x] rectifieur de classes dans le pipeline
## 2023-12-29 + 2024-01-05
- [x] shap values
- [x] fonction metier pour calculer gain/pertes avec y_pred/y
    - si vrai neg : taux d'interet * montant pret
    - si vrai pos : 0
    - si faux neg : perte 25%
        - saisie biens
	- KPI monétaire pour patron à partir de taux d'intéret, bien saisis etc
- [x] datadrift avec librairie Evidently pour monitorer changements dans le temps entre train et test
## 2024-01-12
- [x] commencer API
- [x] lire liens
- [x] comprende evidently
## 2024-01-19
- [x] split in 3 repos
- [ ] choix KPI : accuracy ? matrice de confusion, rappel, précision, F-1 score, AUROC
- [ ] utiliser seuil proba predict, gridsearch pour trouver meileur seuil de fonction de decision
- [ ] terminer shap values pour 1 individu
- [ ] routes API :
    - [x]/hello ou /ping : pour test
    - [x]/listcustomers : list des clients, liste json des ids users
    - [x]?id=14 : vecteur utils
    - [x]/predict?id=14 charge vecteur, fait calcul et renvoie 0/1 ou proba
    - [x] etat general de la pop : describe en json
    - [ ]/shap?id=14 : json avec dico 2 keys :
        -  pour 1 : contributions de chaque valeur
        -  pour 0
    - [ ] fonction qui extrait un vecteur
## semaine prochaine
- [ ] 

## later
- [ ] optimisation paramètres
- [ ] ecrire README etc
- [ ] poetry gestion venv
- [ ] changelog

# Notes
- accuracy = 0 est modèle parfait si on inverse sa prédiction
    - plus mauvais : 0.5
- 0 : prêt accordé, 1 : problème sur le prêt
- dashboard : streamlit plutôt que Dash
- convention X (matrice) mais y (array)
- data leakage : X -> y, ou train -> test
- split doit se faire avant scaler etc
- pycharm, DataSpell (nb et sql)
- choix API :
    - django (py)
    - flask (py)
    - fast (py, pas de templating, renvoie json)
    - ruby on rails
- streamlit pour front
- regarder figma maquettes
- planning
    - 1 semaine api/back
    - 1 semaine front (streamlit)
    - 1 semaine prod
    - 1 semaine devOps, test operationnels et mise en prod
