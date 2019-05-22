from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django import forms
from .models import work
from datetime import datetime
from django.contrib.auth.decorators import login_required

class formdata(forms.Form):
    info=forms.CharField()

@login_required
def home(request):

    form=formdata(request.POST or None)
    
    if form.is_valid():
        data=form.cleaned_data

        obj=work()
        obj.info=data['info']
        obj.user=request.user
        obj.date_time=datetime.now()
        obj.save()
    
    try:
        qs=work.objects.filter(user=request.user)
        context={'objlist': qs}
        return render(request,"home.html",context)

    except:
        raise Http404

@login_required
def remove(request,objid):
    try:
        work.objects.filter(user=request.user).filter(id=objid).delete()
        return(home(request))

    except:
        return HttpResponseRedirect('')




