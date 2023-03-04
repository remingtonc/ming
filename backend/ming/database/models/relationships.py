import sqlalchemy
from .base import Base

record_has_tag = sqlalchemy.Table(
    "record_has_tag",
    Base.metadata,
    sqlalchemy.Column("tag_id", sqlalchemy.ForeignKey("Tag.tag_id")),
    sqlalchemy.Column("record_id", sqlalchemy.ForeignKey("Record.record_id")),
    sqlalchemy.PrimaryKeyConstraint("tag_id", "record_id"),
)
