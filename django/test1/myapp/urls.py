from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<int:page>", views.viewArticle, name="page"),
    path("article/<int:page>/<int:id>", views.viewArticle2, name="page/id"),
]
