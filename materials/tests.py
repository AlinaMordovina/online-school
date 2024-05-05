from rest_framework.test import APITestCase, APIClient
from users.models import User
from materials.models import Lesson, Course, Subscription
from django.urls import reverse
from rest_framework import status


class MaterialsTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.ru', password='5462')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title='test', owner=self.user)
        self.lesson = Lesson.objects.create(title='test', course=self.course,
                                            video_link='https://www.youtube.com/test',
                                            owner=self.user)

    def test_retrieve_lesson(self):
        url = reverse('materials:lesson_detail', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(data.get("title"), self.lesson.title)

    def test_create_lesson(self):
        url = reverse('materials:lesson_create')
        data = {
            "title": "test lesson",
            "video_link": "https://www.youtube.com/test"
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_update_lesson(self):
        url = reverse('materials:lesson_update', args=(self.lesson.pk,))
        data = {
            "video_link": "https://www.youtube.com/test_test"
        }
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(data.get("video_link"), "https://www.youtube.com/test_test")

    def test_delete_lesson(self):
        url = reverse('materials:lesson_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_list_lessons(self):
        url = reverse('materials:lesson_list')
        response = self.client.get(url)
        data = response.json()
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [{'id': self.lesson.pk,
                               'title': self.lesson.title,
                               'preview': self.lesson.preview,
                               'description': self.lesson.description,
                               'video_link': self.lesson.video_link,
                               'course': self.course.pk,
                               'owner': self.user.pk}]}
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            data,
            result
        )


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.ru', password='5462')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="test", owner=self.user)
        self.subscription = Subscription.objects.create(course=self.course, user=self.user)

    def test_create_subscription(self):
        data = {
            "course": self.course.id,
            "user": self.user.id,
        }
        url = reverse('materials:subscription')
        response = self.client.post(url, data=data)
        data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            data,
            "подписка удалена"
        )