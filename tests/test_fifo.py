# tests/test_fifo.py

import unittest
from algorithms.fifo import FIFOReplacement

class TestFIFO(unittest.TestCase):
    def test_fifo_replacement(self):
        fifo = FIFOReplacement(3)
        reference_string = [7, 0, 1, 2, 0, 3, 0]

        for page in reference_string:
            fifo.access_page(page)

        self.assertEqual(fifo.get_page_faults(), 6)  # Expected faults
        self.assertIn(0, fifo.frames)  # Last frame must contain 0

if __name__ == "__main__":
    unittest.main()
