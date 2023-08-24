# Solar Irradiance Forecasting [![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0?style=for-the-badge) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

___


## Project Goal

The goal of this project is to develop a solution for short-term irradiance forecasting using historical data. For context, irradiance is the amount of solar energy that reaches the earth’s surface per unit area. This irradiance is the basis for the calculation of overall power production capacity; forecasting irradiance allows you to forecast production. Accurate irradiance forecasting is essential for renewable energy generators, especially solar power plants, to optimize their energy production and meet regulatory requirements.

The objective is to leverage the various historical data provided in the *"[A comprehensive dataset for the accelerated development and benchmarking of solar forecasting methods](https://zenodo.org/record/2826939)"* dataset to build a solution that can accurately forecast irradiance for the next 20 minutes.

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