from django.db import models


class Frame(models.Model):
    color = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.color}"


class Seat(models.Model):
    color = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.color}"


class Tire(models.Model):
    type = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.type}"


class Basket(models.Model):
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quantity}"


class Bike(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    has_basket = models.BooleanField()

    # def update_parts(self):
    #     # Decrease the quantity of available bike parts
    #     # based on the ordered bike's components
    #     self.frame.quantity -= 1
    #     self.seat.quantity -= 1
    #     self.tire.quantity -= 2  # Each bike has two tires
    #     if self.has_basket:
    #         Basket.quantity -=1
    #
    #     self.tire.save()
    #
    #     self.save()

    def __str__(self):
        return f"{self.name}"



class Order(models.Model):
    PENDING = 'P'
    READY = 'R'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (READY, 'Ready'),
    ]

    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"{self.status}"


class BikeForm(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)