from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: " + self.name


class CarModel(models.Model):
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    COUPE = 'coupe'
    CONVERTIBLE = 'convertible'
    HATCHBACK = 'hatchback'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (CONVERTIBLE, 'Convertible'),
        (HATCHBACK, 'Hatchback'),
    ]

    dealer_id = models.IntegerField()
    name = models.CharField(null=False, max_length=30, default='')
    car_type = models.CharField(
        max_length=20,
        choices=CAR_TYPES,
        default=SEDAN
    )
    year = models.IntegerField(
        default=2023,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return "Name: " + self.name


