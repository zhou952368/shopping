from django.contrib.auth.models import User
from django.db import models


# 系统扩展表
class UserProfile(models.Model):
    uid = models.AutoField(primary_key=True)
    icon = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    desc = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_profile'


class Address(models.Model):
    detail = models.CharField(max_length=64)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'address'


class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    detail_url = models.CharField(max_length=200)
    order = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'banner'


class Category(models.Model):
    cate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'category'


class Navigation(models.Model):
    nav_id = models.AutoField(primary_key=True)
    nav_name = models.CharField(max_length=64)

    class Meta:
        db_table = 'navigation'


class Order(models.Model):
    oid = models.AutoField(primary_key=True)
    order_code = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    mobile = models.CharField(max_length=11)
    user_message = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    pay_date = models.DateTimeField(blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    confirm_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    uid = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='uid')

    class Meta:
        db_table = 'order'


class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    cate = models.ForeignKey(Category, models.DO_NOTHING)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'property'


class PropertyValue(models.Model):
    pro_value_id = models.AutoField(primary_key=True)
    property_id = models.IntegerField()
    shop_id = models.IntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        db_table = 'property_value'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=4000)
    create_date = models.DateTimeField(blank=True, null=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING)
    uid = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='uid')

    class Meta:
        db_table = 'review'


class Shop(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=255)
    original_price = models.DecimalField(max_digits=7, decimal_places=2)
    promote_price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField()
    cate = models.ForeignKey(Category, models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'shop'


class ShopCar(models.Model):
    car_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    shop = models.ForeignKey(Shop, models.DO_NOTHING)
    uid = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='uid')
    oid = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'shop_car'


class ShopImage(models.Model):
    shop_img_id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, models.DO_NOTHING)
    type = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'shop_image'


class SubMenu(models.Model):
    sub_menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    cate = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        db_table = 'sub_menu'


class SubMenu2(models.Model):
    sub_menu2_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sub_menu = models.ForeignKey(SubMenu, models.DO_NOTHING)

    class Meta:
        db_table = 'sub_menu2'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=64)
    password = models.CharField(max_length=64)
    age = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        db_table = 'user'
