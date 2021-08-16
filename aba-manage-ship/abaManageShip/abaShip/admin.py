from django.contrib import admin
from django.contrib.auth.models import Permission
from django.utils.html import mark_safe
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ImageItemInlineAdmin(admin.StackedInline):
    model = ImageItem
    fk_name = 'post'

class IDCardInlineAdmin(admin.StackedInline):
    model = IDCard

class OrderIneLineAdmin(admin.StackedInline):
    model = OrderShip


class AuctionInlineAdmin(admin.StackedInline):
    model = Auction
    fk_name = 'post'

class PostForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):

    class Media:
        css= {
            'all': ('/static/css/main.css',)
        }
    list_display = ["description", "weight", "customer"]
    list_filter = ["customer__username", "send_adress", "receive_adress"]
    search_fields = [ "send_adress", "receive_adress", "customer__username"]
    form = PostForm
    inlines = [ImageItemInlineAdmin,  ]


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','username', 'is_active']
    list_filer = ['first_name', 'last_name','username', 'is_active']
    search_fields = ['first_name', 'last_name','username', 'is_active']
    readonly_fields = ['image_avt']
    inlines = [IDCardInlineAdmin]

    def image_avt(self, object):
        return mark_safe("<img src='/static/image/{img_url}' alt='{alt}' width='120px' />".format(
            img_url=object.avatar.name, alt=object.username))


class IDCardAdmin(admin.ModelAdmin):
    list_display = ['user', 'id_card','mfg_date', 'exp_date']
    list_filter = ['user__username', 'id_card','mfg_date', 'exp_date']
    search_fields = ['user__username', 'id_card','mfg_date', 'exp_date']
    readonly_fields = ['img_front', 'img_back',]

    def img_front(self, object):
        return mark_safe("<img src='/static/image/{img_url}' alt='{alt}' width='90px' />".format(
            img_url=object.image_card_front.name, alt=object.id_card
        ))

    def img_back(self, object):
        return mark_safe("<img src='/static/image/{img_url}' alt='{alt}' width='90px' />".format(
            img_url=object.image_card_back.name, alt=object.id_card
        ))


class OrderShipAdmin(admin.ModelAdmin):
    list_display = ['post', 'receive_stock', 'send_stock', 'post__Auction_win', 'active', 'shipper','shipped_date','status']
    list_filter =  ['post', 'receive_stock', 'send_stock', 'active', 'shipper','shipped_date','status']
    search_fields =  ['post__description', 'receive_stock__address', 'send_stock__address', 'active', 'shipper__username','shipped_date','status']
    # inlines =


class AuctionAdmin(admin.ModelAdmin):
    list_display = ['shipper', 'post', 'cost', 'is_win', 'active','created_date']
    list_filter = ['shipper', 'post', 'cost', 'is_win', 'active','created_date']
    search_fields = ['shipper__username', 'post', 'cost', 'is_win', 'active','created_date']
    inlines = [OrderIneLineAdmin,]


class ImageItemAdmin(admin.ModelAdmin):
    list_display = ['post', 'image']
    list_filter = ['post', 'image']
    search_fields = ['post', 'image']
    readonly_fields = ['item',]

    def item(self, object):
        return mark_safe("<img src='/static/image/{img_url}' alt='{alt}' width='90px' />".format(
            img_url=object.image.name, alt=object.image.name
        ))


class AbaShipAdminSite(admin.AdminSite):
    site_header = 'Hệ thống quản lý giao hàng AbaShip'

admin_site  =  AbaShipAdminSite(name='myadmin')




# admin.site.unregister(User)
admin_site.register(User, UserAdmin)
admin_site.register(OrderShip)
admin_site.register(OrderShipDetail)
admin_site.register(Post, PostAdmin)
admin_site.register(ImageItem, ImageItemAdmin)
admin_site.register(Auction, AuctionAdmin)
admin_site.register(Stock)
admin_site.register(CommentShipper)
admin_site.register(Voucher)
admin_site.register(IDCard,IDCardAdmin)
admin_site.register(Permission)
admin_site.register(Deduct)
admin_site.register(DebtApp)
# admin_site.register(Detp)

