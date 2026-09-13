from datetime import datetime, timezone
import pytest
from pydantic import ValidationError
from contracts.telemetry import Telemetry

def example():
    return dict(node_id='PG-A',zone_id='A',boot_id='simulation-1',sequence=1,captured_at='2026-09-12T10:00:00Z',source_type='simulated',measurements={'relative_humidity_pct':65},firmware_version='sim-0.1')

def test_missing_measurement_stays_missing():
    value=Telemetry.model_validate(example())
    assert value.measurements.air_temperature_c is None
    assert value.source_type=='simulated'

@pytest.mark.parametrize('change',[{'zone_id':'B'},{'source_type':'realish'},{'captured_at':'2026-09-12T10:00:00'},{'sequence':-1},{'sequence':1.2},{'measurements':{'relative_humidity_pct':101}},{'measurements':{'soil_moisture_relative_pct':50}},{'measurements':{'light_lux':float('nan')}}])
def test_reject_invalid_telemetry(change):
    payload=example();payload.update(change)
    with pytest.raises(ValidationError):Telemetry.model_validate(payload)

def test_calibrated_moisture_accepted():
    payload=example();payload.update(calibration_id='substrate-A-v1',measurements={'soil_moisture_raw_adc':1234,'soil_moisture_relative_pct':45})
    assert Telemetry.model_validate(payload).measurements.soil_moisture_relative_pct==45
