from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError



# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def get_help(request):
    return render(request, 'get_help.html')

@login_required(login_url='/login/')
def alldevice(request):
    new_devices = NewDevices.objects.all()

    context = {
        'newdevices': new_devices
    }

    return render(request, 'alldevice.html', context)


@login_required(login_url='/login/')
def reportDevice(request):
    if request.method == "POST":
        form = ReportedDeviceForm(request.POST)
        if form.is_valid():


            subject = "VME Support"
            body = {
                'device_issue_description': form.cleaned_data['device_issue_description'],
                'device_type': form.cleaned_data['device_type'],
                'device_serial': form.cleaned_data['device_serial'],

            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'mailmasterwebvme@gmail.com', ['mailmasterwebvme@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect(reportDevice)

    form = ReportedDeviceForm()
    return render(request, "reportdevice.html", {'form': form})




def handler404(request, exception):
    return render(request, '404.html')

def myReportedDevices(request):
    myRepoDevices = ReportedDevices.objects.all()
    context = {
        'myRepoDevices': myRepoDevices
    }
    return render(request, 'myReportedDevices.html', context)