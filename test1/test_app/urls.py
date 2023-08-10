from django.urls import path
from test_app import views

urlpatterns = [
    path('person/', views.PersonListCreateView.as_view()),
    path('person/<int:pk>/', views.PersonRetrieveUpdateDestroyView.as_view()),
    path('group/', views.GroupListCreateView.as_view()),
    path('group/<int:pk>/', views.GroupRetrieveUpdateDestroyView.as_view()),
    path('membership/', views.MembershipListCreateView.as_view()),
    path('membership/<int:pk>/', views.MembershipRetrieveUpdateDestroyView.as_view())
]
