from django.db import models

from config import settings


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name="Наименование курса")
    preview = models.ImageField(
        upload_to="materials/courses", blank=True, null=True, verbose_name="Превью"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = (
            "title",
        )


class Lesson(models.Model):
    title = models.CharField(max_length=250, verbose_name="Наименование урока")
    preview = models.ImageField(
        upload_to="materials/lessons", blank=True, null=True, verbose_name="Превью"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    video_link = models.CharField(max_length=500, blank=True, null=True, verbose_name="Ссылка на видео")

    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Курс")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = (
            "title",
        )
