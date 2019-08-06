grep -oE '[a-zA-Z0-9]+' words.txt | sort | uniq -c | sort -r | awk '{print $2" "$1}'
