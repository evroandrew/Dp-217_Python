from django.db import models


class Speciality(models.Model):
    name = models.CharField(max_length=50)


class Subspeciality(models.Model):
    name = models.CharField(max_length=50)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='subspecialities')

    def __str__(self):
        return f"{self.name}"


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return f"{self.name}"


class University(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='universities')
    subspecialities = models.ManyToManyField(Subspeciality, related_name='universities')

    def __str__(self):
        return f"{self.name}"