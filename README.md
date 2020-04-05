# scene_detection
The objective of this project is given an input image, develop a model which shall identify the particular scene in the image. Currently, I am using the categories as a part of the Places365 challenge created by the CSAIL Laboratory at MIT.  

# Instructions to Setup the Environment and Execute the Code

1. Download the code in this repository.
git clone https://github.com/vbhave/scene_detect_test/

2. Create a new conda environment to simplify the installation of all dependencies. 
conda create --name sceneDetect python=3.7.4     

3. Activate the new conda environment. 
conda activate sceneDetect

4. Give executable permissions to a script to install the requirements and comply other directory structure requirements. 
chmod +x conda_create.sh

5. Execute the above script
./conda_create.sh

6. Open script.sh and on line 3, change the path to the directory containing the images you want to execute this code on.

7. Execute the script which shall predict the scene class and the attributes of the image. 
./script.sh

The output should be generated in the output directory. The output consists of a results.txt file and a test.db database. The results.txt is a text file containing the name of each image, the top 5 classes with their confidence scores and the attributes. 

The test.db is a SQLite database. It consists of only one table 'scene_detection'. This table shall consist of 4 columns, first one being image name which shall also act as the primary key of the table. The second column stores whether the image is in an indoor or outdoor environment. The third column contains a json object of the top 5 scene classes and their respective confidence scores. The fourth and last column is a comma separated list of the attributes of the image.

<b> Note: </b> You may encounter an error like the 'Bleach' package has not been installed. This package is not a requirement to execute the code in this directory. So it's safe to ignore that. 

# Directory Structure - 

<b> conda_create.sh -> </b> A script to install the requirements and comply with other directory structure requirements. 

<b> create_directories_basic.py -> </b> This script requires two command line arguments as input. First is a directory which should contain the images you want to classify. If a directory with the name as the second argument does not exist such a directory would be created and results would be appended into the output directory. Both the command line arguments are required.
python3 create_directories_basic.py <input_image_dir> <output_dir>

<b> db_setup.py -> </b> Creates a database and the schema as per requirement. 

<b> directory_images -> </b> Directory containing about 20 sample images, which could be used for some general testing purposes.

<b> requirements.txt -> </b> Contains the list of all packages and their version numbers to be installed in the new conda environment. 

<b> script.sh -> </b> The script which shall execute the python code on each image and generate the final output. 

<b> unified.py -> </b> The actual python code using a ResNet-18 model to predict the scene classes and the attributes. 

Rest all files like - categories_places365.txt, IO_places365.txt, labels_sunattribute.txt, and any other files which may get downloaded later during the execution of the code are like index files/lookup tables, required for the execution of the ResNet-18 model and should not be modified. 
