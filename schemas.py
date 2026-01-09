from enum import Enum
from random import randint
from pydantic import BaseModel, Field

def default_destination() -> int:
    return randint(1000, 9999)

class shipmentStatus(str, Enum):
    placed = "placed"
    shipped = "shipped"
    delivered = "delivered"
    in_transit = "in transit"
    returned = "returned"
    processing = "processing"


class Shipment(BaseModel):
    content: str = Field(max_length=30)
    weight: float = Field(description="Weight in kg", le=25, ge=1)
    destination: int | None = Field(description="Destination ZIP code", default_factory=default_destination)
    status: shipmentStatus