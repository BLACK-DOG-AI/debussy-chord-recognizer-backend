from .base_command  import  BaseCommand
from src.models.model import OfferSchema, Offer, db
from src.clients.user_client import UserClient

offer_schema = OfferSchema()

class GetListOffer(BaseCommand):
    def __init__(self, token, owner, post_id):
        self.token = token
        self.owner = owner
        self.post_id = post_id

    def execute(self):
        user_id = UserClient(self.token).validate_user()
        
        if self.owner and not self.post_id:
            return self.get_offers_by_owner(user_id)
        
        if self.post_id and not self.owner:
            return self.get_offers_by_post()
        
        if not (self.owner and self.post_id):
            return self.get_all_offers()
        else:
            return self.get_offers_by_post_and_owner(user_id)

    def build_list_response(self, data_offers):
        list_offers = []
        for offer in data_offers:
            data = {
                "id": offer.id,
                "postId": offer.postId,
                "description": offer.description,
                "size": offer.size.name,
                "fragile": offer.fragile,
                "offer": offer.offer,
                "createdAt": offer.createdAt,
                "userId": offer.userId
            }
            list_offers.append(data)
        return list_offers

    def get_all_offers(self):
        data_offers = db.session.query(Offer).all()
        return self.build_list_response(data_offers)
    
    def get_offers_by_owner(self, user_id):
        if self.owner == "me":
            data_offers = db.session.query(Offer).filter(Offer.userId == user_id).all()
        else:
            data_offers = db.session.query(Offer).filter(Offer.userId == self.owner).all()

        return self.build_list_response(data_offers)
    
    def get_offers_by_post(self):
        data_offers = db.session.query(Offer).filter(Offer.postId == self.post_id).all()
        return self.build_list_response(data_offers)
    
    def get_offers_by_post_and_owner(self, user_id):
        if self.owner == "me":
            data_offers = db.session.query(Offer).filter(Offer.postId == self.post_id, Offer.userId == user_id).all()
        else:
            data_offers = db.session.query(Offer).filter(Offer.postId == self.post_id, Offer.userId == self.owner).all()

        return self.build_list_response(data_offers)
    







        
