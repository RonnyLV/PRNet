DOWNLOAD_ID=$1
FILENAME=$2
CONFIRM=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies "https://docs.google.com/uc?export=download&id=${DOWNLOAD_ID}" -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=${CONFIRM}&id=${DOWNLOAD_ID}" -O "${}"
rm /tmp/cookies.txt