from django.contrib import admin

from .models import (
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

