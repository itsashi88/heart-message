import time
import sys

def print_heart():
    heart = """
     ***     ***
   *     * *     *
  *       *       *
  *               *
   *             *
     *         *
       *     *
         *
    """
    return heart

def display_message():
    heart_message = "I love you! ❤ and i will forever and ever be on ur side. you don't have to worry about a thing ajay, ur my everything️"
    heart_art = print_heart()
    
    sys.stdout.write(heart_art + "\n")
    sys.stdout.write(heart_message + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    display_message()
    time.sleep(10)  # Keep the message displayed for 10 seconds
