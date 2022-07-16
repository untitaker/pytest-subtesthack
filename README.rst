==================
pytest-subtesthack
==================

A hack to explicitly set up and tear down fixtures.

This terrible plugin allows you to set up and tear down fixtures *within* the
test function itself. This is useful (necessary!) for using `Hypothesis
<https://github.com/DRMacIver/hypothesis>`_ inside py.test, as hypothesis will
call the test function multiple times, without setting up or tearing down
fixture state as is normally the case.

Installation::

    pip install pytest-subtesthack

...though the plugin is 32 lines of code, consider vendoring it.

See ``test_example.py`` for usage.
