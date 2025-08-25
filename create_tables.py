from app.database import Base, engine
from app import models

print("Creating Database tables...")
Base.metadata.create_all(bind=engine)
print("Done!")
