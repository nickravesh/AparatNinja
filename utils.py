import sys
import time
import threading
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class LoadingAnimation:
    def __init__(self):
        # Constants
        self.LOADING_FRAMES = ["■□□□", "□■□□", "□□■□", "□□□■"]
        self.LOADING_MESSAGE = "The task is in progress, please wait..."
        self.CLEAR_MESSAGE = " " * 100  # Adjust the number of spaces as needed

        # Flags to control the loading animation
        self.loading_animation_running = False
        self.loading_thread = None

    def show_loading_animation(self, display=True, custom_message=None):
        if display:
            # If the loading animation is already running, return
            if self.loading_animation_running:
                return

            self.loading_animation_running = True

            def square_loading_animation():
                while self.loading_animation_running:
                    for frame in self.LOADING_FRAMES:
                        message = f"\r {Fore.CYAN}{Style.BRIGHT}{frame} {Fore.RESET}"
                        if custom_message:
                            message += custom_message
                        else:
                            message += self.LOADING_MESSAGE
                        sys.stdout.write(message)
                        sys.stdout.flush()
                        time.sleep(0.3)

            # Start the loading animation in a separate thread
            self.loading_thread = threading.Thread(target=square_loading_animation)
            self.loading_thread.start()
        else:
            self.loading_animation_running = False
            if self.loading_thread:
                self.loading_thread.join()  # Wait for the loading animation thread to finish
                sys.stdout.write("\r" + self.CLEAR_MESSAGE + "\r")  # Clear the loading message
                if custom_message:
                    print(custom_message, end="")  # Print a custom message if provided
                else:
                    print(" Task completed!", end="")  # Print "Task completed" as the default message

# Create an instance of the LoadingAnimation class
loading_animation = LoadingAnimation()
