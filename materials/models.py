from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=250, verbose_name="Наименование урока")
    preview = models.ImageField(
        upload_to="materials/lessons", blank=True, null=True, verbose_name="Превью"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    video_link = models.CharField(max_length=500, blank=True, null=True, verbose_name="Ссылка на видео")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = (
            "title",
        )


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name="Наименование курса")
    preview = models.ImageField(
        upload_to="materials/courses", blank=True, null=True, verbose_name="Превью"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    lessons = models.ManyToManyField(Lesson, blank=True, null=True, verbose_name="Уроки курса")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = (
            "title",
        )
