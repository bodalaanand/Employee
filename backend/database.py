from fastapi import FastAPI
from pydantic import BaseModel
from database import Database

DATABASE_URL = "postgresql+asyncpg://postgres:Nana@1610@localhost:5432/employees_db"