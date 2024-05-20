from .views import home_view,shop_view,ContactView

from django.urls import path

urlpatterns = [
    path('', home_view, name="home-page"),
    path('shop/',shop_view,name="shop-page"),
    path("contact/",ContactView.as_view(),name="contact-page")
]