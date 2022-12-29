from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin

from .models import Basket, Category, Products


class IndexVIew(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'


class CatalogListView(TitleMixin, ListView):
    model = Products
    title = 'Store - Каталог'
    template_name = 'products/catalog.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(CatalogListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


@login_required
def basket_add(request, product_id):
    Basket.create_or_update(product_id, request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
