from subscriber import Subscriber
from collections import deque
from threading import Thread
import time


class EventChannel(Thread):

    def __init__(self):
        super(EventChannel, self).__init__()
        self.events = []
        self.state = len(self.events)
        self.subscribers = []

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def publish(self, event: str):
        self.events.append(event)

    def notify(self, event):
        for subscriber in self.subscribers:
            subscriber.handleEvent(event)

    def run(self):
        while True:
            if len(self.events) != self.state:
                print("New event published!")
                self.state = len(self.events)
                self.notify(self.events[self.state - 1])


if __name__ == '__main__':
    pass
