from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from authentication.views import router as auth_router
from tasks.views import router as tasks_router

api_v1 = NinjaAPI()


api_v1.add_router("/tasks", tasks_router)
api_v1.add_router("/auth", auth_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api_v1.urls),
]
