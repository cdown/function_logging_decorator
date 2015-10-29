from logdecorator import log_when_called
import testfixtures
import logging
from hypothesis import given
import hypothesis.strategies as st

LOGGER_NAME = 'hunter2'
log = logging.getLogger(LOGGER_NAME)


ALL_SORTS_ITEMS = (
    st.integers(), st.text(), st.floats(), st.booleans(), st.complex_numbers(),
    st.tuples(), st.fractions(), st.decimals(),
)
ALL_SORTS = st.tuples(st.recursive(st.one_of(*ALL_SORTS_ITEMS), st.lists))


@log_when_called(log)
def example_func(*args, **kwargs):
    pass


@given(ALL_SORTS)
def test_basic_log(args):
    with testfixtures.LogCapture() as logs:
        example_func(args)

    logs.check(
        (
            LOGGER_NAME, 'DEBUG',
            "Calling example_func(%r)" % (args,),
        )
    )
