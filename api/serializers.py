from rest_framework import serializers

from api.models import PeopleContact


class PeopleContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleContact
        # fields = '__all__' if you want to serialize all the fields of the model
        fields = ['id','first_name', 'last_name', 'email', 'phone', 'gender', 'date_of_birth', 'note','is_active']
