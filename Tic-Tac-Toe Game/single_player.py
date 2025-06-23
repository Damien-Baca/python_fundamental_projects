from state import State


class SinglePlayer(State):
    def __init__(self):
        State.__init__(self)

    def startup(self):
        print('SinglePlayer - startup')

    def cleanup(self):
        print('SinglePlayer - cleanup')

    def event_loop(self):
        print('SinglePlayer - event_loop')

    def update(self):
        print('SinglePlayer - update')
        self.draw()

    def draw(self):
        print('SinglePlayer - draw')
