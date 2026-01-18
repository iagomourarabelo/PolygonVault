# test_polygonvault.py
"""
Tests for PolygonVault module.
"""

import unittest
from polygonvault import PolygonVault

class TestPolygonVault(unittest.TestCase):
    """Test cases for PolygonVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PolygonVault()
        self.assertIsInstance(instance, PolygonVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PolygonVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
