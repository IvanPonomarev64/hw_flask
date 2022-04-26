from flask import jsonify, request
from flask.views import MethodView

from models import CreateModel
from settings import Session

from db.tables import Owner, Advertisement, Token

from exception import HTTPError


class AdvertisementView(MethodView, CreateModel):
    def post(self):
        with Session() as session:
            return super().create(request.json, session, 'advertisement')

    def get(self):
        data = request.json
        with Session() as session:
            response = session.query(Advertisement).filter(Advertisement.id == data["adv"]).first()
            if response:
                return jsonify(response.to_dict())
            raise HTTPError(400, "Advertisement not found")

    def delete(self):
        data = request.json
        with Session() as session:
            if session.query(Advertisement).filter(Advertisement.id == data["ad"]).first().owner_id == data["owner"]:
                session.query(Advertisement).filter(
                    Advertisement.id == data["ad"],
                    Advertisement.owner_id == data["owner"]).delete()
                session.commit()
                return jsonify("Success")
            raise HTTPError(400, "You don't have enough rights for this operation")


class OwnerView(MethodView, CreateModel):
    def post(self):
        with Session() as session:
            return super().create(request.json, session, 'owner')


def login():
    data = request.json
    with Session() as session:
        owner = session.query(Owner).filter(Owner.email == data['email']).first()

        if not owner:
            raise HTTPError(401, "invalid login")

        elif not owner.check_password(data['password']):
            raise HTTPError(401, "invalid password")

        elif owner and owner.check_password(data['password']):
            token = Token(owner_id=owner.id)
            session.add(token)
            session.commit()
            return jsonify({'token': token.id})
