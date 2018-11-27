from django.shortcuts import render

from apps.main.models import Navigation, Category, Banner


def index(request):
    nav_list = Navigation.objects.all()
    cate_list = Category.objects.all()
    banner_list = Banner.objects.all()
    for cate in cate_list:
        shops = cate.shop_set.all()
        for shop in shops:
            shop_img = shop.shopimage_set.values_list('shop_img_id', flat=True).first()
        cate.shops = shops
    return render(request, 'index.html', locals())
