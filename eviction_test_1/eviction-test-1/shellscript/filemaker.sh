read -p "Enter directory name : " DIRECTORY

read -p "Enter file name : " FILE
mkdir "$DIRECTORY"
touch "./$DIRECTORY/$FILE"
echo "hello" > "./$DIRECTORY/$FILE"
cd "./$DIRECTORY"
echo "world" >> ./"$FILE"
cat "$FILE"
