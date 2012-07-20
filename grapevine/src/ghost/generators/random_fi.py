from common.fuzzgenerator.gvgenerator import Generator
import random
import binascii

class RandomFI(Generator):
    profile = None
    state = None
    seed = None
    
    def __init__(self, profile, seed):
        pass

    def getNext(self):
        args = []
        for _ in range(0,8):
            args.append(self.__getarg())
        return args

    def affectState(self, data):
        print data

    def __getrand(self):
        random_file = open('/dev/urandom', 'r')
        data = random_file.read(128).rstrip()
        random_file.close()
        return data

    def __getnumber(self):
        state = random.randrange(0,5)
        if state == 0:
            random.seed(1)
            return random.randrange(2147483647)
        elif state == 1:
            random.seed(1)
            # C-like random
            return (0xffffff00 | (random.randrange(2147483647) % 256)) 
        elif state == 2:
            return 0x8000
        elif state == 3:
            return 0xffff
        elif state == 4:
            return 0x80000000

    def __getarg(self):
           state = random.randrange(0,5)
           if state == 0:
               return 0x0804fd00 #userland addr
           elif state == 1:
              return 0x0000a000 #unmapped addr
           elif state == 2:
              return 0xc01fa0b6 #kernel addr, a guess
           elif state == 3:
              return self.__getnumber() #some number
           elif state == 4:
              return self.__getrand()



