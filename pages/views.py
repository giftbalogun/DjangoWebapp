from django.shortcuts import render, redirect
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices

from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.views.generic import View


def index(request):
    listings = Listing.objects.order_by(
        '-list_data').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'index.html', context)


def about(request):
    listings = Listing.objects.order_by(
        '-list_data').filter(is_published=True)[:3]

    realtors = Realtor.objects.order_by('-hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,

        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }

    return render(request, 'about.html', context)


class SendFormEmail(View):

    def get(self, request):

        # Get the form data
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        message = request.GET.get('message', None)

        # Send Email
        send_mail(
            'Contact Me Form',
            'Hello ' + name + ',\n' + message,
            'blgnbalogun@gmail.com',  # Admin
            [email, 'balogunigift@aol.com',
             'igiftbalogun@icloud.com', 'blgnbalogun53@gmail.com'],
            fail_silently=False,
        )

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.'))
        return redirect('mailme')


def mailme(request):
    listings = Listing.objects.order_by(
        '-list_data').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'contact.html', context)
