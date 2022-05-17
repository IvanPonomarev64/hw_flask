from settings import created_by_celery, flask_app, mail
from flask_mail import Message


@created_by_celery.task()
def send_mail(emails, email_data):
    for address in emails:
        msg = Message(email_data['subject'],
                      sender=flask_app.config['MAIL_DEFAULT_SENDER'],
                      recipients=[address])
        msg.body = email_data['body']
        with flask_app.app_context():
            mail.send(msg)
