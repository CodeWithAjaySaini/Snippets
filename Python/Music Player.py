import pygame
import os

# Initialize Pygame mixer
pygame.mixer.init()

# Function to load and play music
def load_music(file_path):
    if os.path.exists(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(-1)  # Play the music in an infinite loop
        print(f"Playing: {file_path}")
    else:
        print(f"File '{file_path}' not found!")

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()
    print("Music paused.")

# Function to resume music
def resume_music():
    pygame.mixer.music.unpause()
    print("Music resumed.")

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")

# Function to display the menu options
def show_menu():
    print("\nMusic Player Options:")
    print("1. Play Music")
    print("2. Pause Music")
    print("3. Resume Music")
    print("4. Stop Music")
    print("5. Quit")

def main():
    print("Welcome to the Simple Music Player!\n")
    
    music_file = input("Enter the path to the music file (e.g., 'song.mp3'): ")

    # Load and play the music
    load_music(music_file)

    # Show menu and listen for user input
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            load_music(music_file)
        elif choice == '2':
            pause_music()
        elif choice == '3':
            resume_music()
        elif choice == '4':
            stop_music()
        elif choice == '5':
            print("Exiting the music player. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
