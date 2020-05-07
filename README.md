# scene_detection
The objective of this project is given an input image, develop a model which shall identify the particular scene in the image. Currently, I am using the categories as a part of the Places365 challenge created by the CSAIL Laboratory at MIT.  

# Instructions to Setup the Environment and Execute the Code

1. Download the code in this repository.

<b> git clone https://github.com/vbhave/scene_detect_test/ </b>

Ensure that you navigate in the directory. If you do git clone also do 

<b> cd scene_detect_test </b>

2. Create a new conda environment to simplify the installation of all dependencies. 

<b> conda create --name sceneDetect python=3.7.4 </b>

You may have to press 'y' one or more times to complete the installation. (As far as I know there is never a security issue to execute this command and the permission is taken just to obtain storage space for the execution of the operation.)

3. Activate the new conda environment. 

<b> conda activate sceneDetect </b>

4. Give executable permissions to a script to install the requirements and comply other directory structure requirements. 

<b> chmod +x conda_create.sh </b>

You may encounter a error like rm: cannot remove 'output': No such file or directory. It is safe to ignore this since the script tries to delete a directory which may or may not exist. In case the directory does not exist, such an error message gets displayed.

5. Execute the above script

<b> ./conda_create.sh </b>

6. Open script.sh and on line 3, change the path to the directory containing the images you want to execute this code on.

7. Execute the script which shall predict the scene class and the attributes of the image. 

<b> ./script.sh </b>

The output should be generated in the output directory. The output consists of a results.txt file and a test.db database. The results.txt is a text file containing the name of each image, the top 5 classes with their confidence scores and the attributes. 

The test.db is a SQLite database. It consists of only one table 'scene_detection'. This table shall consist of 4 columns, first one being image name which shall also act as the primary key of the table. The second column stores whether the image is in an indoor or outdoor environment. The third column contains a json object of the top 5 scene classes and their respective confidence scores. The fourth and last column is a comma separated list of the attributes of the image.

<b> Note: </b> You may encounter an error like the 'Bleach' package has not been installed. This package is not a requirement to execute the code in this repository. So it's safe to ignore that. 

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


# Timeline

# Week 1 - 2/14/2020 - 2/20/2020

I used a pretrained state of the art resnet model, trained on the Places365 dataset. The model gets reasonably good accuracy while tested on some sample random images. 

The current my_basic.py, downloads the weights of the pretrained resnet model, also downloads a bunch of sample images and prints on terminal the top 5 categories of each image. 

# Week 2 - 2/21/2020 - 2/27/2020

* I explored the Places 205 dataset which had fewer categories. However, the categories added in Places365, are of importance to this task and hence I decided to continue work on Places 365. 
* Worked with Kautilya to create API's as per the Image Similarity Task Requirement.

# Week 3 - 2/28/2020 - 3/5/2020

* I found a pretrained resnet model which when given an input image can classify whether the image is in an indoor or outdoor setting. 
* The same model can also be used to identify the scene attributes of an input image. However, I am unable to run the model in a loop, and works only when input one image at a time. However, the attributes produced by the model are extremely informative and can be used as features for other tasks.

# Week 4 - 3/6/2020 - 3/12/2020
* I took a pass this week to prepare for my mid terms of other courses. 

# Week 5 - 3/13/2020 - 3/19/2020
* Spring Break

# Week 6 - 3/20/2020 - 3/26/2020
* Modified the code to determine scene attributes in batch mode. 
* Resized images to get model to work on all kinds of images like those captured by laptops, mobile devices, datasets, etc.

# Week 7 - 3/27/2020 - 4/2/2020
* Worked on modularizing and packaging my code.
* Added installation instructions and other details to ship it to Dan.
* Had a meeting with Jagath. Using his remote access he tested the working of my code on Dan's machine on a few sample images. 

# Week 8 - 4/3/2020 - 4/9/2020
* Added some more features to my package like creating a progress bar in bash script. 
* Ran a baseline image colorization model. Used this model to convert grayscale images into colored images and got some improvement in scene detection results using the colorized images. (The confidence scores of the detected scene improved as compared to the model working on grayscale images.)

# Week 9 - 4/10/2020 - 4/16/2020
* I took a pass this week to catch up with assignments of other courses.

# Week 10 - 4/17/2020 - 4/23/2020
* I benchmarked my model on the validation set of Places365 dataset. 
* I have commented and documented my code.

# Week 11 - 4/24/2020 - 4/30/2020
* Worked on getting some results like interesting scene categories, scene categories with highest precision, recall, F1 scores.
* Worked on my Final Week Presentation.
