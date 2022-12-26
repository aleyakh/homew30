import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Ads, Categories
from users.models import User


def index(request):
    return JsonResponse({"status": "ok"})


class AdsListViews(ListView):
    model = Ads
    queryset = Ads.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('-price')

        paginator = Paginator(self.object_list, 5)
        page_num = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_num)

        ads = [{
            "id": ad.pk,
            "name": ad.name,
            "author": ad.author.username,
            "price": ad.price,
            "description": ad.description,
            "address": [loc.name for loc in ad.author.locations.all()],
            "image": ad.image.url if ad.image else None,
            "is_published": ad.is_published,
            "category_id": ad.category_id.name
        } for ad in page_obj]

        result = {
            "items": ads,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }

        return JsonResponse(result, safe=False)


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
                    "id": ad.id,
                    "name": ad.name,
                    "author": ad.author.username,
                    "price": ad.price,
                    "description": ad.description,
                    "address": [loc.name for loc in ad.author.locations.all()],
                    "image": ad.image.url if ad.image else None,
                    "is_published": ad.is_published,
                    "category_id": ad.category_id.name
                })


@method_decorator(csrf_exempt, name='dispatch')
class AdsCreateView(CreateView):
    model = Ads
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        author = get_object_or_404(User, pk=ad_data["author"])
        category = get_object_or_404(Categories, pk=ad_data["category_id"])

        new_ad = Ads.objects.create(name=ad_data["name"],
                                    price=ad_data["price"],
                                    author=author,
                                    category_id=category,
                                    description=ad_data.get("description"),
                                    is_published=ad_data.get("is_published", False)
                                    )

        return JsonResponse({"id": new_ad.pk,
                             "name": new_ad.name,
                             "author": new_ad.author.username,
                             "price": new_ad.price,
                             "description": new_ad.description,
                             "address": [loc.name for loc in new_ad.author.locations.all()],
                             "is_published": new_ad.is_published,
                             "image": new_ad.image.url if new_ad.image else None,
                             "category_id": new_ad.category_id.name
                             })


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


@method_decorator(csrf_exempt, name='dispatch')
class AdsUpdateView(UpdateView):
    model = Ads
    fields = "__all__"

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)

        if "name" in ad_data:
            self.object.name = ad_data["name"]
        if "price" in ad_data:
            self.object.price = ad_data["price"]
        if "description" in ad_data:
            self.object.description = ad_data["description"]
        if "author_id" in ad_data:
            self.object.author_id = ad_data["author_id"]
        self.object.save()
        return JsonResponse({"id": self.object.pk,
                             "name": self.object.name,
                             "price": self.object.price,
                             "description": self.object.description,
                             "author": self.object.author.username
                             })


@method_decorator(csrf_exempt, name='dispatch')
class AdsDeleteView(DeleteView):
    model = Ads
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        ad = self.get_object()
        ad_pk = ad.pk
        super().delete(request, *args, **kwargs)

        return JsonResponse({"id": ad_pk})


class CategoriesListViews(ListView):
    model = Categories
    queryset = Categories.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('name')
        return JsonResponse(data=[{"id": category.pk, "name": category.name} for category in self.object_list],
                            safe=False)


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
                    "id": category.id,
                    "name": category.name
                })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesCreateView(CreateView):
    model = Categories
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        cat_data = json.loads(request.body)
        new_cat = Categories.objects.create(**cat_data)
        return JsonResponse({"id": new_cat.pk,
                             "name": new_cat.name
                             })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesUpdateView(UpdateView):
    model = Categories
    fields = "__all__"

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        cat_data = json.loads(request.body)
        self.object.name = cat_data["name"]
        self.object.save()
        return JsonResponse({"id": self.object.pk,
                             "name": self.object.name
                             })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesDeleteView(DeleteView):
    model = Categories
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        cat = self.get_object()
        cat_pk = cat.pk
        super().delete(request, *args, **kwargs)

        return JsonResponse({"id": cat_pk})
