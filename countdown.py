import time

# countdown timer to kickoff the game 
def countdown_time():
    secs = 5
    while secs:
        timer = '{:01d}'.format(secs)
        print(timer, end='\r')
        time.sleep(1)
        secs -= 1 

def countdown_match():
    secs = 3
    while secs:
        timer = '{:01d}'.format(secs)
        print(timer, end='\r')
        time.sleep(1)
        secs -= 1 
    
