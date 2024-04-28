from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView, PaymentUpdateAPIView, PaymentDestroyAPIView, \
    UserRegisterAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name="user_create"),
    path('', UserListAPIView.as_view(), name="user_list"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user_detail"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("<int:pk>/delete/", UserDestroyAPIView.as_view(), name="user_delete"),

    path('payment/create/', PaymentCreateAPIView.as_view(), name="payment_create"),
    path('payment/', PaymentListAPIView.as_view(), name="payment_list"),
    path("payment/<int:pk>/", PaymentRetrieveAPIView.as_view(), name="payment_detail"),
    path("payment/<int:pk>/update/", PaymentUpdateAPIView.as_view(), name="payment_update"),
    path("payment/<int:pk>/delete/", PaymentDestroyAPIView.as_view(), name="payment_delete"),

    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
