from app.db.session import SessionLocal
from app.models.user import User
from app.security import get_password_hash

db = SessionLocal()

new_user = User(
    email="payamistestinguserobject_2-27-26@gmail.com",
    hashed_password=get_password_hash("test123"),
)

db.add(new_user)
db.commit()

users = db.query(User).all()
print(users)

db.close()