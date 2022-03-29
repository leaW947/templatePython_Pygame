import pygame

class AssetManager:

    def __init__(self):
        self.lstImages={}
        self.lstSounds=[]


    def addImages(self,pPath):
        img=pygame.image.load(pPath)
        self.lstImages[pPath]=img


    def addSounds(self,pPath):
        self.lstSounds.append(pPath)


    def getImages(self,pPath):
        return self.lstImages[pPath]


    def getSounds(self,pPath):

        for snd in self.lstSounds:
            if pPath==snd:
                return pygame.mixer.music.load(snd)