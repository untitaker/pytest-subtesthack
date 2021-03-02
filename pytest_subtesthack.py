import pytest

from _pytest.python import Function

@pytest.fixture
def subtest(request):
    parent_test = request.node
    def inner(func):
        if hasattr(Function, "from_parent"):
            item = Function.from_parent(
                parent_test,
                name=request.function.__name__ + '[]',
                originalname=request.function.__name__,
                callobj=func,
            )
        else:
            item = Function(
                name=request.function.__name__ + '[]',
                parent=parent_test,
                callobj=func
            )
        nextitem = parent_test  # prevents pytest from tearing down module fixtures

        item.ihook.pytest_runtest_setup(item=item)
        item.ihook.pytest_runtest_call(item=item)
        item.ihook.pytest_runtest_teardown(item=item, nextitem=nextitem)



    return inner
