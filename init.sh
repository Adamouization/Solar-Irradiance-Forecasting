#!/bin/bash 
echo "Setting up Cloud environment..."

echo "Changing directory to '/home/jovyan/Solar-Irradiance-Forecasting'..."
cd  /home/jovyan/Solar-Irradiance-Forecasting

echo "Upading apt-get and intalling the latest version of 'libgl1-mesa-glx'..."
sudo apt-get update 
sudo apt-get install -y libgl1-mesa-glx 

echo "Installing Python libraries..."
pip install scikit-learn tqdm

echo "Exporting variables..."
export TF_ENABLE_ONEDNN_OPTS=0

echo "Setup completed successfully."