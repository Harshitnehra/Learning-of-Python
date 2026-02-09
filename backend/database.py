import os
from motor.motor_asyncio import AsyncIOMotorClient
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGODB_DB_NAME", "assessment")


client: AsyncIOMotorClient | None = None


def get_client() -> AsyncIOMotorClient:
    if client is None:
        raise RuntimeError("MongoDB client not initialized")
    return client


def get_db():
    
    return get_client()[DB_NAME]
