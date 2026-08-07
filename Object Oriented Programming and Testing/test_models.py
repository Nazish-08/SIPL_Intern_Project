from models import VehicleEvent, DetectionResult


def test_vehicle_event_creation():
    vehicle = VehicleEvent("MH12AB1234", "Gate-1", 18)
    assert vehicle.vehicle == "MH12AB1234"


def test_vehicle_gate():
    vehicle = VehicleEvent("MH12AB1234", "Gate-1", 18)
    assert vehicle.gate == "Gate-1"


def test_vehicle_tat():
    vehicle = VehicleEvent("MH12AB1234", "Gate-1", 18)
    assert vehicle.tat == 18


def test_detection_result():
    result = DetectionResult("MH12AB1234", True, 98.5)
    assert result.detected is True


def test_detection_confidence():
    result = DetectionResult("MH12AB1234", True, 98.5)
    assert result.confidence == 98.5


def test_invalid_vehicle():
    vehicle = VehicleEvent("", "Gate-1", 18)
    assert vehicle.vehicle == ""