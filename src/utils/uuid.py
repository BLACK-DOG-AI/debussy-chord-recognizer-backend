from src.errors.errors import BadRequest
import uuid

class UuidUtil:
    def __init__(self, offer_id):
        self.offer_id = offer_id

    def validate_uuid(self):
        try:
            uuid_result = uuid.UUID(self.offer_id, version=4)
            return str(uuid_result) == self.offer_id
        except Exception:
            raise BadRequest()