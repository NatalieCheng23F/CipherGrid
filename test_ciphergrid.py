# test_ciphergrid.py
"""
Tests for CipherGrid module.
"""

import unittest
from ciphergrid import CipherGrid

class TestCipherGrid(unittest.TestCase):
    """Test cases for CipherGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CipherGrid()
        self.assertIsInstance(instance, CipherGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CipherGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
