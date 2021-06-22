from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Login(models.Model):
    class Meta:
        db_table = "login_data"
    
    username = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=50,null=False)

class Address(models.Model):
    class Meta:
        db_table = "address"

    user = models.ForeignKey(Login, null=False, on_delete=CASCADE)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=7)
    complement = models.CharField(max_length=100, null=True)

class CreateUser(models.Model):
    class Meta:
        db_table = "create_user"

    initial_data = models.ForeignKey(Login, null=False, on_delete=CASCADE)
    address = models.ForeignKey(Address, null=False, on_delete=CASCADE)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11,null=False)




