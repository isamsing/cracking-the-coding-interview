from threading import Thread


class Subscriber(Thread):

    def __init__(self):
        super(Subscriber, self).__init__()

    def handleEvent(self, event):
        print(event)

    def run(self) -> None:
        while True:
            pass


if __name__ == '__main__':
    pass
