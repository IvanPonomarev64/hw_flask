from views import OwnerView, AdvertisementView, login, SendEmailView
from settings import flask_app


flask_app.add_url_rule(
    "/owner-post/", view_func=OwnerView.as_view("create_owner"), methods=["POST"]
)

flask_app.add_url_rule(
    "/adv-post/", view_func=AdvertisementView.as_view("create_ad"), methods=["POST"]
)

flask_app.add_url_rule(
    "/adv-get/", view_func=AdvertisementView.as_view("get_ad"), methods=["GET"]
)

flask_app.add_url_rule(
    "/adv-delete/", view_func=AdvertisementView.as_view("delete_ad"), methods=["DELETE"]
)

flask_app.add_url_rule(
    "/login/", view_func=login, methods=["POST"]
)

flask_app.add_url_rule(
    "/send-mail/", view_func=SendEmailView.as_view("creat_task"), methods=['POST']
)

flask_app.add_url_rule(
    "/status/<task_id>/", view_func=SendEmailView.as_view("get_status"), methods=['GET']
)