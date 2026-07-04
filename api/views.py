from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

from api.models import PeopleContact
from api.serializers import PeopleContactSerializer

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
    if request.method == 'GET':
        contact = get_object_or_404(PeopleContact, pk=pk)
        contact_serializer = PeopleContactSerializer(contact)
        return JsonResponse(contact_serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PeopleContactSerializer(data=data)
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
