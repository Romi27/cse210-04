from casting.actor import Actor

class Rock(Actor):

    def __init__(self):
        pass


    def set_message(self,message):
        self._message=message;
    def get_message(self):
        return(self._message)