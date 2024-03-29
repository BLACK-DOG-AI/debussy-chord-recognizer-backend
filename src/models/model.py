from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from enum import Enum
from datetime import datetime
import uuid

db = SQLAlchemy()

class Size(Enum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"

class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    postId = db.Column(db.String(36))
    userId = db.Column(db.String(36))
    description = db.Column(db.String(140))
    size = db.Column(db.Enum(Size))
    fragile = db.Column(db.Boolean())
    offer = db.Column(db.Numeric(10,2))
    createdAt = db.Column(db.DateTime, default=datetime.now())

class OfferSchema(SQLAlchemyAutoSchema): 
    class Meta:
        model = Offer
        load_instance = True
    