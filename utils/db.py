# # A fake db class

# class FakeDB:
#     def __init__(self):
#         self.admins = {}

#     def add_admin(self, admin_data):
#         self.admins[admin_data.email] = admin_data

#     def get_admin(self, email):
#         return self.admins.get(email)

#     def remove_admin(self, email):
#         if email in self.admins:
#             del self.admins[email]
#         else:
#             raise ValueError("Admin not found.")


# db = FakeDB()


# def get_db():
#     return db


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Settings

settings = Settings() 

# 1. First step is to create the engine. 
Engine = create_engine(settings.get_postgres_url().render_as_string(hide_password=False))

SessionLocal = sessionmaker(bind=Engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 