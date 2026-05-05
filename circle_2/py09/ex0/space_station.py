
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    """Model for validating space station data with Pydantic."""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:

    print("Space Station Data Validation")
    print("=" * 40)

    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 4, 4, 14, 30, 00),
            is_operational=True,
            notes="Routine maintenance completed successfully"
        )

        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")

        if valid_station.is_operational:
            status = "Operational"
        else:
            "Not Operational"
        print(f"Status: {status}")

    except ValidationError as e:
        print(f"Error: {e}")

    print("\n" + "=" * 40)

    try:
        Invalid_station = SpaceStation(
            station_id="ISS002",
            name="Lunar Base Alpha",
            crew_size=22,
            power_level=75.0,
            oxygen_level=88.5,
            last_maintenance=datetime(2024, 4, 4, 14, 30, 00)
        )

        if Invalid_station:
            print("All good")

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"{error['msg']}")


if __name__ == "__main__":
    main()
