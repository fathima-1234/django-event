# events/dispatcher.py

class Dispatcher:
    _handlers = {}

    @classmethod
    def RegisterHandler(cls, event_name, handler):
        if event_name not in cls._handlers:
            cls._handlers[event_name] = []
        cls._handlers[event_name].append(handler)

    @classmethod
    def Dispatch(cls, event_name, *args, **kwargs):
        if event_name in cls._handlers:
            for handler in cls._handlers[event_name]:
                handler(*args, **kwargs)
