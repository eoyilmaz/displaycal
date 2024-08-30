# -*- coding: utf-8 -*-
import platform
import pytest
from DisplayCAL import RealDisplaySizeMM, config
from DisplayCAL.dev.mocks import check_call
from DisplayCAL.edid import get_edid
from tests.data.display_data import DisplayData

@pytest.mark.skipif(platform.system() != "Linux", reason="This test depends on Linux. Run if Linux")
def test_device_id_from_edid_1():
    """Testing DisplayCAL.colord.device_id_from_edid() function."""
    from DisplayCAL.colord import device_id_from_edid

    with check_call(config, "getcfg", DisplayData.CFG_DATA, call_count=2):
        print("Before calling _enumerate_displays")
        with check_call(RealDisplaySizeMM, "_enumerate_displays", DisplayData.enumerate_displays()):
            print("After calling _enumerate_displays")
            print("Before calling get_edid")
            edid = get_edid(0)
            print("After calling get_edid")
            device_id = device_id_from_edid(edid)
            assert isinstance(device_id, str)
            assert device_id != ""

            # Additional debug prints
            print(f"check_call type: {type(check_call)}")
            print(f"check_call attributes: {dir(check_call)}")
            print(f"call_count: {getattr(check_call, 'call_count', 'Attribute not found')}")
