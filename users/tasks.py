from celery import shared_task

from datetime import timedelta

from django.utils import timezone

from users.models import User


@shared_task
def check_user_activity():
    """Проверяет пользователей на активность за последние 30 дней и блокирует не активных"""

    month = timezone.now() - timezone.timedelta(days=30)
    not_active_users = User.objects.filter(last_login__lt=month)
    for user in not_active_users:
        user.is_active = False
        user.save()
