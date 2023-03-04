import sqlalchemy
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
from sqlalchemy.schema import FetchedValue
from .types import Password


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(
        sqlalchemy.BigInteger, autoincrement=True, server_default=FetchedValue()
    )
    email: Mapped[str] = mapped_column(sqlalchemy.Text, nullable=False)
    password: Mapped[str] = mapped_column(Password, deferred=True, nullable=False)
    create_time: Mapped[datetime] = mapped_column(
        sqlalchemy.TIMESTAMP, server_default=FetchedValue()
    )

    __table_args__ = (
        sqlalchemy.PrimaryKeyConstraint("user_id"),
        sqlalchemy.UniqueConstraint("email"),
    )

    records = relationship("Record", back_populates="user")
    sessions = relationship("UserSession", back_populates="user")
