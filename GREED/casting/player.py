from casting.actor import Actor

class Player(Actor):

    def __init__(self):
        self._score=0

    def score_rock(self):
        self._score -=1

    def score_gem(self):
        self._score +=1
    
    def get_score(self):
        return(self._score)
