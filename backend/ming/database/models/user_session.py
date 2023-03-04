import sqlalchemy
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from uuid import UUID
from datetime import datetime
from sqlalchemy.schema import FetchedValue


class UserSession(Base):
    __tablename__ = "user_session"

    user_id: Mapped[int] = mapped_column(sqlalchemy.BigInteger)
    session_id: Mapped[UUID] = mapped_column(
        sqlalchemy.Uuid, server_default=FetchedValue()
    )
    create_time: Mapped[datetime] = mapped_column(
        sqlalchemy.TIMESTAMP, server_default=FetchedValue()
    )

    __table_args__ = (
        sqlalchemy.PrimaryKeyConstraint("user_id", "session_id"),
        sqlalchemy.ForeignKeyConstraint(["user_id"], ["user.user_id"]),
    )

    user = relationship("User", back_populates="sessions")
