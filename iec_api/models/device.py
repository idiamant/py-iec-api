from dataclasses import dataclass, field

from mashumaro import DataClassDictMixin, field_options

from iec_api.models.response_descriptor import ResponseDescriptor

#
# GET https://iecapi.iec.co.il//api/Device/{bp_number}
#
# [
#     {
#         "isActive": true,
#         "deviceType": 3,
#         "deviceNumber": "23231111",
#         "deviceCode": "503"
#     }
#
# -----------
# GET https://iecapi.iec.co.il//api/Device/{bp_number}/{contract_id}
# {
#     "data": {
#         "counterDevices": [
#             {
#                 "device": "00000000002000111",
#                 "register": "001",
#                 "lastMR": "00000000000011111",
#                 "lastMRDate": "2024-01-11",
#                 "lastMRType": "01",
#                 "lastMRTypeDesc": "קריאת מונה לפי שגרות מערכת",
#                 "connectionSize": {
#                     "size": 25,
#                     "phase": 3,
#                     "representativeConnectionSize": "3X20"
#                 }
#             }
#         ],
#         "mrType": "01"
#     },
#     "reponseDescriptor": {
#         "isSuccess": true,
#         "code": "00",
#         "description": null
#     }
# }


@dataclass
class Device(DataClassDictMixin):
    """Device dataclass."""

    device_type: int | None = field(metadata=field_options(alias="deviceType"))
    device_number: str | None = field(metadata=field_options(alias="deviceNumber"))
    device_code: str | None = field(metadata=field_options(alias="deviceCode"))
    is_active: bool = field(metadata=field_options(alias="isActive"))


@dataclass
class ConnectionSize(DataClassDictMixin):
    """Connection dataclass."""
    size: int = field(metadata=field_options(alias="size"))
    phase: str = field(metadata=field_options(alias="phase"))
    representative_connection_size: str = field(metadata=field_options(alias="representativeConnectionSize"))


@dataclass
class CounterDevice(DataClassDictMixin):
    """Counter Device dataclass."""
    device: str = field(metadata=field_options(alias="device"))
    register: str = field(metadata=field_options(alias="register"))
    last_mr: str = field(metadata=field_options(alias="lastMR"))
    last_mr_date: str = field(metadata=field_options(alias="lastMRDate"))
    last_mr_type: str = field(metadata=field_options(alias="lastMRType"))
    last_mr_type_desc: str = field(metadata=field_options(alias="lastMRTypeDesc"))
    connection_size: ConnectionSize = field(metadata=field_options(alias="connectionSize"))


@dataclass
class Devices(DataClassDictMixin):
    """Devices dataclass."""
    counter_devices: list[CounterDevice] | None = field(metadata=field_options(alias="counterDevices"))
    mr_type: str = field(metadata=field_options(alias="mrType"))


@dataclass
class GetDeviceResponse(DataClassDictMixin):
    """Get Device Response dataclass."""
    data: Devices
    response_descriptor: ResponseDescriptor = field(metadata=field_options(alias="reponseDescriptor"))
