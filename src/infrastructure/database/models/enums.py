from enum import Enum


class EventFormat(str, Enum):
    """Enum for event format types.

    Attributes:
        ONLINE: Online event format
        OFFLINE: Offline event format
        HYBRID: Hybrid event format

    """

    ONLINE = "online"
    OFFLINE = "offline"
    HYBRID = "hybrid"


class EventStatus(str, Enum):
    """Enum for event statuses.

    Attributes:
        PLANNED: Event is planned
        ONGOING: Event is currently ongoing
        COMPLETED: Event has been completed
        CANCELLED: Event was cancelled

    """

    PLANNED = "planned"
    ONGOING = "ongoing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Currency(str, Enum):
    """Enum for currency types.

    Attributes:
        USD: United States Dollar
        EUR: Euro
        RUB: Russian Ruble

    """

    USD = "USD"
    EUR = "EUR"
    RUB = "RUB"


class ParticipantStatus(str, Enum):
    """Enum for participant statuses.

    Attributes:
        REGISTERED: Participant is registered
        CONFIRMED: Registration is confirmed
        WAITLISTED: Participant is in waiting list
        CANCELLED: Registration was cancelled
        ATTENDED: Participant attended the event
        NO_SHOW: Participant didn't show up

    """

    REGISTERED = "registered"
    CONFIRMED = "confirmed"
    WAITLISTED = "waitlisted"
    CANCELLED = "cancelled"
    ATTENDED = "attended"
    NO_SHOW = "no_show"


class Gender(str, Enum):
    """Enum for gender types.

    Attributes:
        MALE: Male gender
        FEMALE: Female gender

    """

    MALE = "male"
    FEMALE = "female"
