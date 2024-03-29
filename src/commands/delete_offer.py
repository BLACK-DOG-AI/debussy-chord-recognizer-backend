from .base_command  import  BaseCommand
from src.models.model import OfferSchema, Offer, db
from src.errors.errors import NotFound
from src.clients.user_client import UserClient
from src.utils.uuid import UuidUtil

offer_schema = OfferSchema()

class DeleteOffer(BaseCommand):
    def __init__(self, offer_id, token):
        self.offer_id = offer_id
        self.token = token

    def execute(self):
        UserClient(self.token).validate_user()
        UuidUtil(self.offer_id).validate_uuid()

        offer = db.session.get(Offer, self.offer_id)
        if not offer:
            raise NotFound()
        
        db.session.delete(offer)
        db.session.commit()

        return {"msg": "la oferta fue eliminada"}