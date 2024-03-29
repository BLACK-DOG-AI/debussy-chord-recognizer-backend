from .base_command import BaseCommand
from src.models.model import db, Offer

class Reset(BaseCommand):
    def execute(self):
        db.session.query(Offer).delete()
        db.session.commit()
        return {"msg": "Todos los datos fueron eliminados"}