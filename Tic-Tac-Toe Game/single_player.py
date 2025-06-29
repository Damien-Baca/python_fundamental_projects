

class SinglePlayer:
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

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
