from django.core.mail import send_mail
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.timezone import now


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE,
                                verbose_name='Связанный пользователь')
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name='О себе')
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True, verbose_name='Фотография пользователя')
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'Профиль пользователя: {self.user.username}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class EmailVerificationModel(models.Model):
    code = models.UUIDField(unique=True, verbose_name='Уникальный код')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания запроса')
    expiration_time = models.DateTimeField(verbose_name='Время истечения запроса')

    def __str__(self):
        return f'Подтверждение почты для пользователя: {self.user.username}'

    def send_verification_email(self):
        address = reverse('users:email_verification', kwargs={'code': self.code, 'email': self.user.email})
        full_address = settings.DOMAIN_NAME + address
        subject = f'Подтверждение E-mail для пользователя {self.user.username}'
        message = f'Для того, чтобы подтвердить свой адрес электронной почты, перейдите по ссылке: {full_address}'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email]
        )

    def is_expired(self):
        return True if now() >= self.expiration_time else False

