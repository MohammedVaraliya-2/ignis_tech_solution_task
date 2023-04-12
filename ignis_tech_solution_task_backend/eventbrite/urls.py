from django.urls import path
from .views import RegisterAPIView, LoginAPIView, EventListAPIView, CreateEventAPIView, ToggleEventLikeAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('events/', EventListAPIView.as_view(), name='event_list'),
    path('events/create/', CreateEventAPIView.as_view(), name='event_create'),
    path('events/<int:pk>/like/', ToggleEventLikeAPIView.as_view(), name='event_like'),
]
