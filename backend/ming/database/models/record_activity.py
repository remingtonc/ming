import sqlalchemy
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
from .record import Record
from sqlalchemy.schema import FetchedValue


class RecordActivity(Record):
    __tablename__ = "record_activity"

    record_id: Mapped[int] = mapped_column(sqlalchemy.BigInteger)
    name: Mapped[str] = mapped_column(sqlalchemy.Text)
    description: Mapped[str] = mapped_column(sqlalchemy.Text)
    happiness: Mapped[int] = mapped_column(sqlalchemy.SmallInteger)
    productivity: Mapped[int] = mapped_column(sqlalchemy.SmallInteger)
    start_time: Mapped[datetime] = mapped_column(
        sqlalchemy.TIMESTAMP, server_default=FetchedValue()
    )
    end_time: Mapped[datetime] = mapped_column(sqlalchemy.TIMESTAMP)

    __table_args__ = (
        sqlalchemy.PrimaryKeyConstraint("record_id"),
        sqlalchemy.ForeignKeyConstraint(["record_id"], ["record.record_id"]),
    )
    __mapper_args__ = {
        "polymorphic_identity": "record_activity",
    }
