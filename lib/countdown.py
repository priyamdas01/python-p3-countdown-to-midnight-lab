# your code goes here!
import time
def countdown(argues):
    args = argues
    while args >= 0:
        if args == 0:
            print("HAPPY NEW YEAR!")
        else:
            print(f"{args} SECOND(S)!")
        args -= 1

def countdown_with_sleep(argues):
    args = argues
    while args >= 0:
        if args == 0:
            print("HAPPY NEW YEAR!")
        else:
            print(f"{args} SECOND(S)!")
        time.sleep(1)
        args -= 1