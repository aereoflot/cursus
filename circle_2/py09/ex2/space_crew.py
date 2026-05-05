
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from typing import List


class Rank(str, Enum):

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validation_rules(self) -> "SpaceMission":
        if self.mission_id[0] != 'M':
            raise ValueError("Mission id must start with: 'M'")
        leather = False
        for member in self.crew:
            if member.rank == Rank.CAPTAIN:
                leather = True
            elif member.rank == Rank.COMMANDER:
                leather = True
        if not leather:
            raise ValueError("Mission must have at least one "
                             "Commander or Captain")
        veterans = 0
        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience > 5:
                    veterans += 1
            half = len(self.crew) // 2
            if veterans < half:
                raise ValueError("50% must have 5+ years of experience")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)
    print("Valid mission created:")

    try:
        member1 = CrewMember(
            member_id="A001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=45,
            specialization="Mission Command",
            years_experience=20,
            is_active=True
        )

        member2 = CrewMember(
            member_id="A002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=32,
            specialization="Navigation",
            years_experience=8,
            is_active=True
        )

        member3 = CrewMember(
            member_id="A003",
            name="ALice Johnson",
            rank=Rank.OFFICER,
            age=28,
            specialization="Engineering",
            years_experience=5,
            is_active=True
        )

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 4, 7),
            duration_days=900,
            crew=[member1, member2, member3],
            mission_status="planned",
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(f"Error: {e}")

    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")

    print("\n" + "=" * 41)
    print("Expected validation error:")

    try:
        invalid_member1 = CrewMember(
            member_id="B001",
            name="Tom Hardy",
            rank=Rank.CADET,
            age=25,
            specialization="Training",
            years_experience=1,
            is_active=True
        )

        invalid_member2 = CrewMember(
            member_id="B002",
            name="Emma Watson",
            rank=Rank.OFFICER,
            age=30,
            specialization="Operations",
            years_experience=4,
            is_active=True
        )

        invalid_mission = SpaceMission(
            mission_id="M2025_VENUS",
            mission_name="Venus Survey",
            destination="Venus",
            launch_date=datetime(2026, 5, 15),
            duration_days=200,
            crew=[invalid_member1, invalid_member2],
            mission_status="planned",
            budget_millions=500.0
        )

        if invalid_mission:
            print("All good")

    except ValidationError as e:
        print(e.errors()[0]['msg'][13:])


if __name__ == "__main__":
    main()
