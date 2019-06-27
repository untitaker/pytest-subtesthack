import pytest

from hypothesis import given
from hypothesis.strategies import text

@pytest.fixture(scope='module')
def thing():
    return object()

@given(s=text())
def test_foo(thing, subtest, s):
    outer_thing = thing
    @subtest
    def test_inner(tmpdir, thing):
        # A fresh tmpdir is created for each run of `test_inner`. This is not
        # the case if the tmpdir fixture is required in `test_foo`, in that
        # case test state would be leaked.

        # The `thing` fixture is module-level, and is only set up once.

        assert thing is outer_thing
        assert not tmpdir.listdir()
        tmpdir.join('lol').write(repr(s))

