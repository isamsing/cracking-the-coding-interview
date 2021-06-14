from eventChannel import EventChannel
from publisher import Publisher
from subscriber import Subscriber

if __name__ == '__main__':
    eventChannel = EventChannel()
    producer = Publisher(eventChannel)
    subscriber = Subscriber()
    eventChannel.subscribe(subscriber)

    producer.start()
    subscriber.start()
    eventChannel.start()
