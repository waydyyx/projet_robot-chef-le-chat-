class State:
    def __init__(self, st):
        self._st=st

    def change_state(self,st):
        self._st=st
    
    def start(self):
        self._st.start()

    # def __getattribute__(self, name):
    #     return getattr(self._st, name)