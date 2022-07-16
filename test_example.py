import pytest

from hypothesis import given, settings, HealthCheck
from hypothesis.strategies import text

pytest_plugins = ["pytester"]

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


try:
    test_foo = settings(suppress_health_check=[HealthCheck.function_scoped_fixture])(test_foo)  # type: ignore
except AttributeError:
    pass


def test_failure(pytester):
    """Make sure test failures do not crash pytest."""

    pytester.makepyfile(
        """
        import pytest

        from hypothesis import given, settings, HealthCheck
        from hypothesis.strategies import text

        @pytest.fixture(scope='function')
        def thing():
            return object()

        @given(s=text())
        @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
        def test_foo(subtest, s):
            @subtest
            def test_inner(thing):
                assert s, "the string is empty"
    """
    )

    result = pytester.runpytest()

    result.assert_outcomes(failed=1)
    result.stdout.fnmatch_lines(["FAILED test_failure.py::test_foo - AssertionError: the string is empty"])
