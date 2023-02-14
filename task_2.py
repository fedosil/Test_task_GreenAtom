from typing import Callable, List, Iterable


def create_handlers(callback: Callable[[int], None]) -> List[Callable[[int], None]]:
    handlers = []
    for step in range(5):
        handlers.append(lambda x=step: callback(x))
    return handlers


def execute_handlers(handlers: Iterable[Callable[[], None]]) -> None:
    for handler in handlers:
        handler()
