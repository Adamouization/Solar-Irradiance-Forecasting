# Short-Term Solar Irradiance Forecasting using LSTMs
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/agpl-3.0?style=for-the-badge) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

___


## Project Goal

Solar energy is a rapidly growing source of renewable energy, contributing significantly to global sustainability efforts. It depends on solar irradiance, which is the amount of solar energy received per unit area, measured using GHI (global irradiance). Accurate solar irradiance forecasting is crucial for:
* optimising energy production
* designing, planning and operational management of solar energy farms.

The goal of this project is to build a predictive model that can accurately predict future irradiance.

The objective is to leverage the various historical data provided in the *"[A comprehensive dataset for the accelerated development and benchmarking of solar forecasting methods](https://zenodo.org/record/2826939)"* dataset to build a solution that can accurately forecast irradiance for the next 20 minutes.

## Preliminary LSTM result

![image](https://raw.githubusercontent.com/Adamouization/Solar-Irradiance-Forecasting/master/output/model_validation/lstm_v4_forecast_vs_actual.png)

## Setup

Create a virtual environment:

```
python -m venv <PATH>/Solar-Irradiance-Forecasting
source <PATH>/Solar-Irradiance-Forecasting/bin/activate
```

Install requirements:

```
cd Solar-Irradiance-Forecasting
pip install -r env/requirements-light.txt
```

Download data:
```
python src/utils/donwload_zenodo_data.py
```

Open relevant Jupyternotebooks in `src/`

## License 
* see [LICENSE](https://github.com/Adamouization/Solar-Irradiance-Forecasting/blob/master/LICENSE) file.

## Contact
* Email: adam[at]jaamour[dot]com
* Website: www.adam.jaamour.com
* Linktree: https://linktr.ee/adamouization
