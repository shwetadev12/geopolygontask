from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from mozio_app.models import Provider, ServiceArea
from mozio_app.serializers import (
    ProviderSerializer,
    ServiceAreaSerializer,
    GetPolygonsSerializer
    ) 


class CreateProviderViewSet(APIView):
    
    def post(self, request, format=None):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
            )


class GetProviderViewSet(APIView):
    
    def get(self, request, pk, format=None):
        try:
            provider = Provider.objects.get(pk=pk)
            serializer = ProviderSerializer(provider)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
                )
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UpdateProviderViewSet(APIView):
    
    def put(self, request, pk, format=None):
        try:
            provider = Provider.objects.get(pk=pk)
            serializer = ProviderSerializer(provider, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                    )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class DeleteProviderViewSet(APIView):
    
    def get(self, request, pk, format=None):
        try:
            provider = Provider.objects.get(pk=pk)
            provider.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateServiceAreaViewSet(APIView):
    
    def post(self, request, format=None):
        serializer = ServiceAreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
            )


class GetServiceAreaViewSet(APIView):
    
    def get(self, request, pk, format=None):
        try:
            service_area = ServiceArea.objects.get(pk=pk)
            serializer = ServiceAreaSerializer(service_area)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
                )
        except ServiceArea.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UpdateServiceAreaViewSet(APIView):
    
    def put(self, request, pk, format=None):
        try:
            service_area = ServiceArea.objects.get(pk=pk)
            serializer = ServiceAreaSerializer(service_area, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                    )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
        except ServiceArea.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class DeleteServiceAreaViewSet(APIView):
    
    def get(self, request, pk, format=None):
        try:
            service_area = ServiceArea.objects.get(pk=pk)
            service_area.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ServiceArea.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class GetPolygonsViewSet(APIView):
    
    def get(self, request, format=None):
        lat = request.query_params.get("lat", None)
        lng = request.query_params.get("lng", None)
        polygons_list = ServiceArea.objects.all()
        matched_polygon = []
        for polygon in polygons_list:
            for coordinate in polygon.polygon['coordinates'][0]:
                if lat in coordinate and lng in coordinate:
                    matched_polygon.append(polygon)

        if matched_polygon:
            return Response(
                matched_polygon,
                status=status.HTTP_200_OK
                )
        return Response(status=status.HTTP_404_NOT_FOUND)
