from celery import shared_task
from materials.models import Course, Subscription
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


@shared_task
def update_newsletter(course_id):
    """Отправляет письмо подписанным пользователям об обновлении курса"""

    course = Course.objects.get(pk=course_id)
    subscription_list = Subscription.objects.filter(course=course_id)
    subject = f'Обновление курса {course}'
    massage = f'Добрый день! Ознакомьтесь с обновлением курса {course}'
    user_list = []
    for subscription in subscription_list:
        user = subscription.user
        user_list.append(user)
    send_mail(
        subject=subject,
        message=massage,
        from_email=EMAIL_HOST_USER,
        recipient_list=user_list,
    )
