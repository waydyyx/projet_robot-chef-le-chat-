class Sequence:
    def __init__(self, seq):
        self.strats = seq
        self.cur = -1

    def start(self):
        self.cur = -1

    def step(self):
        if self.stop(): return
        if self.cur < 0 or self.strats[self.cur].stop():
            self.cur += 1
            self.strats[self.cur].start()
        self.strats[self.cur].step()

    def stop(self):
        return self.cur == len(self.strats) - 1 and self.strats[self.cur].stop()
    

class Strat_while:
    def __init__(self,strat,condition):
        self.strat = strat
        self.cond=condition

    def start(self):
        self.strat.start()

    def step(self):
        self.strat.step()

    def stop(self):
        return self.cond()
    
class Strat_for:
    def __init__(self, strat, n):
        self.max=n
        self.curr=0
        self.strat=strat

    def start(self):
        self.curr=0

    def step(self):
        if self.strat.stop():
            self.curr+=1
            self.strat.start()
        self.strat.step()

    def stop(self):
        return self.curr>=self.max
        

class Strat_if:
    def __init__(self, strat1, strat2, cond, ):
        self.strat1=strat1
        self.strat2=strat2
        self.cond=cond

    def start(self):
        self.strat1.start()
        self.strat2.start()

    def step(self):
        if self.cond():
            self.strat1.step()
        else:
            self.strat2.step()

    def stop(self):
        return (self.strat1.stop()or self.strat2.stop())
