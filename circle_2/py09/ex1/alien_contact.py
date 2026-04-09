
from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional


class ContactType(str, Enum):

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_alien_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        if self.contact_type == ContactType.PHYSICAL:
            if self.is_verified is False:
                raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError("Telepathic contact requires at least 3 "
                                 "witnesse")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include received "
                             "messages")
        return self


def main():
    print("Alien Contact Log Validation")
    print("=" * 38)
    print("Valid contact report:")

    try:
        ValidContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-04-04T14:30:00",
            location="Area 51, Nevada",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="'Greetings form Zeta Reticuli'",
            is_verified=True
        )

        print(f"ID: {ValidContact.contact_id}")
        print(f"Type: {ValidContact.contact_type}")
        print(f"Location: {ValidContact.location}")
        print(f"Signal: {ValidContact.signal_strength}/10")
        print(f"Duration: {ValidContact.duration_minutes} minutes")
        print(f"Witnesses: {ValidContact.witness_count}")
        print(f"Message: {ValidContact.message_received}")

    except ValidationError as e:
        print(f"Error: {e}")

    print("\n" + "=" * 38)

    print("Expected validation error:")

    try:
        InvalidContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-04-04T14:30:00",
            location="Area 51, Nevada",
            contact_type="telepathic",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            is_verified=True
        )

        InvalidContact.validate_alien_rules()
    except ValidationError as e:
        print(e.errors()[0]['msg'][13:])


if __name__ == "__main__":
    main()
