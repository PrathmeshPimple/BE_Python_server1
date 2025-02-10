from task import *

def main():
    while True:
        command = input("Enter command: ").strip().lower()
        
        if command == "set alarm":
            set_alarm()  # This will now run in a separate thread
        
        elif command.startswith("open "):  
            open_application(command)  # Extracts app name & opens it

        elif "take photo" in command:
            take_photo()
        
        elif "screenshot" in command:
            take_screenshot()

        elif "internet speed" in command:
            get_internet_speed()

        elif "time" in command:
            get_current_time()

        elif "action" in command:
            action = input("Enter action (shutdown/sleep/restart): ").lower()
            system_control(action)

        # elif command.startswith("play "):
        #     song_name = command[5:]  # Extract song name
        #     play_song(song_name)

        # elif command == "pause":
        #     control_spotify("pause")

        # elif command == "next":
        #     control_spotify("next")

        # elif command == "previous":
        #     control_spotify("previous")

        # elif command == "volume up":
        #     control_spotify("volume up")

        # elif command == "volume down":
        #     control_spotify("volume down")

        # elif command =="close spotify":
        #     print("closing spotify in 1...")
        #     time.sleep(1)
        #     close_spotify()

        # elif command == "exit":
        #     print("Exiting...")
        #     break
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()
