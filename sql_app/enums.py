from enum import Enum, unique


@unique
class NotificationType(str, Enum):
    CALL = "VOICE_CALL"
    TXT_MSG = "TXT_MSG"

@unique
class DeviceType(str, Enum):
    CAMERA = "CAMERA"
    SENSOR = "SENSOR"

@unique
class DeviceState(str, Enum):
    ON = "ON"
    OFF = "OFF"
