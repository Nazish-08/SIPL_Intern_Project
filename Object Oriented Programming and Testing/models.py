from dataclasses import dataclass

@dataclass
class VehicleEvent:
    vehicle: str
    gate: str
    tat: int


@dataclass
class DetectionResult:
    vehicle: str
    detected: bool
    confidence: float