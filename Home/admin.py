from django.contrib import admin
from Home.models import Employes,Company
# Register your models here.

class emp(admin.ModelAdmin):
    list_display=["E_id","C_id","F_name","L_name","Email","profile_pic"]
admin.site.register(Employes,emp)
admin.site.register(Company)
