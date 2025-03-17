# do not change the method name
def main():
    songs = ['"Bohemian Rhapsody" by Queen', '"Hotel California" by Eagles', '"Sweet Child O\'Mine" by Guns N\'Roses',
             '"Billie Jean" by Michael Jackson', '"Stairway to Heaven" by Led Zeppelin']
    playlist = []
    print("Welcome to Playlist Manager!")
    print(f"Current playlist: {playlist}")
    for song in songs:
        song_name, artist = song.split(" by ")
        new_format = f"{song_name.replace('"', '')} - {artist}"
        playlist.append(new_format)
        print(f"Adding: {song}")
        print(f"Current playlist: {playlist}")
    print(f"Recently added songs (last 3): {playlist[-3:]}")
    print(f"First song: {playlist[0]}")
    print(f"Last song: {playlist[-1]}")
    print(f"Removing: \"Hotel California\" by Eagles")
    playlist.remove("Hotel California - Eagles")
    print(f"Current playlist: {playlist}")
    print(f"Top songs list: {playlist[:2]}")


# do not change the following lines:
main()
