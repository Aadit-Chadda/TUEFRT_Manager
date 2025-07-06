# Test Postgres on Neon
import os
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://neondb_owner:npg_K0IBuH1NPCEl@ep-weathered-sun-aeotj4sk-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    row = connection.execute(text("SELECT version();"))
    print(row.scalar())

