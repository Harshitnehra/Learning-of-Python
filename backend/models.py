
from datetime import datetime


def doc_to_employee(doc: dict) -> dict:
    """Convert employees collection document to API response."""
    if not doc:
        return doc
    return {
        "id": str(doc["_id"]),
        "employee_id": doc.get("employee_id", ""),
        "full_name": doc.get("full_name") or doc.get("name", ""),
        "email": doc.get("email", ""),
        "department": doc.get("department"),
        "is_active": doc.get("is_active", True),
    }


def doc_to_attendance(doc: dict) -> dict:
    """Convert attendance collection document to API response."""
    if not doc:
        return doc
    date_val = doc.get("date")
    if hasattr(date_val, "date"):
        date_val = date_val.date()
    created = doc.get("created_at")
    if isinstance(created, datetime):
        created = created.isoformat()
    return {
        "id": str(doc["_id"]),
        "employee_id": str(doc.get("employee_oid", doc.get("employee_id", ""))),
        "employee_code": doc.get("employee_code", ""),
        "employee_name": doc.get("employee_name", ""),
        "date": date_val,
        "status": doc.get("status", "Present"),
        "created_at": created,
    }
