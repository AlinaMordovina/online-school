from django.contrib import admin

from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "avatar", "country")
    list_filter = ("country",)
    search_fields = (
        "email",
        "phone",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at", "course", "lesson", "method", "amount",)
    list_filter = ("course", "lesson", "method", "user")
