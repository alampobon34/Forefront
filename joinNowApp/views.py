from django.shortcuts import render, redirect
from joinNowApp.models import *
from joinNowApp.forms import *
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from foreFrontApp.forms import *
# Create your views here.


def join_now(request):
    sub_form = subscribeForm()
    if request.method == 'POST':
        form = joinUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your form has been saved into our database...")
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            sending_email = EmailMessage(
                "join now", phone, settings.EMAIL_HOST_USER, [email])
            sending_email.content_subtype = 'html'
            file = request.FILES['CV']
            sending_email.attach(file.name, file.read(), file.content_type)
            sending_email.send()
            request.session['name'] = name
            return redirect('home')
        else:
            name = request.POST['name']
            request.session['name'] = name
            messages.error(
                request, "Your Information Is Not Saved. Please Try Again..")
            return render(request, 'join-now.html', {'form': form, 'sub_form': sub_form})
    form = joinUsForm()
    context = {
        'form': form,
        'sub_form': sub_form
    }
    return render(request, 'join-now.html', context)
