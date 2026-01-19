from enum import Enum
from pydantic import BaseModel, Field

class shipmentStatus(str, Enum):
    placed = "placed"
    shipped = "shipped"
    delivered = "delivered"
    in_transit = "in transit"
    returned = "returned"
    processing = "processing"

class BaseShipment(BaseModel):
    content: str = Field(max_length=30)
    weight: float = Field(description="Weight in kg", le=25, ge=1)
    destination: int | None = Field(description="Destination ZIP code")

class ShipmentRead(BaseShipment):
    status: shipmentStatus

class ShipmentCreate(BaseShipment):
    pass

class ShipmentUpdate(BaseModel):
    content: str | None = Field(max_length=30, default=None)
    weight: float | None = Field(description="Weight in kg", le=25, ge=1, default=None)
    destination: int | None = Field(description="Destination ZIP code", default=None)
    status: shipmentStatus