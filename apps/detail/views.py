from django.shortcuts import render

from apps.main.models import Shop, ShopImage, PropertyValue, Review


def detail(request):
    shop_id = request.GET.get('sid')
    if shop_id:
        try:
            shops = Shop.objects.filter(shop_id=shop_id).values('shop_id', 'promote_price',
                                                                'original_price', 'stock',
                                                                'sub_title', 'name')
            if shops.exists():
                shop = shops.first()
                imgs = ShopImage.objects.filter(shop_id=shop.get('shop_id')).values('shop_img_id', 'type')
                shop.update(imgs=imgs)
                property = PropertyValue.objects.filter(shop_id=shop_id)
                reviews = Review.objects.filter(shop_id=shop_id)
                return render(request, 'detail.html', {'shop': shop, 'property': property, 'reviews': reviews})
        except Exception as e:
            print(e)
    else:
        pass
        # return render(request, 'detail.html')
