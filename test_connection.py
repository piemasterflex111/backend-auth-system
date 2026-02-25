from app.db.session import engine

try:
    with engine.connect() as connection:
        print("Database connection successful! with engine.connect() as connection ")
except Exception as e:
    print("Connection failed:", e)