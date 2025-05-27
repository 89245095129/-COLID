# Задача 5. Принцип инверсии зависимостей (DIP)
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def notify(self, recipient, message):
        pass


class EmailNotifier(Notifier):
    def notify(self, recipient, message):
        print(f"Отправка email для {recipient}: {message}")


class SMSNotifier(Notifier):
    def notify(self, recipient, message):
        print(f"Отправка SMS на номер {recipient}: {message}")


class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier
    
    def notify_user(self, user, message):
        recipient = user.email if isinstance(self.notifier, EmailNotifier) else user.phone
        self.notifier.notify(recipient, message)