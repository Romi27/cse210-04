class Velocity:

    def __init__(self, dx, dy):

        self._dx = dx
        self._dy = dy

    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy

    def set_dx(self, dx):
        self._dx = dx

    def set_dy(self, dy):
        self._dy = dy

    def scale(self, factor):

        return Velocity(self._dx*factor, self._dy * factor)
