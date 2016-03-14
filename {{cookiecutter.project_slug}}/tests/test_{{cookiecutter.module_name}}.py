# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.module_name }}
----------------------------------

Tests for `{{ cookiecutter.module_name }}` module.
"""

import pytest

from {{ cookiecutter.module_name }} import {{ cookiecutter.module_name }}


@pytest.yield_fixture
def hello():
    # ...
    foo = 'hello'
    yield foo
    # ...


class Test{{ cookiecutter.module_name|capitalize }}:

    def test_000_something(self):
        pass
