from .base_command  import  BaseCommand
from src.models.model import OfferSchema, Offer, db
from src.errors.errors import BadRequest, PreconditionFailed
from src.clients.user_client import UserClient
from src.models.model import Size

offer_schema = OfferSchema()

class CreateOffer(BaseCommand):

    def __init__(self, json, token):
        self.post_id = json.get("postId", "").strip()
        self.description = json.get("description", "").strip()
        self.size = json.get("size", "").strip()
        self.fragile = json.get("fragile", None)
        self.offer = json.get("offer", None)
        self.token = token

    def execute(self):
        if not (self.post_id and self.description and self.size and self.fragile != None and self.offer != None):
            raise BadRequest()
        
        if not (self.size in Size.__members__):
            raise PreconditionFailed()
        
        if self.offer < 0:
            raise PreconditionFailed()

        user_id = UserClient(self.token).validate_user()
        offer = Offer(postId=self.post_id, userId=user_id, description=self.description, size=self.size, fragile=self.fragile, offer=self.offer)

        db.session.add(offer)
        db.session.commit()
        return {
            'id': offer.id, 
            'userId': offer.userId, 
            'createdAt': offer.createdAt.isoformat()
        }