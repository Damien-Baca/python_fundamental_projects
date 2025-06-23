from state import State

WHITE = (255, 255, 255)


class Menu(State):
    def __init__(self):
        State.__init__(self)

    def startup(self):
        print('Menu - startup')

    def cleanup(self):
        print('Menu - cleanup')

    def event_loop(self):
        print('Menu - event_loop')

    def update(self, screen, dt):
        print('Menu - update')
        self.draw(screen)

    def draw(self, screen):
        print('Menu - draw')
        screen.fill(WHITE)
