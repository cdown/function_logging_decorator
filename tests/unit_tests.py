from logdecorator import log_when_called
import testfixtures
import logging

LOGGER_NAME = 'hunter2'
log = logging.getLogger(LOGGER_NAME)


@log_when_called(log)
def example_func(*args, **kwargs):
    pass


def test_basic_log():
    with testfixtures.LogCapture() as logs:
        example_func('a', 1, ['x'])

    logs.check(
        (
            LOGGER_NAME, 'DEBUG',
            "Calling example_func('a', 1, ['x'])",
        )
    )
