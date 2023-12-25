"""
Name:Bosheng Huang
Date started:2023-12-20

"""
import csv


def load_songs_from_file():
    songs = []
    print("Song List 1.0 - by Bosheng Huang")
    try:
        with open('songs.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                title, artist, year, state = row
                songs.append([title, artist, year, state])
        print("{} songs loaded".format(len(songs)))
    except FileNotFoundError:
        print("No existing songs file found. Starting with an empty library.")
    return songs


def display_menu():
    print("\nMenu:")
    print("D. Display Songs")
    print("A. Add Song")
    print("C. Complete a Song")
    print("Q. Quit")


def display_songs(songs):
    learned_songs = [song for song in songs if song[3].lower() == 'l']
    unlearned_songs = [song for song in songs if song[3].lower() == 'u']

    print("\nSongs in the Library:")
    print("{:<5} {:<10} {:<40} {:<20} {:<10}".format("No.", "Learned", "Title", "Artist", "Year"))
    print("-" * 85)

    for i, song in enumerate(songs, 1):
        learned_mark = '*' if not song[3].lower() == 'l' else ' '
        print("{:<5} {:<10} {:<40} {:<20} {:<10}".format(i, learned_mark, song[0], song[1], f"({song[2]})"))

    print("\n{} songs learned, {} songs still to learn.".format(len(learned_songs), len(unlearned_songs)))


def add_song(songs):
    print("Enter details for a new song.")
    while True:
        title = get_user_input("Title: ")
        if title == '' or title.isspace():
            print("Input can not be blank.")
        else:
            break
    while True:
        artist = get_user_input("Artist: ")
        if artist == '' or artist.isspace():
            print("Input can not be blank.")
        else:
            break

    while True:
        try:
            year = int(get_user_input("Enter the year of the song: "))
            if 1 <= year:
                break
            else:
                print("Number must be > 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    songs.append([title, artist, year, 'u'])
    print("{} by {} ({}) added to song list".format(title, artist, year))


def complete_song(songs):
    unlearned_songs = [song for song in songs if not song[3].lower() == 'l']

    if not unlearned_songs:
        print("No more songs to learn!")
        return

    while True:
        try:
            song_number = int(get_user_input("\nEnter the number of the song to mark as learned: "))
            if 1 <= song_number <= len(songs):
                selected_song = songs[song_number - 1]
                if selected_song[3] == 'l':
                    print("You have already learned {}".format(selected_song[0], selected_song[1]))
                else:
                    selected_song[3] = 'l'
                    print("{} by {} learned".format(selected_song[0], selected_song[1]))
                break
            elif song_number <= 0:
                print("Number must be > 0.")
            else:
                print("Invalid song number")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def save_songs_to_file(songs):
    with open('songs.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for song in songs:
            writer.writerow([song[0], song[1], song[2], song[3]])


def get_user_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            if user_input:
                return user_input
            else:
                print("Input cannot be empty. Try again.")
        except ValueError:
            print("Invalid input. Please try again.")


def main():
    songs = load_songs_from_file()

    while True:
        display_menu()

        choice = get_user_input("\nEnter your choice: ")

        if choice.lower() == 'd':
            display_songs(songs)
        elif choice.lower() == 'a':
            add_song(songs)
        elif choice.lower() == 'c':
            complete_song(songs)
        elif choice.lower() == 'q':
            save_songs_to_file(songs)
            print("{} songs saved to songs.csv.".format(len(songs)))
            print("Make some music!")
            break
        else:
            print("Invalid menu choice")


if __name__ == '__main__':
    main()
