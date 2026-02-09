"""
Request/response schemas with validation.
"""
from datetime import date, datetime
from typing import Literal, Optional
from pydantic import BaseModel, EmailStr, Field


# ----- Employee -----

class EmployeeCreate(BaseModel):
    employee_id: str = Field(..., min_length=1, description="Unique employee identifier")
    full_name: str = Field(..., min_length=1, description="Full name")
    email: EmailStr
    department: Optional[str] = None


class EmployeeResponse(BaseModel):
    id: str
    employee_id: str
    full_name: str
    email: str
    department: Optional[str]
    is_active: bool


# ----- Attendance -----

AttendanceStatus = Literal["Present", "Absent"]


class AttendanceCreate(BaseModel):
    employee_id: str = Field(..., description="Employee ID (unique code) or MongoDB id")
    date: date
    status: AttendanceStatus = "Present"


class AttendanceResponse(BaseModel):
    id: str
    employee_id: str
    employee_code: str
    employee_name: Optional[str] = ""
    date: date
    status: str
    created_at: Optional[str] = None
