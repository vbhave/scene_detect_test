#!/bin/bash

# record the start time. (done to measure the time required for the execution
# of the program)
start_time=$(date)
# enter the absolute path to the directory containing all images of the 
# test set
directory_name=/home/osboxes/Desktop/scene_detection/directory_images/

#directory_name=/home/osboxes/Desktop/scene_detection/grayscale
#directory_name=/home/osboxes/Desktop/places365/val_256

# creating the output directory where all results will be stored
mkdir output

# finding the number of images in the directory (actually counts the number of
# files but I am assuming that the directory contains only images)
file_count=$(ls $directory_name | wc -l)

# Creates an instance of the progress bar. Input is the number of input images
# on which computation has been completed. Percentage calculated in comparison
# to total number of images in the directory
progress-bar() {
  local duration=${1}
    # prints the "done"(▇) symbol in the ratio of the number of images whose 
    # computation is complete
    already_done() { for ((done=0; done< (( ((($duration)*60)/($elapsed)) )); done++)); do printf "▇"; done }

    # prints the "blank"( ) symbol in the ratio of the number of images whose 
    # computation is complete
    remaining() { for ((remain=0; remain< 60 - (( (($duration)*60)/($elapsed) )) ;  remain++)); 
    		do printf " "; done }

    # prints the percentage completion in numerical form
    percentage() { printf "| %s%%" $(( (($duration)*100)/($elapsed)*100/100 )); }

    # ensures that the next print shall happen on the same line so that we
    # done have a long output (else output lines will be equal to number of
    # images in the input directory)
    clean_line() { printf "\r"; }

    # calls each of the above functions in the order
  	  declare -i elapsed=file_count
      already_done; remaining; percentage
      sleep 1
      clean_line
}

# creates the dataset through the dataset setup script
python3 db_setup.py

echo "Started Working on Dataset. Check Progres Bar below - "

# counter is like a loop variable iterating over all images in the dataset
counter=1
for entry in $(ls $directory_name)
do  
  # executes the forward pass over the current image selected through the 
  # unified parsing script
  python3 unified.py $directory_name/$entry
  # updates the progress bar as per the number of images finished computing
  progress-bar counter
  # updates the loop variable for each input image finished computing  
  counter=$((counter + 1))
done

# measures the current time again, which is recorded as the end time of the 
# program
end_time=$(date)

# computes the total time required for the program and prints it
let "total_time = $(( $(date -d "$end_time" "+%s") - $(date -d "$start_time" "+%s") ))"

#echo "Took ${total_time} seconds to compute over ${counter} images." >> output/stats.txt
echo "Took ${total_time} seconds to compute over ${file_count} images." >> output/stats.txt

# print new line to create a nice output on the command line
echo " "