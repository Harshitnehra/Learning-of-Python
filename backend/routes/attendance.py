
from datetime import date, datetime
from fastapi import APIRouter, Depends, HTTPException, Query
from bson import ObjectId

from database import get_db
from models import doc_to_attendance
from schemas import AttendanceCreate, AttendanceResponse

router = APIRouter()


async def _resolve_employee(db, employee_id: str):
   
    employee_id = employee_id.strip()
    if len(employee_id) == 24:
        try:
            oid = ObjectId(employee_id)
            doc = await db.employees.find_one({"_id": oid})
            if doc:
                return doc
        except Exception:
            pass
    doc = await db.employees.find_one({"employee_id": employee_id})
    return doc


async def _get_employee_doc(db, employee_id: str):
    doc = await _resolve_employee(db, employee_id)
    if not doc:
        raise HTTPException(
            status_code=404,
            detail="Employee not found. Use a valid Employee ID.",
        )
    return doc


@router.get("/", response_model=list[AttendanceResponse])
async def list_attendance(
    employee_id: str | None = Query(None, description="Filter by Employee ID "),
    from_date: date | None = Query(None, alias="from_date"),
    to_date: date | None = Query(None, alias="to_date"),
    skip: int = 0,
    limit: int = 500,
    db=Depends(get_db),
):
   
    filt = {}
    if employee_id:
        emp = await _get_employee_doc(db, employee_id)
        filt["employee_oid"] = emp["_id"]
    if from_date or to_date:
        date_q = {}
        if from_date:
            date_q["$gte"] = datetime.combine(from_date, datetime.min.time())
        if to_date:
            date_q["$lte"] = datetime.combine(to_date, datetime.max.time())
        filt["date"] = date_q

    cursor = db.attendance.find(filt).skip(skip).limit(limit).sort("date", -1)
    docs = await cursor.to_list(length=limit)
    if not docs:
        return []
    employee_oids = list({d["employee_oid"] for d in docs})
    name_by_oid = {}
    async for emp in db.employees.find(
        {"_id": {"$in": employee_oids}},
        {"_id": 1, "full_name": 1, "name": 1},
    ):
        name_by_oid[emp["_id"]] = emp.get("full_name") or emp.get("name") or ""
    out = []
    for d in docs:
        if d["employee_oid"] not in name_by_oid:
            continue
        d = dict(d)
        d["employee_name"] = d.get("employee_name") or name_by_oid.get(d["employee_oid"], "")
        out.append(AttendanceResponse(**doc_to_attendance(d)))
    return out


@router.get("/{attendance_id}", response_model=AttendanceResponse)
async def get_attendance(attendance_id: str, db=Depends(get_db)):
    try:
        oid = ObjectId(attendance_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid attendance id format.")
    doc = await db.attendance.find_one({"_id": oid})
    if not doc:
        raise HTTPException(status_code=404, detail="Attendance record not found.")
    emp = await db.employees.find_one(
        {"_id": doc["employee_oid"]},
        {"full_name": 1, "name": 1},
    )
    if not emp:
        raise HTTPException(status_code=404, detail="Attendance record not found.")
    doc = dict(doc)
    doc["employee_name"] = doc.get("employee_name") or emp.get("full_name") or emp.get("name") or ""
    return AttendanceResponse(**doc_to_attendance(doc))


@router.post("/", response_model=AttendanceResponse, status_code=201)
async def create_attendance(data: AttendanceCreate, db=Depends(get_db)):
    
    if await db.employees.count_documents({}) == 0:
        raise HTTPException(
            status_code=400,
            detail="No employees yet. Add one above.",
        )
    if data.date > date.today():
        raise HTTPException(
            status_code=400,
            detail="Cannot mark attendance for a future date. Only today or past dates are allowed.",
        )
    employee = await _get_employee_doc(db, data.employee_id)
    date_val = datetime.combine(data.date, datetime.min.time())
    existing = await db.attendance.find_one({
        "employee_oid": employee["_id"],
        "date": date_val,
    })
    if existing:
        raise HTTPException(
            status_code=400,
            detail=f"Attendance already marked for this employee on {data.date}.",
        )
    doc = {
        "employee_oid": employee["_id"],
        "employee_code": employee["employee_id"],
        "employee_name": employee.get("full_name") or employee.get("name", ""),
        "date": date_val,
        "status": data.status,
        "created_at": datetime.utcnow(),
    }
    result = await db.attendance.insert_one(doc)
    doc["_id"] = result.inserted_id
    return AttendanceResponse(**doc_to_attendance(doc))
