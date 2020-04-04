#!/bin/bash
directory_name=/home/osboxes/Desktop/scene_detection/directory_images/
#file_count=$(ls /home/osboxes/Desktop/scene_detection/directory_images | wc -l)
#echo "directory name is    "
#echo "$directory_name"
file_count=$(ls $directory_name | wc -l)
#echo $file_count

progress-bar() {
  local duration=${1}
    already_done() { for ((done=0; done< (( ((($duration)*40)/($elapsed)) )); done++)); do printf "▇"; done }
    remaining() { for ((remain=$elapsed; remain< 60 - (( (($duration)*40)/($elapsed) )) ;  remain++)); 
    		do printf " "; done }
    percentage() { printf "| %s%%" $(( (($duration)*100)/($elapsed)*100/100 )); }
    clean_line() { printf "\r"; }
  	  declare -i elapsed=file_count
      already_done; remaining; percentage
      sleep 1
      clean_line
}

python3 db_setup.py

counter=1
#for entry in "/home/osboxes/Desktop/scene_detection/directory_images"/*
for entry in $(ls $directory_name)
do 
  #echo "$entry"
  python3 unified.py $directory_name/$entry
  progress-bar counter
  counter=$((counter + 1))
done