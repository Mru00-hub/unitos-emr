import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT count(*) FROM patients;"))
        print(f"✅ SUCCESS! Patient Count: {result.scalar()}")
except Exception as e:
    print(f"❌ ERROR: {e}")
