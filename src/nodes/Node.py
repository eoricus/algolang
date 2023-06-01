"""
TODO
Общий класс для всех узлов, который появится, когда я пойму как
можно упростить их работу
"""

from typing import Any


class Node:
    def set_init_token(self, token):
        self.init_token = token


def node(cls):
    """
    Декоратор, который выполняет общий функционал
    для всех узлов.

    Пока только присваивает лексему к классу, но 
    мне кажется что позже я найду чуть больше способов
    использования декоратора
    """

    def decorator(func):
        def wrapper(self, *args, **kwargs):
            init_token = self.token.current
            instance = func(self, *args, **kwargs)
            print(init_token)
            instance.set_init_token(init_token)
            return instance
        return wrapper

    return decorator(cls)
