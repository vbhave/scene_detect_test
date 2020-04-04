#!/bin/bash
file_count=$(ls /home/osboxes/Desktop/scene_detection/directory_images | wc -l)
echo $file_count

progress-bar() {
  local duration=${1}


    #already_done() { for ((done=0; done<$elapsed; done++)); do printf "▇"; done }
    #remaining() { for ((remain=$elapsed; remain<$duration; remain++)); do printf " "; done }
    #percentage() { printf "| %s%%" $(( (($elapsed)*100)/($duration)*100/100 )); }
    already_done() { for ((done=0; done< (( ((($duration)*40)/($elapsed)) )); done++)); do printf "▇"; done }
    remaining() { for ((remain=$elapsed; remain< 60 - (( (($duration)*40)/($elapsed) )) ;  remain++)); 
    		do printf " "; done }
    percentage() { printf "| %s%%" $(( (($duration)*100)/($elapsed)*100/100 )); }
    clean_line() { printf "\r"; }

  #for (( elapsed=1; elapsed<=$duration; elapsed++ )); do
  	  declare -i elapsed=file_count
      already_done; remaining; percentage
      sleep 1
      clean_line
  #done
  #clean_line
}


#FOLDER=output
#if [ ! -d "$FOLDER" ]; then
#	rm -r output
#fi
#mkdir output



python3 db_setup.py

#shopt -s nullglob
#numfiles=(*)
#numfiles=("find /home/osboxes/Desktop/scene_detection/directory_images/ -maxdepth 1")
#echo "$numfiles"

#numfiles=${#numfiles[@]}

#numfiles = $(find . -maxdepth 1 -type f -printf . | wc -c)

#echo "$numfiles"

#count = $("ls -l "/home/osboxes/Desktop/scene_detection/directory_images" | grep -v ^d | wc -l")
#echo "$count"
#for entry in "directory_images"/*
#progress-bar 10
#count_files = ${0}
counter=1
for entry in "/home/osboxes/Desktop/scene_detection/directory_images"/*
do 
  python3 unified.py $entry
  progress-bar counter
  counter=$((counter + 1))
done