class Song:
    def __init__(self, title, artist, album, year):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year

def add_song():
    title = input("Enter song title: ")
    artist = input("Enter song artist: ")
    album = input("Enter song album: ")
    year = input("Enter song year: ")
    song = Song(title, artist, album, year)
    songs.append(song)
print("Song added successfully.")

def binary_search_songs(songs, search_term):
    """
    Binary search implementation to search for songs based on title or artist.
    Assumes the songs list is sorted alphabetically by either title or artist.
    """
    results = []
    low = 0
    high = len(songs) - 1

    while low <= high:
        mid = (low + high) // 2
        song = songs[mid]

        if search_term in song.title or search_term in song.artist:
            # Check all songs to the left for matches
            left = mid - 1
            while left >= 0 and (search_term in songs[left].title or search_term in songs[left].artist):
                results.append(songs[left])
                left -= 1

            results.append(song)  # Add the current song

            # Check all songs to the right for matches
            right = mid + 1
            while right < len(songs) and (search_term in songs[right].title or search_term in songs[right].artist):
                results.append(songs[right])
                right += 1

            break  # Exit the loop after finding all matches

        if search_term < song.title or search_term < song.artist:
            high = mid - 1
        else:
            low = mid + 1

    return results

def search_songs():
    search_term = input("Enter a song title or artist to search for: ")
    results = binary_search_songs(sorted(songs, key=lambda x: x.title), search_term)
    if not results:
        print("No results found.")
    else:
        for song in results:
            print(song.title, song.artist)



def delete_song():
    search_term = input("Enter a song title or artist to delete: ")
    deleted = False
    for i in range(len(songs)):
        if search_term in songs[i].title or search_term in songs[i].artist:
            del songs[i]
            print("Song deleted successfully.")
            deleted = True
            break
    if not deleted:
        print("No matching song found.")

def sort_songs():
    sort_order = input("Sort by artist or title? (a/t) ")
    if sort_order.lower() == 'a':
        songs.sort(key=lambda s: s.artist)
    elif sort_order.lower() == 't':
        songs.sort(key=lambda s: s.title)
    else:
        print("Invalid sort order.")
        return
    for song in songs:
        print(song.title, song.artist, song.album, song.year)

# Main program loop
songs = []

# add initial songs to list
#title, artist, album, year
initial_songs = [{'title': 'Swim Good', 'artist' : 'Dermot Kennedy', 'album': 'Dermot Kennedy', 'year' : 2018 },
                 {'title': 'Song2', 'artist' : 'Artist2', 'album': 'Artist3', 'year' : 2022 },
                 {'title': 'Song3', 'artist' : 'Artist3', 'album': 'Album3', 'year' : 2019 },
                 {'title': 'Swim Good', 'artist' : 'by someone else', 'album': 'different album', 'year' : 2023} ]
for item in initial_songs:
    new_song = Song(title=item['title'], artist=item['artist'], album=item['album'], year=item['year'])
    songs.append(new_song)


while True:
    print("""
    JUKEBOX
    -------
    1. Add song
    2. Search songs
    3. Delete song
    4. Sort songs
    5. Exit
    """)

    choice = input("Enter your choice: ")
    if choice == '1':
        add_song() 
    elif choice == '2':
        search_songs()
    elif choice == '3':
        delete_song()
    elif choice == '4':
        sort_songs()
    elif choice == '5':
        print("Exiting jukebox.")
        break
    else:
        print("Invalid choice. Please try again.")