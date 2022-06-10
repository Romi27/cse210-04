from casting.actor import Actor


FRAME_RATE=12
MAX_X=900
MAX_Y=600
CELL_SIZE=15
FONT_SIZE=15
COLS=60
ROWS=40

class Gem(Actor):
    def __init__(self):
        pass

    def set_message(self,message):
        self._message=message;

    def get_message(self):
        return(self._message)