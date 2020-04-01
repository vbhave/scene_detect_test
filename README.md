# scene_detection
The objective of this project is given an input image, develop a model which shall identify the particular scene in the image. Currently, I am using the categories as a part of the Places365 challenge created by the CSAIL Laboratory at MIT.  

# Directory Structure - 

<b> img_dir -> </b> Directory containing about 20 sample images, which could be used for some general testing purposes.

<b> create_directories_basic.py -> </b> This script requires two command line arguments as input. First is a directory which should contain the images you want to classify. If a directory with the name as the second argument does not exist such a directory would be created and results would be appended into the output directory. Both the command line arguments are required.
python3 create_directories_basic.py <input_image_dir> <output_dir>

<b> image_api.py -> </b> Given an input image, the API simply returns the name of the class with highest confidence. One command line argument is required.
python3 image_api.py <input_image_name>

<b> my_basic.py -> </b> Prints the top 5 categories with maximum confidence on the 20 sample images in img_dir
python3 my_basic.py

<b> get_scene_attributes.py -> </b> Given a direcotry containing images can run the unified script which produces the scene classification scores, scene attributes and input or output classification.
python3 get_scene_attributes.py <input_image_dir>

<b> image_dict_api.py -> </b> Given an input image, the API returns a dictionary with keys being the names of the scenes and the values being their confidence scores. 
python3 image_dict_api.py <input_image_name>

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
