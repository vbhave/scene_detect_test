# install pip inside the conda environment
conda install pip

# installs all the required libraries for the scene detection package
pip install -r requirements.txt

# allow executable permission to the generic script which can be used to 
# perform scene detection over images of the input directory specified in the
# script
chmod +x script.sh

# removes any directory or file with name output to avoid any clashes later
# where a directory named output is created to store all the results
# including the result database, result text file and program runtime 
# statistics
rm -r output