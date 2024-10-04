# Uchicago Summer Session 2023 Datascience Final Project

## By Alex Ramirez, James Lin, Corona Tian and Jiaxi Gao

Predicting solubility of molecules using different models and featurizers

- Google slides [here](https://docs.google.com/presentation/d/1AsLmARh14S6VrX4i22SRakJaMcos_oLuE3odWVhBWAA/edit?usp=sharing)
- Writeup [here](https://docs.google.com/document/d/1fgVQPa7_vVjLtaloX6Kyowh7Ua_8eq6EjhcoLDfZ5B4/edit?usp=sharing) (WIP)

## Building (poetry)

1. Download [Poetry](https://python-poetry.org/docs/#installation)
2. Clone this repository
3. Run `poetry install` in the root directory of this repository
4. Either
   1. Option 1, jupyter lab
      1. Run `poetry run jupyter notebook` to start the notebook server
      2. Open the outputted link in your browser
   2. Option 2, vscode
      1. Run `poetry env info --path`
      2. Open the command pallet (Ctrl+Shift+P) and type `Python: Select Interpreter`
      3. Click "Enter interpreter path" and paste the path from step 1
      4. Open the jupyter notebook file in vscode
      5. On the top right, click the "Select Kernel" button and select the kernel with the same name as the path from step 1

## Building (pip) (untested)

1. Make sure you running a python ver `>=3.10,<3.11`
2. Clone this repository
3. Run `pip install -r requirements.txt` in the root directory of this repository
4. Follow step 4 from the poetry instructions

## Notebooks (in /notebooks)

| Notebook               | Description                                                                      |
| ---------------------- | -------------------------------------------------------------------------------- |
| `main.ipynb`           | Main notebook. Data exploration, analysis, featurizer & model training / testing |
| `outliers.ipynb`       | More data exploration, analysis & seeing outliers in the dataset                 |
| `testing_models.ipynb` | Testing saved models from `main.ipynb` on new, never seen molecules              |
| `util.py`              | Utility functions for saving / loading saved models                              |

## Models (in /models) (load using `pickle.load`)

| File                    | Name                              | Time     | Mean 5-fold RMSE | Mean 5-fold r^2 | RMSE   | r^2    |
| ----------------------- | --------------------------------- | -------- | ---------------- | --------------- | ------ | ------ |
| `random_forest.pkl`     | Random forest                     | 23.2s    | 1.1444           | 0.7599          | 1.1474 | 0.7683 |
| `bagging.pkl`           | Bagging (Random forest estimator) | 1m 14.2s | 1.1461           | 0.760           | 1.1529 | 0.7660 |
| `bagging_reg.pkl`       | Bagging (Decision tree estimator) | 21.6s    | 1.1466           | 0.7563          | 1.1565 | 0.7646 |
| `gradient_boosting.pkl` | Gradient boosting                 | 12.7s    | 1.1767           | 0.7443          | 1.2129 | 0.7411 |
| `decision_tree.pkl`     | Decision tree                     | 3.1s     | 1.3269           | 0.6747          | 1.3840 | 0.6629 |
| `adaboost.pkl`          | AdaBoost                          | 7.2s     | 1.4032           | 0.6358          | 1.4327 | 0.6387 |

## Datasets (in /data)

| File                         | Source                                                                                                       | Description                                  |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| `aqsoldb.csv`                | <https://www.kaggle.com/datasets/sorkun/aqsoldb-a-curated-aqueous-solubility-dataset>                        | Main training dataset                        |
| `delaney.csv`                | <https://pubs.acs.org/doi/10.1021/ci034243x>                                                                 | 18 extra unique molecules for testing models |
