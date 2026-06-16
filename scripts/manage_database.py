from models.models import Unit
from core.database import Base, engine, SessionLocal
import argparse
from pathlib import Path
import json
from typing import Type, TypeVar

parser = argparse.ArgumentParser()

parser.add_argument("command", choices=["init", "drop", "seed"])
args = parser.parse_args()

units = Path("../seed/units")

Model = TypeVar("Model", bound=Base)

def seed_db(model: Type[Model], directory: Path, extension: str):
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


if args.command == "drop":
    Base.metadata.drop_all(bind=engine)
if args.command == "init":
    Base.metadata.create_all(bind=engine)
if args.command == "seed":
    seed_db(Unit, units, "json")
