from sqlalchemy.exc import IntegrityError
from db.tables import Owner, Advertisement, Token
from settings import bcrypt
from validation import validator_model, OwnerModel, AdvertisementModel


class CreateModel:
    def create(self, data, session, table_name):
        with session:
            if table_name == 'owner':
                owner_data = validator_model(data, OwnerModel)
                new_entry = Owner(email=owner_data['email'],
                                  password=bcrypt.generate_password_hash(owner_data["password"].encode()).decode())

            elif table_name == 'advertisement':
                adv_data = validator_model(data, AdvertisementModel)
                token = session.query(Token).filter(Token.id == adv_data['token']).first()
                if token:
                    new_entry = Advertisement(title=adv_data['title'],
                                              description=adv_data['description'],
                                              owner_id=token.owner_id)
            session.add(new_entry)
            try:
                session.commit()
                return new_entry.to_dict()
            except IntegrityError:
                session.rollback()

