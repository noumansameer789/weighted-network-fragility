import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from network_fragility.analysis import largest_component_fraction, participation_coefficient


class NetworkTest(unittest.TestCase):
    def setUp(self):
        self.graph = {
            "a": {"b": 1.0},
            "b": {"a": 1.0, "c": 1.0},
            "c": {"b": 1.0, "d": 1.0},
            "d": {"c": 1.0},
        }

    def test_attack_consequence(self):
        self.assertEqual(largest_component_fraction(self.graph), 1.0)
        self.assertAlmostEqual(largest_component_fraction(self.graph, {"b"}), 2 / 3)

    def test_participation(self):
        communities = {"a": 0, "b": 0, "c": 1, "d": 1}
        self.assertAlmostEqual(participation_coefficient(self.graph, communities, "b"), 0.5)


if __name__ == "__main__":
    unittest.main()
