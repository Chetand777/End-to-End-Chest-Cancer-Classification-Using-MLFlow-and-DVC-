# End-to-End-Chest-Cancer-Classification-Using-MLFlow-and-DVC-


## Workflow

1. Update config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update entity
5. Update configuration manager in src config
6. Update components
7. Update the pipeline
8. Update main.py
9. Update dvc.yaml


[Documentation](https://mlflow.org/docs/latest/index.html)

#### cmd
- mlflow ui

#### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Chetand777/End-to-End-Chest-Cancer-Classification-Using-MLFlow-and-DVC-.mlflow
MLFLOW_TRACKING_USERNAME=Chetand777 \
MFLOW_TRACKING_PASSWORD=e1afbba45719bba39c443ab80bab12cfbb386212 \
python script.py

Run this to export new env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Chetand777/End-to-End-Chest-Cancer-Classification-Using-MLFlow-and-DVC-.mlflow

export MLFLOW_TRACKING_USERNAME=Chetand777

export MLFLOW_TRACKING_PASSWORD='PASSWORD'

```