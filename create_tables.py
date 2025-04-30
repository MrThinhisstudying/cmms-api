from app.database import engine
from app import models

print("✅ Connected to:", engine.url)
models.Base.metadata.create_all(bind=engine)
print("✅ All tables created.")
