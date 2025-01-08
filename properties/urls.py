from django.urls import path
from .views import PropertyCreateView, PropertySearchView

urlpatterns = [
    path('api/properties', PropertyCreateView.as_view(), name='create_property'),
    path('api/properties/search', PropertySearchView.as_view(), name='search_properties'),
]