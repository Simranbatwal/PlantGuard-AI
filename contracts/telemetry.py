"""PlantGuard v1 telemetry contract. No sensor values are manufactured by validation."""
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, AwareDatetime, model_validator
class Measurements(BaseModel):
    model_config = ConfigDict(extra='forbid', allow_inf_nan=False)
    air_temperature_c: float | None = Field(default=None, ge=-40, le=125)
    relative_humidity_pct: float | None = Field(default=None, ge=0, le=100)
    soil_moisture_raw_adc: int | None = Field(default=None, ge=0, le=4095)
    soil_moisture_relative_pct: float | None = Field(default=None, ge=0, le=100)
    leaf_wetness_raw: float | None = None
    leaf_wetness_state: Literal['wet','dry','unknown'] = 'unknown'
    light_lux: float | None = Field(default=None, ge=0)
class Telemetry(BaseModel):
    model_config = ConfigDict(extra='forbid')
    schema_version: Literal['1.0'] = '1.0'
    node_id: Literal['PG-A','PG-B']
    zone_id: Literal['A','B']
    boot_id: str = Field(min_length=1,max_length=64)
    sequence: int = Field(ge=0,strict=True)
    captured_at: AwareDatetime
    source_type: Literal['physical','simulated','replay']
    measurements: Measurements
    calibration_id: str | None = None
    firmware_version: str = Field(min_length=1,max_length=64)
    @model_validator(mode='after')
    def check_binding(self):
        if self.node_id != 'PG-'+self.zone_id: raise ValueError('Node and zone mapping mismatch')
        if self.measurements.soil_moisture_relative_pct is not None and not self.calibration_id:
            raise ValueError('Relative soil moisture requires a calibration ID')
        return self
