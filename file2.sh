#!/bin/bash
echo -e "Enter the type of the file you want to delete (1-file, 2-directory): \c"
read choice

if [ "$choice" == "1" ]; then
    echo -e "Enter the name of the file you want to delete: \c"
    read file_name
    rm -i "$file_name"
    echo "Task finished."

elif [ "$choice" == "2" ]; then
    echo -e "Enter the name of the directory: \c"
    read dir_name
    rm -ri "$dir_name"
    echo "Task finished."

else
    echo "Invalid option. Please choose 1 or 2."
fi
