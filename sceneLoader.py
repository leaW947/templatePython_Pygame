import assetManager
import utils
import gameplayService

import sceneGame

class SceneLoader:

    def __init__(self):
        self.gameState=""

        self.myAssetManager = None
        self.myUtils=None
        self.myGameplayService = None

        self.mySceneGame=sceneGame.SceneGame()


    def load(self,pScreen):
        self.myAssetManager=assetManager.AssetManager()
        self.myUtils=utils.Utils()
        self.myGameplayService=gameplayService.GameplayService()

        self.myGameplayService.setScreen(pScreen)
        self.myGameplayService.setUtils(self.myUtils)
        self.myGameplayService.setAssetManager(self.myAssetManager)


    def init(self,pGameState):
        self.gameState=pGameState

        if self.gameState=="menu":
            print("loadMenu")
        elif self.gameState=="gameplay":
            self.mySceneGame.load(self.myGameplayService, self)
        elif self.gameState=="gameover":
            print("loadGameover")


    def update(self,dt):

        if self.gameState == "menu":
            print("updateMenu")
        elif self.gameState == "gameplay":
            self.mySceneGame.update(dt)
        elif self.gameState == "gameover":
            print("updateGameover")


    def draw(self):

        if self.gameState == "menu":
            print("drawMenu")
        elif self.gameState == "gameplay":
            self.mySceneGame.draw()
        elif self.gameState == "gameover":
            print("drawGameover")


    def keypressed(self,pKey):

        if self.gameState == "menu":
            print("keypressedMenu")
        elif self.gameState == "gameplay":
            print("keypressedGame")
        elif self.gameState == "gameover":
            print("keypressedGameover")


    def mousepressed(self,pBtn,pPos):

        if self.gameState == "menu":
            print("mousepressedMenu")
        elif self.gameState == "gameplay":
            print("mousepressedGame")
        elif self.gameState == "gameover":
            print("mousepressedGameover")


    def mousemove(self,pPos):

        if self.gameState == "menu":
            print("mousemoveMenu")
        elif self.gameState == "gameplay":
            print("mousemoveGame")
        elif self.gameState == "gameover":
            print("movemoveGameover")