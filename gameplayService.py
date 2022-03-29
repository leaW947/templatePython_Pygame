class GameplayService:

    def __init__(self):
        self.screen=None
        self.assetManager=None
        self.utils=None


    def setScreen(self,pScreen):
        self.screen=pScreen


    def setAssetManager(self,pAssetManager):
        self.assetManager=pAssetManager


    def setUtils(self,pUtils):
        self.utils=pUtils