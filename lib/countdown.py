# your code goes here!
import time

def countdown(x):
    while x > 0:
        print(f"{x} SECOND(S)!")
        x -= 1
    print("HAPPY NEW YEAR!")

countdown(10)

def countdown_with_sleep(y):
    while y > 0:
        print(f"{y} SECOND(S)!")
        time.sleep(1)
        y -= 1
        
    print("HAPPY NEW YEAR!")

countdown_with_sleep(5)