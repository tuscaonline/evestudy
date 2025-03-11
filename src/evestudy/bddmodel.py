from typing import Optional, Self, List
from sqlalchemy import ForeignKey
from sqlalchemy import String, JSON
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Types(Base):
    __tablename__ = "types"
    id: Mapped[int] = mapped_column(primary_key=True)
    basePrice: Mapped[Optional[float]]
    capacity: Mapped[Optional[float]]

    factionID: Mapped[Optional[int]]
    graphicID: Mapped[Optional[int]]
    groupID: Mapped[Optional[int]]
    iconID: Mapped[Optional[int]]
    marketGroupID: Mapped[Optional[int]]
    mass: Mapped[Optional[float]]
    masteries: Mapped[Optional[JSON]] = mapped_column(type_=JSON)
    metaGroupID: Mapped[Optional[float]]

    portionSize: Mapped[Optional[int]]
    published: Mapped[Optional[bool]]
    raceID: Mapped[Optional[int]]
    radius: Mapped[Optional[float]]
    sofFactionName: Mapped[Optional[str]]
    sofMaterialSetID: Mapped[Optional[int]]
    soundID: Mapped[Optional[int]]
    traits: Mapped[Optional[JSON]] = mapped_column(type_=JSON)
    variationParentTypeID: Mapped[Optional[int]]
    volume: Mapped[Optional[float]]
    descriptionEn: Mapped[Optional[str]]
    descriptionFr: Mapped[Optional[str]]
    nameEn: Mapped[Optional[str]]
    nameFr: Mapped[Optional[str]]

    description: Mapped[Optional[JSON]] = mapped_column(type_=JSON)
    name: Mapped[Optional[JSON]] = mapped_column(type_=JSON)

    def __repr__(self) -> str:
        return f"Types(id={self.id!r}, name={self.nameEn!r}, fullname={self.descriptionEn!r})"

    @classmethod
    def load(cls, id: int, description: dict={}, name: dict={}, **kwArgs):
        return cls(
            id=id,
            description=description,
            name=name,
            descriptionEn=description.get("en"),
            descriptionFr=description.get("fr"),
            nameEn=name.get("en"),
            nameFr=name.get("fr"),
            **kwArgs
        )


# class Address(Base):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped["User"] = relationship(back_populates="addresses")
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"
