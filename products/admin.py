from django.contrib import admin

from .models import (
                    BackCall,
                    Category,
                    Collection, 
                    Product, 
                    ProductImage,
                    ProductColor,
                    Favorite,
                    AboutUs,
                    AboutUsImage,
                    News,
                    Advantages,
                    PublicOffers,
                    Help,
                    Footer,
                    FloatingButton,
                    )


admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductColor)
admin.site.register(Favorite)
admin.site.register(AboutUs)
admin.site.register(AboutUsImage)
admin.site.register(News)
admin.site.register(Advantages)
admin.site.register(PublicOffers)
admin.site.register(Help)
admin.site.register(Footer)
admin.site.register(FloatingButton)


@admin.register(BackCall)
class BackCallAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'created_at', 'type_of_appeal', 'status_of_call')
    list_filter = ('status_of_call', )
    search_fields = ('number', 'name', )
