from sources.traducteur.state import State

class Control:
    def __init__(self,state):
        self.state=state

    def start(self):
        self.state.start()
