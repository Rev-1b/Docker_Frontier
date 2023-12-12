import uuid
from datetime import timedelta

from celery import shared_task
from django.contrib.auth.models import User
from django.utils.timezone import now

from users.models import EmailVerificationModel


@shared_task
def send_verification_email(user_id):
    user = User.objects.get(pk=user_id)
    expiration = now() + timedelta(hours=48)
    record = EmailVerificationModel.objects.create(code=uuid.uuid4(), user=user, expiration_time=expiration)
    record.send_verification_email()
