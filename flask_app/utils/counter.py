from typing import Callable
from redis import Redis
import functools


class HitCounter:
    """Redis value wrapper for incrementing view counts."""

    def __init__(self, redis: Redis, view: Callable):
        self.redis = redis
        self.view = view.__name__

    def increment(self) -> int:
        """Increment and return view count for :self.view:"""

        incremented = self.value() + 1
        self.redis.set(self.view, incremented)
        return incremented

    def value(self) -> int:
        """Increment and return view count for :self.view:"""

        return int(self.redis.get(self.view) or 0)


def hit_counted(redis):
    """Decorator for wrapping view with view count tracking.

    >>> @app.route('/hit-me')
    >>> @hit_counted(redis)
    >>> def hit_me(view_count):
    >>>     return f"I have been hit {view_count} times."
    """

    def wrapper(f):
        counter = HitCounter(redis, f)

        @functools.wraps(f)
        def wrapped():
            return f(counter.increment())

        return wrapped

    return wrapper
