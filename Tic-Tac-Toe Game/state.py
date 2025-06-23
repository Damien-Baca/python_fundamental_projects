import abc


class State(abc.ABC):
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

    @abc.abstractmethod
    def startup(self):
        pass

    @abc.abstractmethod
    def cleanup(self):
        pass

    @abc.abstractmethod
    def event_loop(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass
