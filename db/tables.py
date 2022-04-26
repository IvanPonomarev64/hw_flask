from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from settings import bcrypt
import uuid


Base = declarative_base()


class Advertisement(Base):
    __tablename__ = "advertisement"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, unique=True)
    description = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())
    owner_id = Column(Integer, ForeignKey("owner.id"))

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "creation_time": int(self.creation_time.timestamp()),
            "owner": self.owner_id
        }


class Owner(Base):
    __tablename__ = "owner"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String, nullable=False, unique=False)
    advertisement_id = relationship(Advertisement, backref='owner')

    @classmethod
    def hashing(cls, password: str):
        return bcrypt.generate_password_hash(password.encode()).decode()

    def check_password(self, password: str):
        return bcrypt.check_password_hash(self.password.encode(), password.encode())

    def to_dict(self):
        return {
            "email": self.email,
            "id": self.id,
        }


class Token(Base):
    __tablename__ = "tokens"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    creation_time = Column(DateTime, server_default=func.now())
    owner_id = Column(Integer, ForeignKey("owner.id"))
    owner = relationship(Owner, lazy="joined")


def create_table(engine, insp):
    tables = (Owner.__tablename__, Advertisement.__tablename__, Token.__tablename__)
    for table_name in tables:
        if table_name in insp.get_table_names():
            print("Next")
        else:
            Base.metadata.create_all(engine)
            print("ok")
