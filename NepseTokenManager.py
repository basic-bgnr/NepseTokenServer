from NepseTokenLib import NepseToken
from threading import Semaphore, Thread 
import time

class NepseTokenManager:
    def __init__(self):
        self.nepse_token = NepseToken()
        self.token = None
        self.semaphore = Semaphore()
        self.freq = 15 # secs

        token_update_thread = Thread(target=self.update)
        token_update_thread.start()

    def update(self):
        while True:
            self.semaphore.acquire()
            # print('updating ......')
            self.token = self.nepse_token.getValidToken()
            # print('update complete.')
            self.semaphore.release()
            time.sleep(self.freq)
    
    def getValidToken(self):
        return self.token