from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="Home"),
    path("about", views.about, name="Aboutus"),
    path("contact", views.contact, name="CONTACT_TO_ADMIN"),
    path("search", views.search, name="search"),
    path("view", views.view, name="view"),
]
