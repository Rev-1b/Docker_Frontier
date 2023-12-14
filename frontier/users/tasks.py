import uuid
from datetime import timedelta

from celery import shared_task
from django.contrib.auth.models import User
from django.utils.timezone import now

from django.contrib.auth.forms import PasswordResetForm
from users.models import EmailVerificationModel


@shared_task
def send_verification_email(user_id):
    user = User.objects.get(pk=user_id)
    expiration = now() + timedelta(hours=48)
    record = EmailVerificationModel.objects.create(code=uuid.uuid4(), user=user, expiration_time=expiration)
    record.send_verification_email()


@shared_task
def send_reset_mail_task(subject_template_name, email_template_name, context,
                         from_email, to_email, html_email_template_name):
    context['user'] = User.objects.get(pk=context['user'])

    PasswordResetForm.send_mail(
        None,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name
    )
