from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db import Base

from app.database.enums import IncedentStatus, IncedentSource


class Incedent(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(nullable=False)

    status: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default=IncedentStatus.PENDING.value,
    )

    source: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default=IncedentSource.MONITORING.value,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
