from eventChannel import EventChannel
from threading import Thread


class Publisher(Thread):

    def __init__(self, eventChannel: EventChannel):
        super(Publisher, self).__init__()
        self.eventChannel = eventChannel

    def run(self):
        while True:
            event = input("Enter a message!\n")
            self.eventChannel.publish(event)

