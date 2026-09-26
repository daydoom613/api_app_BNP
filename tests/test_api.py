from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_only_three_business_endpoints():
    routes = {(m, route.path) for route in app.routes if route.path.startswith("/api/") for m in route.methods}
    assert routes == {("GET", "/api/GetCatalog"), ("POST", "/api/CreateOrder"), ("PUT", "/api/UpdateItem/{item_id}")}

def test_catalog_order_update():
    assert client.get("/api/GetCatalog").status_code == 200
    assert client.post("/api/CreateOrder", json={"product_id": 1, "quantity": 2}).json()["order"]["total"] == 200
    assert client.put("/api/UpdateItem/1", json={"name": "Updated Compute"}).status_code == 200
