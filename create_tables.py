from app.db.session import engine
from app.db.base import Base

# This import is important - even if unused directly 
from app.models.user import User

Base.metadata.create_all(bind=engine)   

print("Tables created successfully!")