# tests/test_memory_manager.py

import unittest
from memory.memory_manager import MemoryManager

class TestMemoryManager(unittest.TestCase):
    def test_memory_load_and_remove(self):
        mm = MemoryManager(3)
        mm.load_page(1, 0)
        mm.load_page(2, 1)

        self.assertTrue(mm.is_page_in_memory(1))
        self.assertTrue(mm.is_page_in_memory(2))

        mm.remove_page(1)
        self.assertFalse(mm.is_page_in_memory(1))

if __name__ == "__main__":
    unittest.main()
