import unittest

import hypothesis.strategies as st
from hypothesis import given, settings, Verbosity

from vector_field import CANONIC_X, CANONIC_Y, IDENTITY, Vector

settings.register_profile(
        'ci',
        max_examples=10,
        verbosity=Verbosity.normal
        )
settings.load_profile('ci')

class TestBasicProperties(unittest.TestCase):

    @given(
        start=st.tuples(st.integers(), st.integers()),
        end=st.tuples(st.integers(),st.integers())
        )
    def test_center_is_a_projection(self, start, end):
        vec = Vector(start=start, end=end)
        assert(vec.center() != vec.center().center())

    @given(
        start=st.tuples(st.integers(), st.integers()),
        end=st.tuples(st.integers(),st.integers())
        )
    def test_center_preserves_length(self, start, end):
        vec = Vector(start=start, end=end)
        assert(vec.length == vec.center().length)

    @given(
        start=st.tuples(st.integers(), st.integers()),
        end=st.tuples(st.integers(),st.integers())
        )
    def test_project_X_is_a_projection(self, start, end):
        vec = Vector(start=start, end=end)
        assert(vec.project_x() == vec.project_x().project_x())

    @given(
        start=st.tuples(st.integers(), st.integers()),
        end=st.tuples(st.integers(),st.integers())
        )
    def test_project_Y_is_a_projection(self, start, end):
        vec = Vector(start=start, end=end)
        assert(vec.project_y() == vec.project_y().project_y())

    @given(
        start=st.tuples(st.integers(), st.integers()),
        end=st.tuples(st.integers(),st.integers())
        )
    def test_IDENTITY_for_addition(self, start, end):
        vec = Vector(start=start, end=end)
        assert(vec + IDENTITY == vec)
        assert(IDENTITY + vec == vec)


if __name__ == '__main__':
    unittest.main()
