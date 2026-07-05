from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import PeopleContact, Apartment, Shop
from api.serializers import PeopleContactSerializer, ApartmentSerializer, ShopSerializer

"""
 - This is api is written using Django regular view with the help of function definition
 - This is approach nothing related to REST framework feature
"""

@csrf_exempt
def people_contacts(request):
    """"
     List and create all the people contacts
    """
    if request.method == 'GET':
        contacts = PeopleContact.objects.all()
        contact_serializer = PeopleContactSerializer(contacts, many=True)
        return JsonResponse(contact_serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PeopleContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)


@csrf_exempt
def people_contacts_details(request, pk):
    try:
        contact = get_object_or_404(PeopleContact, pk=pk)
    except PeopleContact.DoesNotExist:
        return JsonResponse({'error': 'PeopleContact does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        contact_serializer = PeopleContactSerializer(contact)
        return JsonResponse(contact_serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PeopleContactSerializer(contact, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        contact = PeopleContact.objects.get(pk=pk)
        contact.delete()
        return JsonResponse({'success': True}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)


"""
 - REST Framework Feature - Function Based View 
 - request and Response are here the DRF objects not the Django object
 """
@api_view(['GET', 'POST'])
def apartments_list(request):
    if request.method == 'GET':
        apartments = Apartment.objects.all()
        apartment_serializer = ApartmentSerializer(apartments, many=True)
        return Response(apartment_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        apartment_serializer = ApartmentSerializer(data=request.data)
        if apartment_serializer.is_valid():
            apartment_serializer.save()
            return Response(apartment_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(apartment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Method Not Allowed'}, status=405)


@api_view(['GET', 'PUT', 'DELETE'])
def apartments_details(request, pk):
    try:
        apartment = get_object_or_404(Apartment, pk=pk)
    except Apartment.DoesNotExist:
        return Response({'error': 'Apartment does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        apartment_serializer = ApartmentSerializer(apartment)
        return Response(apartment_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        apartment_serializer = ApartmentSerializer(apartment, data=request.data)
        if apartment_serializer.is_valid():
            apartment_serializer.save()
            return Response(apartment_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(apartment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        apartment.delete()
        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)

    else:
        return Response({'error': 'Method Not Allowed'}, status=405)


"""
- REST Framework Feature - Class Based View
- Inheriting APIView class from DRF
"""
class ShopList(APIView):
    """
    List all shops, or create a new shop.
    """

    def get(self, request, format=None):
        shops = Shop.objects.all()
        shop_serializer = ShopSerializer(shops, many=True)
        return Response(shop_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShopDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Shop.objects.get(pk=pk)
        except Shop.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        shop = self.get_object(pk)
        shop_serializer = ShopSerializer(shop)
        return Response(shop_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        shop = self.get_object(pk)
        serializer = ShopSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        shop = self.get_object(pk)
        shop.delete()
        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)
