conda create --name sceneDetect python=3.7.4
eval "$(conda shell.bash hook)"
conda activate sceneDetect
conda install pip
pip install -r requirements.txt
chmod +x script.sh