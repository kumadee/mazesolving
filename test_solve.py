import unittest
import tempfile

from solve import solve
from factory import SolverFactory

class TestMaze(unittest.TestCase):
    def test_default(self):
        sf = SolverFactory()
        solve(sf, sf.Default, "examples/normal.png", tempfile.mkstemp())
