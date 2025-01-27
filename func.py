import time
import random

def random_delay(start=2,end=15):
    time.sleep(random.uniform(start,end))

def human_typing(element,text):
    for char in text:
        element.send_keys(char)
        random_delay(0.1,0.3)