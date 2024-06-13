import time
import os

def love_message(name):
    heart = """
     ******       ******
   **      **   **      **
 **         ** **         **
**            **            **
**                         **
 **                       **
   **                   **
     **               **
       **           **
         **       **
           **   **
             **
    """
    message = f"I love you, {name}!"
    return heart + "\n" + message

def clear_screen():
    # Clear command for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear command for Unix/Linux/Mac
    else:
        os.system('clear')

def flash_message(name, duration=20, interval=1.5):
    end_time = time.time() + duration
    while time.time() < end_time:
        # Print the message
        print(love_message(name))
        # Wait for the interval
        time.sleep(interval)
        # Clear the screen
        clear_screen()
        # Wait for the interval
        time.sleep(interval)

# Flash the love message for Michelle for 10 seconds
flash_message("Michelle")
