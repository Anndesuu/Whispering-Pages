from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name = "home"),
    path("home", views.page, name = "page"),
    path("sharerecipe", views.sharerecipe, name = "addrecipe"),
    path("addrecipe", views.addrecipe, name = "add"),
    path('viewrecipe/<int:recipeid>', views.recipe, name = "viewrecipe"),
    path('delete/<int:id>', views.delete, name = "delete"),
    path('update/<int:id>', views.update, name = "update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)