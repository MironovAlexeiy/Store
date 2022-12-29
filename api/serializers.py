from rest_framework import fields, serializers

from products.models import Basket, Category, Products


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())

    class Meta:
        model = Products
        fields = ('id', 'title', 'description', 'price', 'quantity', 'image', 'category')


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    get_sum = fields.FloatField(required=False)
    total_sum = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('id', 'product', 'quantity', 'get_sum', 'created', 'total_sum', 'total_quantity')
        read_only_fields = ('created', )

    def get_total_sum(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_sum()

    def get_total_quantity(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_quantity()
