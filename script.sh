python3 db_setup.py
#for entry in "directory_images"/*
for entry in "/home/osboxes/Desktop/scene_detection/directory_images"/*
do 
  python3 unified.py $entry
done
