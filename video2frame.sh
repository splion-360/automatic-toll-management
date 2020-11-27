for FILE_NAME in *.mp4
do
    ffmpeg -i "$FILE_NAME" -vf fps=1/1 "${FILE_NAME%.*}"%05d.jpg -hide_banner
done