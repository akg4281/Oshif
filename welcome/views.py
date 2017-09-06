import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView
from .models import mytable
from  django.http import HttpResponseRedirect
#from django.urls import reverse
# Create your views here.

def index(request):
	
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)
	#var_data = mytable.objects.order_by('name')
	
    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count(),
		'datalist' : mytable.objects.order_by('name')
    })

def health(request):
    return HttpResponse(PageView.objects.count())
	
def savedata(request):
		if request.POST:
		#my_form = MyForm(request.POST)
		#if (my_form.is_valid()):
			name = request.POST.get('name', 'jyoti')
			place= request.POST.get('place', 'ctc')
			var_mydata = mytable(name=name,place=place)
			var_mydata.save();
		return HttpResponseRedirect('/')
		#else:
		#	my_form = MyForm()
		
		#return render(request, 'index.html',{'form': my_form,})
		