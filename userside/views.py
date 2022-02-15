from django.shortcuts import render
from django.db.models import Max, Avg, Min

from api.models import Cpu


def index(request):
    cpu_list = Cpu.objects.all().order_by('-id')[:100]
    cpu_all = Cpu.objects.all().order_by('-id')
    context = {'cpu_list': cpu_list,
               'cpu_list_max': round(cpu_list.aggregate(Max('load')).get('load__max'), 2),
               'cpu_list_min': round(cpu_list.aggregate(Min('load')).get('load__min'), 2),
               'cpu_list_avg': round(cpu_list.aggregate(Avg('load')).get('load__avg'), 2),
               'cpu_all_max': round(cpu_all.aggregate(Max('load')).get('load__max'), 2),
               'cpu_all_min': round(cpu_all.aggregate(Min('load')).get('load__min'), 2),
               'cpu_all_avg': round(cpu_list.aggregate(Avg('load')).get('load__avg'), 2),
               }
    return render(request, 'index.html', context)
