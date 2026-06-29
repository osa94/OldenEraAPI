from models.models import Unit, CreatureType
from core.database import Base, engine, SessionLocal
import argparse
from pathlib import Path
import json
from typing import Type, TypeVar

parser = argparse.ArgumentParser()

parser.add_argument("command", choices=["init", "drop", "models","relationships"])
args = parser.parse_args()

units = Path("seed/units")
creature_types = Path("seed/abilities/passive_abilities")

Model = TypeVar("Model", bound=Base)

def seed_models(model: Type[Model], directory: Path, extension: str):
    database = SessionLocal()
    try:
        for json_file in directory.glob(f"*.{extension}"):
            with open(json_file, "r", encoding="utf-8") as f:
                json_data = json.load(f)
            for element in json_data.values():
                existing = database.query(model).filter_by(name=element["name"]).first()
                if existing:
                    continue
                new_object = model(**element)
                database.add(new_object)
        database.commit()
    finally:
        database.close()

def seed_relationship(model1, model2, model1_key, model2_key, model1_json_path: str, model2_json_path, association_json_path):
    database = SessionLocal()
    model1_json = json.load(open(model1_json_path))
    model2_json = json.load(open(model2_json_path))
    association_json = json.load(open(association_json_path))
    for element in association_json:
        model1_dict = model1_json.get(element.get(model1_key))
        model2_dict = model2_json.get(element.get(model2_key))

        unit = database.query(model1).filter_by(name=model1_dict.get("name")).first()

        passive = database.query(model2).filter_by(name=model2_dict.get("name")).first()
        unit.passive_abilities.append(passive)

    database.commit()

if args.command == "drop":
    Base.metadata.drop_all(bind=engine)
if args.command == "init":
    Base.metadata.create_all(bind=engine)
if args.command == "models":
    seed_models(Unit, units, "json")
    seed_models(CreatureType, creature_types, "json")
'''if args.command == "relationships":
    seed_relationship(Unit, PassiveAbility, "unit_id", "passive_id", 'seed/units/units_hive.json',
                      'seed/abilities/passive_abilities/passive_abilities.json',
                      "seed/associations/passive_unit_hive.json")'''
