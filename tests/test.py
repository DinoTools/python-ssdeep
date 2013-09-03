#!/usr/bin/env python

import unittest

import ssdeep

class FunctionTest(unittest.TestCase):
    def testClassHash(self):
        obj = ssdeep.Hash()
        obj.update("Also called fuzzy hashes, Ctph can match inputs that have homologies.")
        self.assertEqual(
            obj.digest(),
            "3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C"
        )

    def testComputeHash(self):
        self.assertEqual(
            ssdeep.hash("Also called fuzzy hashes, Ctph can match inputs that have homologies."),
            "3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C"
        )

        self.assertEqual(
            ssdeep.hash("Also called fuzzy hashes, CTPH can match inputs that have homologies."),
            "3:AXGBicFlIHBGcL6wCrFQEv:AXGH6xLsr2C"
        )

    def testCompareHash(self):
        self.assertEqual(
            ssdeep.compare(
                "3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C",
                "3:AXGBicFlIHBGcL6wCrFQEv:AXGH6xLsr2C"
            ),
            22
        )

    def testComputeHashFromFile(self):
        self.assertEqual(
            ssdeep.hash_from_file("test-file.txt"),
            "3:AXGBicFlgVNhBGcL6wCrFQE3:AXGHsNhxLsr2s"
        )

if __name__ == "__main__":
    unittest.main()
