import time
import datetime

def countdown():
    s = 5
    
    while s > 0:
        timer = datetime.timedelta(seconds=s)
        print(timer, end="\r")
        
        time.sleep(1)
        
        s -= 1
        
countdown()
print('Welcome to Rock Paper and Scissors!')
    
