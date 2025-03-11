import pytest
from src.evestudy import bddmodel

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select


@pytest.fixture
def createDb():
    engine = create_engine("sqlite://")
    bddmodel.Base.metadata.create_all(engine)
    return engine


@pytest.fixture
def scourge() -> bddmodel.Types:
    scourge = {
        "basePrice": 30000.0,
        "description": {
            "de": "Eine ultraschwere Lenkwaffe mit Durchschlagkopf. Sie ist zwar ein langsames Projektil, aber ihr bloßes Schadenspotential ist einfach überwältigend.",
            "en": "An ultra-heavy piercing missile. While it is a slow projectile, its sheer damage potential is simply staggering.",
            "es": "Misil perforante ultrapesado. Aunque lento, su potencial de daño real resulta impresionante.",
            "fr": "Missile perforant ultra-lourd. Il s'agit certes d'un projectile assez lent, mais au potentiel destructeur tout simplement impressionnant.",
            "ja": "ウルトラヘビーピアシングミサイル。速度は遅いが、その破壊力は実に驚異的。",
            "ko": "대형 관통 미사일입니다. 느린 비행 속도를 지니고 있으나 타격 시 적에게 치명적인 피해를 입힙니다.",
            "ru": "Сверхтяжелая бронебойная ракета. Отличается низкой скоростью, но ее ударная мощь поражает воображение.",
            "zh": "一种终极重型穿刺导弹。虽然慢而笨重，但是破坏力着实惊人。",
        },
        "graphicID": 20014,
        "groupID": 89,
        "iconID": 1346,
        "marketGroupID": 923,
        "mass": 1500.0,
        "metaGroupID": 1,
        "name": {
            "de": "Scourge Torpedo",
            "en": "Scourge Torpedo",
            "es": "Torpedo Scourge",
            "fr": "Torpille Scourge",
            "ja": "スコージトルピード",
            "ko": "스커지 토피도",
            "ru": "Scourge Torpedo",
            "zh": "鞭挞鱼雷",
        },
        "portionSize": 100,
        "published": True,
        "radius": 300.0,
        "volume": 0.05,
    }
    idScourge = 267
    scourge = bddmodel.Types.load(idScourge, **scourge)

    dTypeMaterials = [
        {"materialTypeID": 34, "quantity": 1876},
        {"materialTypeID": 39, "quantity": 12},
        {"materialTypeID": 40, "quantity": 4},
    ]
    materials = []
    for i in dTypeMaterials:
        materials.append(
            bddmodel.TypeMaterials(**i)
        )
    scourge.materials = materials
    return scourge


def test_scourge(createDb: Engine, scourge: bddmodel.Types):
    assert scourge.nameFr == "Torpille Scourge"
    assert (
        scourge.__repr__()
        == "Types(id=267, name='Scourge Torpedo', fullname='An ultra-heavy piercing missile. While it is a slow projectile, its sheer damage potential is simply staggering.')"
    )


def test_insertScourge(createDb: Engine, scourge: bddmodel.Types):
    engine = createDb

    with Session(engine) as session:
        session.add(scourge)
        session.commit()

    session = Session(engine)
    stmt = select(bddmodel.Types).where(bddmodel.Types.id == 267)
    result = session.scalars(stmt).one()
    assert result.id == 267
    assert result.nameEn == "Scourge Torpedo"
    assert len(result.materials) == 3
    ...
    