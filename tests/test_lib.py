#!/usr/bin/env python
import pytest
import ssdeep


class TestFunctionsFail(object):
    def test_compare(self):
        with pytest.raises(TypeError):
            ssdeep.compare(
                "3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C",
                None
            )

        with pytest.raises(TypeError):
            ssdeep.compare(
                None,
                "3:AXGBicFlIHBGcL6wCrFQEv:AXGH6xLsr2C"
            )

        with pytest.raises(ssdeep.BaseError):
            ssdeep.compare(
                "3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C",
                ""
            )


class TestFunctions(object):
    def test_compare(self):
        res = ssdeep.compare(
            "3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C",
            "3:AXGBicFlIHBGcL6wCrFQEv:AXGH6xLsr2C"
        )
        assert res == 22

        res = ssdeep.compare(
            b"3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C",
            b"3:AXGBicFlIHBGcL6wCrFQEv:AXGH6xLsr2C"
        )
        assert res == 22

    def test_hash_1(self):
        res = ssdeep.hash("Also called fuzzy hashes, Ctph can match inputs that have homologies.")
        assert res == "3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C"

    def test_hash_2(self):
        res = ssdeep.hash("Also called fuzzy hashes, CTPH can match inputs that have homologies.")
        assert res == "3:AXGBicFlIHBGcL6wCrFQEv:AXGH6xLsr2C"

    def test_hash_from_file(self):
        with pytest.raises(IOError):
            ssdeep.hash_from_file("tests/files/")

        with pytest.raises(IOError):
            ssdeep.hash_from_file("tests/files/file-does-not-exist.txt")

        res = ssdeep.hash_from_file("tests/files/file.txt")
        assert res == "3:AXGBicFlgVNhBGcL6wCrFQE3:AXGHsNhxLsr2s"


class TestHashClass(object):
    def test_update(self):
        obj = ssdeep.Hash()
        obj.update("Also called fuzzy hashes, Ctph can match inputs that have homologies.")
        res = obj.digest()

        assert res == "3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C"
