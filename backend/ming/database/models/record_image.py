import sqlalchemy
from .record import Record
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class RecordImage(Record):
    __tablename__ = "record_image"

    record_id: Mapped[int] = mapped_column(sqlalchemy.BigInteger)
    content: Mapped[bytes] = mapped_column(sqlalchemy.LargeBinary)

    __table_args__ = (
        sqlalchemy.PrimaryKeyConstraint("record_id"),
        sqlalchemy.ForeignKeyConstraint(["record_id"], ["record.record_id"]),
    )
    __mapper_args__ = {
        "polymorphic_identity": "record_image",
    }
