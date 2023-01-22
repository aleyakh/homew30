from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.permissons import IsSelectionOwner, IsAdOwnerOrStaff
from ads.serializers import *


def index(request):
    return JsonResponse({"status": "ok"})


class AdsViewSet(ModelViewSet):
    queryset = Ads.objects.order_by("-price")
    default_serializer = AdsSerializer
    serializer_classes = {
        "list": AdsListSerializer,
        "retrieve": AdsDetailSerializer
    }
    default_permission = [AllowAny()]
    permissions = {
        "retrieve": [IsAuthenticated()],
        "update": [IsAuthenticated(), IsAdOwnerOrStaff()],
        "partial_update": [IsAuthenticated(), IsAdOwnerOrStaff()],
        "destroy": [IsAuthenticated(), IsAdOwnerOrStaff()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):

        categories = request.GET.getlist("cat")
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)

        text = request.GET.get("text")
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get("location")
        if location:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location)

        price_from = request.GET.get("price_from")
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)

        price_to = request.GET.get("price_to")
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class AdsUploadImage(UpdateView):
    model = Ads
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get('image')
        self.object.save()
        return JsonResponse({"id": self.object.pk,
                             "name": self.object.name,
                             "image": self.object.image.url
                             })


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    default_serializer = SelectionSerializer
    serializer_classes = {
        "list": SelectionListSerializer,
        "retrieve": SelectionDetailSerializer,
        "create": SelectionCreateSerializer
    }
    default_permission = [AllowAny()]
    permissions = {
        "create": [IsAuthenticated()],
        "retrieve": [IsAuthenticated()],
        "update": [IsAuthenticated(), IsSelectionOwner()],
        "partial_update": [IsAuthenticated(), IsSelectionOwner()],
        "destroy": [IsAuthenticated(), IsSelectionOwner()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)