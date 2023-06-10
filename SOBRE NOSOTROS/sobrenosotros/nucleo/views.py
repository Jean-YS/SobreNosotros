from django.shortcuts import render

from nucleo.models import Grupo


def home(request):
    grupo=Grupo.objects.all().first()
    context={"Nucleo":grupo}
    return render(request,'nucleo/home.html',context)
# Create your views here.
