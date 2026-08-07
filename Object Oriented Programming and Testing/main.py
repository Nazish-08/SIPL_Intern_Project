from models import VehicleEvent, DetectionResult

vehicle = VehicleEvent(
    vehicle="MH12AB1234",
    gate="Gate-1",
    tat=18
)

result = DetectionResult(
    vehicle="MH12AB1234",
    detected=True,
    confidence=98.5
)

print("Vehicle Event")
print(vehicle)

print("\nDetection Result")
print(result)