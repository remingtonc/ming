import sqlalchemy
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
from sqlalchemy.schema import FetchedValue


class Record(Base):
    __tablename__ = "record"

    record_id: Mapped[int] = mapped_column(
        sqlalchemy.BigInteger, autoincrement=True, server_default=FetchedValue()
    )
    user_id: Mapped[int] = mapped_column(sqlalchemy.BigInteger)
    polymorphic_type: Mapped[str] = mapped_column(sqlalchemy.Text)
    create_time: Mapped[datetime] = mapped_column(
        sqlalchemy.TIMESTAMP, server_default=FetchedValue()
    )

    __table_args__ = (
        sqlalchemy.PrimaryKeyConstraint("record_id"),
        sqlalchemy.ForeignKeyConstraint(["user_id"], ["user.user_id"]),
    )
    __mapper_args__ = {
        "polymorphic_identity": "record",
        "polymorphic_on": polymorphic_type,
    }

    user = relationship("User", back_populates="records")
