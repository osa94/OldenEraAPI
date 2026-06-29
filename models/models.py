from core.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, SmallInteger, Boolean

class Unit(Base):
    __tablename__ = "units"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    faction: Mapped[str] = mapped_column(String, nullable=False)
    tier: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    hp: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    attack: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    defence: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    min_damage: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    max_damage: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    morale: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    luck: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    initiative: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    speed: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    upgrade: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    gold_cost: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    faction_resource_cost: Mapped[int] = mapped_column(SmallInteger, nullable=False)

class CreatureType(Base):
    __tablename__ = "creature_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    min_morale: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    max_morale: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    min_luck: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    max_luck: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    necromancy: Mapped[bool] = mapped_column(Boolean, nullable=False)