import time
import datetime
import pygame

def set_alarm(alarm_time):
    
    print(f"Alarm set for {alarm_time}.")
    sound_file = "Audio For Alarm Clock.mp3"  # Replace with the path to your alarm sound file
    is_running = True
    while is_running:
        
        current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Get the current time in HH:MM:SS format
        print(f"Current time: {current_time}", end="\r")  # Print the current time, overwriting the previous line
        if current_time == alarm_time:
            print("Wake up! It's time!")
            pygame.mixer.init()     #Initialize the mixer module of Pygame to play the alarm sound
            pygame.mixer.music.load(sound_file)   #load the specified sound file into the mixer
            pygame.mixer.music.play()   #Play the loaded sound file
            
            while pygame.mixer.music.get_busy():  #Keep the program running until the alarm sound finishes playing
                time.sleep(1)  # Check every 1 second
            
            
            is_running = False
        time.sleep(1)  # Check every 1 second


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)