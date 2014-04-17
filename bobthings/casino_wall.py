__author__ = 'Yiqiu'

import random, threading, time

class CasinoWall(threading.Thread):
    def __init__(self, threadId):

        self.iThreadsId = threadId
        self.threadsName = "Desk-"+str(self.iThreadsId)
        threading.Thread.__init__( self, name = self.threadsName )

        self.number_of_players = 0

    def run( self ):
        tray = []
        card_no = 13*32
        for i in range(card_no):
            while True:
                card = random.randint(1, 10)
                noc = tray.count(card)

                if card < 10:
                    if noc < 32:
                        break
                else:
                    if noc < 128:
                        break

            tray.append(card)

        while True:
            if self.number_of_players == 0:
                time.sleep(1)
                continue