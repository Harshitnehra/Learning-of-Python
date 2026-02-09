
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId

from database import get_db
from models import doc_to_employee
from schemas import EmployeeCreate, EmployeeResponse

router = APIRouter()


@router.get("/", response_model=list[EmployeeResponse])
async def list_employees(skip: int = 0, limit: int = 500, db=Depends(get_db)):
   
    cursor = db.employees.find().skip(skip).limit(limit).sort("created_at", -1)
    docs = await cursor.to_list(length=limit)
    return [EmployeeResponse(**doc_to_employee(d)) for d in docs]


@router.get("/{id}", response_model=EmployeeResponse)
async def get_employee(id: str, db=Depends(get_db)):
    
    try:
        oid = ObjectId(id)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid employee id format.",
        )
    doc = await db.employees.find_one({"_id": oid})
    if not doc:
        raise HTTPException(status_code=404, detail="Employee not found.")
    return EmployeeResponse(**doc_to_employee(doc))


@router.post("/", response_model=EmployeeResponse, status_code=201)
async def create_employee(data: EmployeeCreate, db=Depends(get_db)):
  
    emp_id = (data.employee_id or "").strip()
    full_name = (data.full_name or "").strip()
    email = (data.email or "").strip().lower()
    department = (data.department or "").strip() or None

    if not emp_id or not full_name or not email:
        raise HTTPException(status_code=400, detail="Employee ID, Full Name and Email are required.")

    existing_id = await db.employees.find_one({"employee_id": emp_id})
    if existing_id:
        raise HTTPException(
            status_code=400,
            detail=f"Employee ID {emp_id} already exists.",
        )
    existing_email = await db.employees.find_one({"email": email})
    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="An employee with this email address already exists.",
        )

    now = datetime.utcnow()
    doc = {
        "employee_id": emp_id,
        "full_name": full_name,
        "email": email,
        "department": department,
        "is_active": True,
        "created_at": now,
        "updated_at": now,
    }
    try:
        result = await db.employees.insert_one(doc)
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=" connection error",
        ) from e
    doc["_id"] = result.inserted_id
    return EmployeeResponse(**doc_to_employee(doc))


@router.delete("/{id}", status_code=200)
async def delete_employee(id: str, db=Depends(get_db)):
  
    try:
        oid = ObjectId(id)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid employee id format.",
        )
    result = await db.employees.delete_one({"_id": oid})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found.")
    return {"message": "Employee deleted successfully."}
