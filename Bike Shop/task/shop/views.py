from django.views import View
from django.shortcuts import render
from .models import Bike, Order, Basket
from .forms import BikeModelForm
from django.shortcuts import redirect
from django.db.models import F


# Create your views here.

class MainPageView(View):
    def get(self, request, *args, **kwargs):
        bikes = Bike.objects.all()
        return render(request, 'bike/content.html', context={"bikes": bikes})


class BikeView(View):
    form_class = BikeModelForm
    template_name = 'bike/bike_details.html'
    success_url = '/order'

    def get(self, request, pk, *args, **kwargs):
        context = {}
        bike = Bike.objects.filter(id=pk).first()
        context['bike'] = bike
        if all([bike.frame.quantity > 0, bike.seat.quantity > 0, bike.tire.quantity > 1]):
            context['bike_form'] = BikeModelForm()
            context['bike_form_available'] = True
        else:
            context['bike_form_available'] = False

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            bike_pk = self.kwargs['pk']
            bike = Bike.objects.filter(id=bike_pk).first()
            print(bike.seat.quantity)
            bike.frame.quantity -= 1
            bike.seat.quantity -= 1
            bike.tire.quantity -= 2
            if bike.has_basket:
                Basket.objects.update(quantity=F('quantity') - 1)
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            phone_number = form.cleaned_data['phone_number']
            order = Order.objects.create(
                bike=bike,
                name=name,
                surname=surname,
                phone_number=phone_number
            )
            order.save()
            bike.seat.save()
            bike.tire.save()
            bike.frame.save()
            bike.save()

            print(bike.seat.quantity)

            return redirect('success', order_no=order.pk)


class SuccessDetailsView(View):
    def get(self, request, *args, **kwargs):
        order_no = self.kwargs['order_no']
        return render(request, 'bike/success.html', {"order_no":order_no})
