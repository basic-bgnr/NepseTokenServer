from NepseTokenLib import NepseToken
from threading import Semaphore, Thread 
import time
from requests.exceptions import RequestException
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
            # self.semaphore.acquire()
            # print('updating ......')
            try:
                self.token = self.nepse_token.getValidToken()
                time.sleep(self.freq)
            except:
                continue
            # print('update complete.')
            # self.semaphore.release()
            
    
    def getValidToken(self):
        return "Server not Initialized" if self.token is None else self.token