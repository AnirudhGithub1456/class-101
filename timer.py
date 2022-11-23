import time
seconds = int(input("How long do you want the timer to go for?"))

def timer(seconds):
    while seconds > 0:
        minutes = int(seconds/60)
        secs = int(seconds%60)
        timer = f'{minutes}:{secs}'
        print(timer)
        seconds = seconds - 1
    print("time up!")

timer(seconds)