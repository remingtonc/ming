import sqlalchemy
from .record import Record
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class RecordLink(Record):
    __tablename__ = "record_link"

    record_id: Mapped[int] = mapped_column(sqlalchemy.BigInteger)
    name: Mapped[str] = mapped_column(sqlalchemy.Text)
    url: Mapped[str] = mapped_column(sqlalchemy.Text)

    __table_args__ = (
        sqlalchemy.PrimaryKeyConstraint("record_id"),
        sqlalchemy.ForeignKeyConstraint(["record_id"], ["record.record_id"]),
    )
    __mapper_args__ = {
        "polymorphic_identity": "record_link",
    }
