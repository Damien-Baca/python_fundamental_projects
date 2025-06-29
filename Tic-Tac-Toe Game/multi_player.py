
class MultiPlayer:
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

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
