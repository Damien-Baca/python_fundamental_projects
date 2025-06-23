from state import State


class MultiPlayer(State):
    def __init__(self):
        State.__init__(self)

    def startup(self):
        print('MultiPlayer - startup')

    def cleanup(self):
        print('MultiPlayer - cleanup')

    def event_loop(self):
        print('MultiPlayer - event_loop')

    def update(self):
        print('MultiPlayer - update')
        self.draw()

    def draw(self):
        print('MultiPlayer - draw')
