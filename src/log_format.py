import datetime
from uuid import uuid4

class LogFormat:
    event_id: uuid4
    timestamp: datetime
    event_type: str