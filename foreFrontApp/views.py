from django.shortcuts import redirect, render
from foreFrontApp.forms import *
from django.contrib import messages
from json import dumps
# Create your views here.
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from foreFrontApp.models import *



def error_404_view(request,exception):
    return render(request, '404.html')

def error_500_view(request):
    return render(request, '500.html')


def index(request):
    news = News.objects.all()
    try:
        sub_form = subscribeForm()
        if request.method == 'POST':
            form = ContactUsForm(request.POST)
            if form.is_valid():
                form.save()
                #message = "Your Form Has Been Sent Successfully !!!"
                #message = dumps(message)
                messages.success(
                    request, "We received your email and will received shortly...")
                name = request.POST['name']
                email = request.POST['email']
                subject = request.POST['subject']
                message = request.POST['message']
                send_mail(subject, message, settings.EMAIL_HOST_USER,
                        [email], fail_silently=False)
                request.session["name"] = name
                return redirect('home')
            else:
                name = request.POST['name']
                messages.error(
                    request, "Invalid Contact Information..Please Try Again...")
                url = "#contact"
                url = dumps(url)
                request.session['name'] = name
                return render(request, 'index.html', {'form': form, 'url': url, 'sub_form': sub_form, 'news': news})
        form = ContactUsForm()
        context = {
            'form': form,
            'sub_form': sub_form,
            'news': news
        }
        return render(request, 'index.html', context)
    except:
        return render(request, 'index.html', context)


def about_us(request):
    try:

        sub_form = subscribeForm()
        context = {
            'sub_form': sub_form,
        }
        return render(request, 'about-us.html', context)
    except:
        pass


def news_details(request, id):
    try:
        news = News.objects.get(id=id)
        sub_form = subscribeForm()
        context = {
            'sub_form': sub_form,
            'news': news
        }

        return render(request, 'news-details.html', context)
    except:
        pass


def subscribe(request):
    try:
        sub_email = request.POST['email']
        get_subscriber, create_subscriber = NewsTeller.objects.get_or_create(
            email=sub_email)
        if create_subscriber:
            messages.success(request, "Thanks for subscribing our website....")
        else:
            messages.error(request, "You already subscribed our website...")
        return redirect('home')
    except:
        pass



