class SceneGame:

    def __init__(self):
        self.gameplayService=None
        self.sceneLoader=None


    def load(self,pGameplayService,pSceneLoader):
        self.gameplayService=pGameplayService
        self.sceneLoader=pSceneLoader


    def update(self,dt):
        print("update")


    def draw(self):
        print("draw")
