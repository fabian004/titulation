from sleep_mode import sleepMode
from active_mode import activeMode
import time
def internalFunction(mode):
    while True:
        time.sleep(1)
        status = mode.status()
        if(status==True):
            sleepMode(mode)
        else:
            activeMode(mode)
    