# test_beatdrift.py
"""
Tests for BeatDrift module.
"""

import unittest
from beatdrift import BeatDrift

class TestBeatDrift(unittest.TestCase):
    """Test cases for BeatDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BeatDrift()
        self.assertIsInstance(instance, BeatDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BeatDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
