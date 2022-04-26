from views import OwnerView, AdvertisementView, login
from settings import app

app.add_url_rule(
    "/owner-post/", view_func=OwnerView.as_view("create_owner"), methods=["POST"]
)

app.add_url_rule(
    "/adv-post/", view_func=AdvertisementView.as_view("create_ad"), methods=["POST"]
)

app.add_url_rule(
    "/adv-get/", view_func=AdvertisementView.as_view("get_ad"), methods=["GET"]
)

app.add_url_rule(
    "/adv-delete/", view_func=AdvertisementView.as_view("delete_ad"), methods=["DELETE"]
)

app.add_url_rule(
    "/login/", view_func=login, methods=["POST"]
)

