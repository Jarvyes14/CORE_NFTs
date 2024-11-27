from django.contrib import admin

# Register your models here.

from .models import NFT, ClaimedNFT

admin.site.register(NFT)
admin.site.register(ClaimedNFT)
