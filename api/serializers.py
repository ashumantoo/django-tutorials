from rest_framework import serializers

from api.models import PeopleContact, Apartment, Shop, ShopItem


class PeopleContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleContact
        # fields = '__all__' if you want to serialize all the fields of the model
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'gender', 'date_of_birth', 'note', 'is_active']


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['id', 'name', 'email', 'phone', 'address', 'total_flats', 'amenities', 'construction_date',
                  'is_available']


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'email', 'phone', 'address', 'category', 'open_date', 'selling_items',
                  'operating_hours',
                  'operating_days', 'created_at', 'updated_at']


class ShopItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopItem
        fields = ['id', 'shop', 'name', 'price', 'quantity', 'manufacture_date', 'expiry_date', 'created_at',
                  'updated_at', 'is_available']
