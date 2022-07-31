import random

class Coin(object):
    def __init__(self):
        self.__res=random.randint(0,1)  ###Initalizes a random variable 
    
    def get_sideup(self):
        if(self.__res==0):
            return "Head"
        if(self.__res==1):
            return "Tail"
    
    def toss(self): ###Tosses the coin
        self.__res=random.randint(0,1)

