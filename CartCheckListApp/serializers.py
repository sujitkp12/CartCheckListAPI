from rest_framework import serializers

from CartCheckListApp.models import CartCheckList, CartCheckListItem


class CartCheckListItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = CartCheckListItem
        fields = '__all__'


class CartCheckListSerializer(serializers.ModelSerializer):
    items = CartCheckListItemSerializer(source='CartChecklistitem_set', many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CartCheckList
        fields = '__all__'