import os
from pathlib import Path
import re

song_title_catching_regex = r"\\contentsline \{subsection\}\{([A-Za-zÀ-ÖØ-öø-ÿ\s]+)\}"

curr_dir = os.path.dirname(os.path.realpath(__file__))
songs_filename = "main.sng"

songs_file_path = Path(curr_dir, songs_filename)

songs = []

with open(songs_file_path, 'r', encoding="utf-8") as file:
    for line in file:
        match = re.match(song_title_catching_regex, line)
        
        if match:
            songs.append((match.group(1), line))


songs_sorted = sorted(songs, key=lambda tup: tup[0])

with open(songs_file_path, 'w', encoding="utf-8") as file:
    for song, line in songs_sorted:
        file.write(line)

