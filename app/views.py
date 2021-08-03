from django.shortcuts import render
#from app.models import Sender

# Create your views here.

def index(request):
      return render(request,'index.html')


"""def index(request):
    if request.method == "POST":
        smsfrom = request.POST.get('email')
        smstext = request.POST.get('name')
        recipients = request.POST.get('address')
        sendsms = request.POST.get('mobile')
        index = index(smsfroml=smsfrom, smstext=smstext, recipients=recipients, sendsms=sendsms)
        index.save()
    return render(request, 'index.html')"""

