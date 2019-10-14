from django.shortcuts import render
from phones.models import Phone, Digma, Xiaomi, Samsung


def show_catalog(request):
    template = 'catalog.html'
    phones_info = []
    digma = Digma.objects.all().select_related('model').first()
    phones_info.append({'name': digma.model.name, 'price': digma.model.price, 'os': digma.model.os, 'ram': digma.model.ram, 'camera': digma.model.camera, 'cpu': digma.model.cpu, 'screen': digma.model.screen, 'max_memory': digma.max_memory, 'fm_radio': digma.fm_radio})
    xiaomi = Xiaomi.objects.all().select_related('model').first()
    phones_info.append({'name': xiaomi.model.name, 'price': xiaomi.model.price, 'os': xiaomi.model.os, 'ram': xiaomi.model.ram, 'camera': xiaomi.model.camera, 'cpu': xiaomi.model.cpu, 'screen': xiaomi.model.screen, 'sim': xiaomi.sim, 'screen_protection': xiaomi.screen_protection, 'dual_camera': xiaomi.dual_camera})
    samsung = Samsung.objects.all().select_related('model').first()
    phones_info.append({'name': samsung.model.name, 'price': samsung.model.price, 'os': samsung.model.os, 'ram': samsung.model.ram, 'camera': samsung.model.camera, 'cpu': samsung.model.cpu, 'screen': samsung.model.screen, 'max_memory': samsung.max_memory, 'sim': samsung.sim})

    context = {
        'phones_info': phones_info
    }
    return render(
        request,
        template,
        context
    )
