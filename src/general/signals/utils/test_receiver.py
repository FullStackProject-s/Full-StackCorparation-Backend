import functools

from django.conf import settings
from django.dispatch import receiver


def suspending_receiver(signal, **decorator_kwargs):
    def our_wrapper(func):
        @receiver(signal, **decorator_kwargs)
        @functools.wraps(func)
        def fake_receiver(sender, **kwargs):
            if not hasattr(settings, 'SUSPEND_SIGNALS'):
                return func(sender, **kwargs)
            if settings.SUSPEND_SIGNALS:
                return
            return func(sender, **kwargs)

        return fake_receiver

    return our_wrapper
