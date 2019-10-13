from django.contrib import admin
from phones.models import Phone, Digma, Xiaomi, Samsung
# Register your models here.

class PhoneAdmin(admin.ModelAdmin):
    pass

class DigmaAdmin(admin.ModelAdmin):
    pass

class XiaomiAdmin(admin.ModelAdmin):
    pass

class SamsungAdmin(admin.ModelAdmin):
    pass

admin.site.register(Phone, PhoneAdmin)
admin.site.register(Digma, DigmaAdmin)
admin.site.register(Xiaomi, XiaomiAdmin)
admin.site.register(Samsung, SamsungAdmin)