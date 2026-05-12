# test_supabasedb.py
"""
Tests for SupabaseDB module.
"""

import unittest
from supabasedb import SupabaseDB

class TestSupabaseDB(unittest.TestCase):
    """Test cases for SupabaseDB class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SupabaseDB()
        self.assertIsInstance(instance, SupabaseDB)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SupabaseDB()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
