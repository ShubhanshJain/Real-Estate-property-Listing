from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Property
from .serializers import PropertySerializer, PropertyCreateSerializer
from rest_framework.pagination import PageNumberPagination

class PropertyCreateView(APIView):
    def post(self, request):
        serializer = PropertyCreateSerializer(data=request.data)
        if serializer.is_valid():
            default_user = User.objects.first() # Manually assigning default user to allow anonymous user
            serializer.save(user=default_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PropertySearchView(APIView):
    def get(self, request):
        location = request.query_params.get('location')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        property_type = request.query_params.get('property_type')
        page = request.query_params.get('page', 1)
        limit = request.query_params.get('limit', 10)

        query = Q(status='available')
        if location:
            query &= Q(location__icontains=location)
        if min_price:
            query &= Q(price__gte=float(min_price))
        if max_price:
            query &= Q(price__lte=float(max_price))
        if property_type:
            query &= Q(property_type__iexact=property_type)

        properties = Property.objects.filter(query).order_by('created_at')

        paginator = PageNumberPagination()
        paginator.page_size = limit
        paginated_properties = paginator.paginate_queryset(properties, request)

        serializer = PropertySerializer(paginated_properties, many=True)
        return paginator.get_paginated_response(serializer.data)
