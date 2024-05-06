from django.test import TestCase
from .models import Tire, Frame, Seat, Bike


# Create your tests here.
class BikeTestCase(TestCase):
    def test_tires(self):
        obj = Tire.objects.create(type="Tread", quantity=12)
        self.assertEqual(obj.quantity, 12)

    def test_frame(self):
        obj = Frame.objects.create(color="pink", quantity=24)
        self.assertEqual(obj.color, "pink")

    def test_bike(self):
        tire = Tire.objects.create(type="Tread", quantity=2)
        frame = Frame.objects.create(color="pink", quantity=1)
        seat = Seat.objects.create(color="white", quantity=24)
        name = "Traveller"
        description = 'This is purely a test drive'
        hasBasket = True

        bike = Bike.objects.create(
            tire=tire,
            frame=frame,
            seat=seat,
            name=name,
            description=description,
            has_basket=hasBasket
        )

        self.assertEqual(bike.description, 'This is purely a test drive')
