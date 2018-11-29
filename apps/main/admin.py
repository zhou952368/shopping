import xadmin
from xadmin import views

# 全局配置

from apps.main.models import Navigation, Shop, User, ShopImage, PropertyValue, SubMenu2, SubMenu, ShopCar, Review, \
    Banner, Category, Order, Property


class BaseStyleSettings:
    # 开启主题修改
    enable_themes = True
    # 使用bootbootstrap主题
    use_bootswatch = True


# 注册自定义全局配置
xadmin.site.register(views.BaseAdminView, BaseStyleSettings)


class GlobalSettings:
    site_title = "商城后台管理"


xadmin.site.register(views.CommAdminView, GlobalSettings)


class NavigationAdmin:
    list_display = ['nav_id', 'nav_name']


xadmin.site.register(Navigation, NavigationAdmin)


class ShopAdmin:
    list_display = ['shop_id', 'name', 'sub_title', 'create_date']
    list_per_page = 20
    search_fields = ['name', 'sub_title']


xadmin.site.register(Shop, ShopAdmin)

# 自定义的admin
from xadmin.plugins import auth


# 显示自定义的方式
class UserAdmin(auth.UserAdmin):
    list_display = ['id', 'username', 'email', 'img_show']


# 先注销
xadmin.site.unregister(User)
# 在注册
xadmin.site.register(User, UserAdmin)


class ShopImageAdmin:
    list_display = ['shop_img_id', 'type']
    list_per_page = 20


xadmin.site.register(ShopImage, ShopImageAdmin)


class PropertyValueAdmin:
    list_display = ['pro_value_id', 'shop', 'property', 'value']
    list_per_page = 20


xadmin.site.register(PropertyValue, PropertyValueAdmin)


# 用户评论
class ReviewAdmin:
    list_dispaly = ['review_id', 'content', 'create_date', 'shop']


xadmin.site.register(Review, ReviewAdmin)


# 轮播图
class BannerAdmin:
    list_display = ['banner_id', 'title', 'image', 'create_time']


xadmin.site.register(Banner, BannerAdmin)


# 分类
class CategoryAdmin:
    list_display = ['cate_id', 'name']


xadmin.site.register(Category, CategoryAdmin)


# 订单管理
class OrderAdmin:
    list_display = ['oid', 'order_code', 'address',
                    'post', 'receiver ', 'mobile', 'user_message', 'create_date', 'pay_date status']


xadmin.site.register(Order, OrderAdmin)


# 商品属性
class PropertyAdmin:
    list_display = ['property_id', 'name', ]


xadmin.site.register(Property, PropertyAdmin)


# 购物车
class ShopCarAdmin:
    list_display = ['car_id', 'number', 'shop', 'user', 'order']


xadmin.site.register(ShopCar, ShopCarAdmin)


# 一级菜单管理
class SubMenuAdmin:
    list_display = ['sub_menu_id', 'name', 'cate']


xadmin.site.register(SubMenu, SubMenuAdmin)


# 二级菜单管理
class SubMenu2Admin:
    list_display = ['sub_menu2_id', 'name', 'sub_menu']


xadmin.site.register(SubMenu2, SubMenu2Admin)
