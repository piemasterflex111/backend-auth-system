from app.db.session import SessionLocal
from app.models.user import User

db = SessionLocal()

new_user = User(
    email="payamistestinguserobject@gmail.com",
    hashed_password="fakehashedpassword",
)

db.add(new_user)
db.commit()
users = db.query(User).all()    
print(users)

db.close()  