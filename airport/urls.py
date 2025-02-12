"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import UserCreateAPIView, UserLoginAPIView
from flights.views import BookingDestroyView, BookingDetailView, BookingUpdateView, FlightsListView, BookingsListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('flight/list/', FlightsListView.as_view(), name='flights-list'),
    path('flight/bookings/', BookingsListView.as_view(), name='bookings-list'),
    path('flight/bookings/<int:booking_id>/', BookingDetailView.as_view(), name='booking-detail'),
    path('flight/bookings/<int:booking_id>/update/', BookingUpdateView.as_view(), name='booking-update'),
    path('flight/bookings/<int:booking_id>/destroy/', BookingDestroyView.as_view(), name='booking-destroy'),


    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('signin/', UserLoginAPIView.as_view(), name='signin'),
    # path('signout/', UserCreateAPIView.as_view(), name='signout'),

]
