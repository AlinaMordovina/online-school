from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None

    phone = models.CharField(
        max_length=35, blank=True, null=True, verbose_name="Номер телефона"
    )
    avatar = models.ImageField(
        upload_to="users/avatar", blank=True, null=True, verbose_name="Аватар"
    )
    country = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Страна"
    )

    email = models.EmailField(unique=True, verbose_name="Email")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    CASH = "Наличные"
    TRANSFER = "Перевод"

    METHOD_CHOICES = [
        (CASH, "Наличные"),
        (TRANSFER, "Перевод"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Курс")
    lesson = models.ForeignKey(Lesson, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Урок")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")
    amount = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    method = models.CharField(max_length=50, choices=METHOD_CHOICES, default=TRANSFER, verbose_name="Способ оплаты")
    session_id = models.CharField(max_length=250, blank=True, null=True, verbose_name="Идентификатор сессии")
    payment_link = models.URLField(max_length=500, blank=True, null=True, verbose_name="Ссылка на оплату")

    def __str__(self):
        return f"{self.created_at}: {self.user} {self.amount}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = (
            "created_at",
            "method",
        )
