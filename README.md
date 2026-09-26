# FinOps: exact three business endpoints

The first column of the supplied spreadsheet contains `CreateOrder`, `GetCatalog`, and `UpdateItem`. Those are the only **business API endpoints** exposed here:

| Name | Method | URL |
|---|---|---|
| CreateOrder | POST | `/api/CreateOrder` |
| GetCatalog | GET | `/api/GetCatalog` |
| UpdateItem | PUT | `/api/UpdateItem/{item_id}` |

The HTML page at `/` and automatically generated FastAPI `/docs` are supporting UI/documentation routes, not additional business endpoints. The spreadsheet also has priority and critical columns; those are metadata, not additional endpoints.

## Local Windows PowerShell

From the `app` directory:

```powershell
py -m pip install -r requirements.txt
py -m uvicorn api.app:app --host 0.0.0.0 --port 8000
```

Open http://localhost:8000 and http://localhost:8000/docs.

## Docker

```powershell
docker build -t finops-web:1.0 .
docker run --rm -p 8000:8000 finops-web:1.0
```

Demo-only: data is stored in memory, and orders are not persisted.
