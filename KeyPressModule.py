import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def getKey(keyName):
    ans = False
    pygame.event.pump()
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName), None)

    if myKey is not None and keyInput[myKey]:
        ans = True

    return ans

def main():
    if getKey("LEFT"):
        print("LEFT key pressed")

    if getKey("RIGHT"):
        print("RIGHT key pressed")

if __name__ == '__main__':
    init()
    while True:
        main()
        pygame.display.update()
        pygame.time.delay(100)
