import enum
from database.orm import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class MonthEnum(enum.Enum):
    JANUARY = 'january'
    FEBRUARY = 'february'
    MARCH = 'march'
    APRIL = 'april'
    MAY = 'may'
    JUNE = 'june'
    JULY = 'july'
    AUGUST = 'august'
    SEPTEMBER = 'september'
    OCTOBER = 'october'
    NOVEMBER = 'november'
    DECEMBER = 'december'

class MonthDaysEnum(enum.IntEnum):
    JANUARY = 31
    FEBRUARY = 28 
    MARCH = 31
    APRIL = 30
    MAY = 31
    JUNE = 30
    JULY = 31
    AUGUST = 31
    SEPTEMBER = 30
    OCTOBER = 31
    NOVEMBER = 30
    DECEMBER = 31


class CityModel(Base):
    __tablename__ = 'city'

    name: Mapped[str]

    parameters: Mapped[list['CityParameterModel']] = relationship(
        back_populates='city'
    )


class CityParameterModel(Base):
    __tablename__ = 'city_parameter'

    moth: Mapped[MonthEnum]

    insolation: Mapped[int]
    wind_speed: Mapped[int]
    air_density: Mapped[int]

    city_id: Mapped[int] = mapped_column(
        ForeignKey('city.id')
    )

    city: Mapped['CityModel'] = relationship(
        back_populates='parameters'
    )

