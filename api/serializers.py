from rest_framework import serializers

from api.models import PeopleContact, Apartment


class PeopleContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleContact
        # fields = '__all__' if you want to serialize all the fields of the model
        fields = ['id','first_name', 'last_name', 'email', 'phone', 'gender', 'date_of_birth', 'note','is_active']

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['id','name', 'email', 'phone','address','total_flats', 'amenities','construction_date','is_available']