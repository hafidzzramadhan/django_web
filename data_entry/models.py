from django.db import models

class Pengguna(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    address_1 = models.TextField()
    address_2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=20)
    state = models.TextField()
    zip_code = models.CharField(max_length=7)
    tanggal_join = models.DateField(auto_now=True)

    def __str__(self):
        return self.email
