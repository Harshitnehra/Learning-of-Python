
import logging
from pathlib import Path

from dotenv import load_dotenv

_backend_dir = Path(__file__).resolve().parent
load_dotenv(_backend_dir / ".env")
load_dotenv(_backend_dir / ".env.local", override=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from motor.motor_asyncio import AsyncIOMotorClient

import database
from routes import employees, attendance


@asynccontextmanager
async def lifespan(app: FastAPI):
    database.client = AsyncIOMotorClient(database.MONGODB_URL)
    db = database.client[database.DB_NAME]
    try:
        await db.employees.create_index("employee_id", unique=True)
        await db.employees.create_index("email", unique=True)
        logger.info("MongoDB connected: %s", database.DB_NAME)
    except Exception as e:
        logger.warning("MongoDB index creation skipped: %s", e)
    try:
        yield
    finally:
        database.client.close()



CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "*",
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Allow-Credentials": "true",
}


def error_response(status_code: int, detail: str) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"success": False, "detail": detail},
        headers=CORS_HEADERS,
    )


app = FastAPI(
    lifespan=lifespan,
    title="Assessment API",
    description="Backend API for employees and attendance (MongoDB)",
    version="1.0.0",
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    messages = [f"{e.get('loc', [])[-1]}: {e.get('msg')}" for e in errors]
    return error_response(422, "Validation error. " + "; ".join(messages))


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.exception("Request failed: %s %s", request.method, request.url.path)
    msg = "An unexpected error occurred. Please try again later."
    if "pymongo" in type(exc).__module__ or "motor" in type(exc).__module__:
        msg = "Database error. Is MongoDB running? Check backend terminal for details."
    return error_response(500, msg)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    for key, value in CORS_HEADERS.items():
        response.headers[key] = value
    return response

app.include_router(employees.router, prefix="/api/employees", tags=["employees"])
app.include_router(attendance.router, prefix="/api/attendance", tags=["attendance"])


@app.get("/api/health")
def health():
    return {"status": "ok", "message": "Backend connected"}


@app.get("/")
def root():
    return {"message": "Assessment API", "docs": "/docs"}
