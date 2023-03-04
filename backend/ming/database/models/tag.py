import sqlalchemy
from .base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.schema import FetchedValue


class Tag(Base):
    __tablename__ = "tag"

    tag_id: Mapped[int] = mapped_column(
        sqlalchemy.BigInteger, autoincrement=True, server_default=FetchedValue()
    )
    name: Mapped[str] = mapped_column(sqlalchemy.Text)

    __table_args__ = (sqlalchemy.PrimaryKeyConstraint("tag_id"),)
