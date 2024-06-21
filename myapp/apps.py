# myapp/apps.py
from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        from events.dispatcher import Dispatcher
        from myapp.handlers import user_logged_in_handler
        Dispatcher.RegisterHandler('event::user::logged_in', user_logged_in_handler)



