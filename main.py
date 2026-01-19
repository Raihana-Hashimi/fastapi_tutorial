from typing import Any

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from .schemas import ShipmentCreate, ShipmentRead, ShipmentUpdate
from .database import shipments, save


app = FastAPI()

# shipments = {
#     12701: {"weight": 1.0, "content": "glassware", "status": "placed", "destination": None},
#     12702: {"weight": 2.3, "content": "books", "status": "shipped", "destination": 12345},
#     12703: {"weight": 1.1, "content": "electronics", "status": "delivered", "destination": 67890},
#     12704: {"weight": 3.5, "content": "furniture", "status": "in_transit", "destination": 11111},
#     12705: {"weight": 1.0, "content": "clothing", "status": "returned", "destination": 22222},
#     12706: {"weight": 4.0, "content": "appliances", "status": "processing", "destination": None},
#     12707: {"weight": 1.8, "content": "toys", "status": "placed", "destination": 33333},
# }



@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id: int):
    # Check for shipment with given id
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given id doesn't exist!"
        )
    shipment_data = shipments[id]
    return shipment_data


@app.post("/shipment", response_model=None)
def submit_shipment(shipment: ShipmentCreate) -> dict[str, int]:
    # Create and assign shipment a new id
    new_id = max(shipments.keys()) + 1
    # Add to shipments dict
    shipments[new_id] = {
        **shipment.model_dump(),
        "id": new_id,
        "status": "placed",
    }
    save()
    # Return id for later use
    return {"id": new_id}


# Use path and query parameters together
@app.get("/shipment/{field}")
def get_shipment_field(field: str, id: int) -> Any:
    return shipments[id][field]


@app.put("/shipment")
def shipment_update(
    id: int, content: str, weight: float, status: str
) -> dict[str, Any]:
    shipments[id] = {
        "content": content,
        "weight": weight,
        "status": status,
    }
    return shipments[id]

@app.patch("/shipment", response_model=ShipmentRead)
def patch_shipment(
    id: int,
    body: ShipmentUpdate
):
    shipment = shipments[id]
    shipment.update(body.model_dump(exclude_none=True))
    save()
    return shipments[id]

@app.delete("/shipment")
def delete_shipment( id: int):
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given id doesn't exist!"
        )
    shipments.pop(id)
    return {"detail": f"Shipment with id #{id} has been deleted."}


# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )