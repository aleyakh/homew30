from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from ads.models import Ads, Categories, Selection
from users.models import User


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'


class AdsDetailSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category_id = SlugRelatedField(slug_field="name", queryset=Categories.objects.all())

    class Meta:
        model = Ads
        fields = '__all__'


class AdsListSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category_id = SlugRelatedField(slug_field="name", queryset=Categories.objects.all())
    locations = serializers.SerializerMethodField()

    def get_locations(self, ad):
        return [loc.name for loc in ad.author.locations.all()]

    class Meta:
        model = Ads
        fields = '__all__'


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class SelectionCreateSerializer(serializers.ModelSerializer):
    owner = SlugRelatedField(read_only=True, required=False, slug_field="username")

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["owner"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionDetailSerializer(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    items = AdsListSerializer(many=True)

    class Meta:
        model = Selection
        fields = "__all__"
