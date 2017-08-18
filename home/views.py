from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import DetailView

from home.models import Booking
from home.models import Bike

import os
import mimetypes
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper


def download_file(request):
   the_file = 'static/file/name.jpg'
   filename = os.path.basename(the_file)
   chunk_size = 8192
   response = StreamingHttpResponse(FileWrapper(open(the_file, 'rb'), chunk_size), content_type=mimetypes.guess_type(the_file)[0])
   response['Content-Length'] = os.path.getsize(the_file)
   response['Content-Disposition'] = "attachment; filename=%s" % filename
   return response


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)

        bikes = Bike.objects.filter(is_available=True)
        ctx['bikes'] = bikes

        return ctx


class BikeDetailView(DetailView):
    template_name = 'bike_detail.html'
    model = Bike

    def get_context_data(self, **kwargs):
        ctx = super(BikeDetailView, self).get_context_data(**kwargs)
        ctx['booking_success'] = 'booking-success' in self.request.GET
        return ctx


class NewBookingView(CreateView):
    model = Booking
    template_name = 'new_booking.html'

    fields = [
            'customer_name', 'customer_email', 'customer_phone_number',
            'booking_start_date', 'booking_end_date', 'booking_message'
        ]

    def get_bike(self):
        bike_pk = self.kwargs['bike_pk']
        bike = Bike.objects.get(pk=bike_pk)
        return  bike

    def get_context_data(self, **kwargs):
        ctx = super(NewBookingView, self).get_context_data(**kwargs)
        ctx['bike'] = self.get_bike()

        return ctx

    def form_valid(self, form):
        new_booking = form.save(commit=False)
        new_booking.bike = self.get_bike()
        new_booking.is_approved = False

        new_booking.save()

        return super(NewBookingView, self).form_valid(form)

    def get_success_url(self):
        bike = self.get_bike()
        bike_details_page_url = bike.get_absolute_url()

        return '{}?booking-success=1'.format(bike_details_page_url)

