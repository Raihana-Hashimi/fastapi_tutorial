from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from .schemas import ShipmentCreate, ShipmentRead, ShipmentUpdate
from .database import Database


app = FastAPI()

db = Database()



@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id: int):
    shipment = db.get(id)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given id doesn't exist!"
        )
    return shipment


@app.post("/shipment", response_model=None)
def submit_shipment(shipment: ShipmentCreate) -> dict[str, int]:
    new_id = db.create(shipment)
    return {"id": new_id}


@app.patch("/shipment", response_model=ShipmentRead)
def patch_shipment(
    id: int,
    shipment: ShipmentUpdate
):
    shipment = db.update(id, shipment)
    return shipment

@app.delete("/shipment")
def delete_shipment( id: int):
    db.delete(id)
    return {"detail": f"Shipment with id #{id} has been deleted."}


# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )