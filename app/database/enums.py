from enum import Enum

class IncedentStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"


class IncedentSource(str, Enum):
    OPERATOR = "operator"
    MONITORING = "monitoring"
    PARTNER = "partner"