from app.db.session import SessionLocal
from app.models.user import User
from app.security import get_password_hash
import uuid

db = SessionLocal()

new_user = User(
    email = f"test_{uuid.uuid4()}@example.com",
    hashed_password=get_password_hash("test123"),
)

db.add(new_user)
db.commit()

users = db.query(User).all()
print(users)

db.close()