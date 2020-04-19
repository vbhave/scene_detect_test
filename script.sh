#!/bin/bash
start_time=$(date)
directory_name=/home/osboxes/Desktop/scene_detection/directory_images/
#directory_name=/home/osboxes/Desktop/scene_detection/grayscale
#directory_name=/home/osboxes/Desktop/places365/val_256

mkdir output

file_count=$(ls $directory_name | wc -l)

progress-bar() {
  local duration=${1}
    already_done() { for ((done=0; done< (( ((($duration)*60)/($elapsed)) )); done++)); do printf "▇"; done }
    remaining() { for ((remain=0; remain< 60 - (( (($duration)*60)/($elapsed) )) ;  remain++)); 
    		do printf " "; done }
    percentage() { printf "| %s%%" $(( (($duration)*100)/($elapsed)*100/100 )); }
    clean_line() { printf "\r"; }
  	  declare -i elapsed=file_count
      already_done; remaining; percentage
      sleep 1
      clean_line
}

python3 db_setup.py
echo "Started Working on Dataset. Check Progres Bar below - "
counter=1
for entry in $(ls $directory_name)
do  
  python3 unified.py $directory_name/$entry
  progress-bar counter
  counter=$((counter + 1))
done
counter=$((counter - 1))
end_time=$(date)
echo "start time is ${start_time}" >> output/stats.txt
echo "end time is ${end_time}" >> output/stats.txt
#let "total_time = ${end_time} - ${start_t ime}"
let "total_time = $(( $(date -d "$end_time" "+%s") - $(date -d "$start_time" "+%s") ))"
echo "time taken is ${total_time}" >> output/stats.txt
echo "Number of images computed is ${counter}" >> output/stats.txt
echo " "
#echo "Number of images computed is ${counter}"
#let ttpi=time_taken/counter
#ttpi=$((time_taken / counter))
#echo "$ttpi"
#echo "Time Taken Per Image is $ttpi" >> output/stats.txt