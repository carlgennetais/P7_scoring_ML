# TODO
## 2023-12-08
- [x] MVP EDA, feature engineering et modeling
## 2023-12-15
- [x] vscode
- [x] github
- [x] dir data, notebooks, requirement, readme, src/init.py fonctions
- [x] problème imbalanced classes for training : manuellement équilibrer classes
## pour semaine suivante
- [ ] split notebooks EDA, preprocessing, modeling
- [ ] pipeline
    - limite data leakage
    - imblearn
- [ ] GridSearch(plusieurs pipelines avec param differents)
- [ ] KPI : accuracy ? matrice de confusion (rappel, précision, F-1 score, AUROC)
- [ ] changelog
- [ ] machinelearnia video pipeline
- [ ] 1e heure de https://yewtu.be/watch?v=0B5eIE_1vpU 

## later
- [ ] rectifieur de classes dans le pipeline
- [ ] optimisation paramètres
- [ ] KPI monétaire pour patron à partir de taux d'intéret, bien saisis etc
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
