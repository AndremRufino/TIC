from main.models import CreateUser, Login, Address
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json

def validator(request) -> bool: 
    received_data = json.loads(request.body)
    login_data = Login.objects.filter(username=received_data['username'])
    return False if len(login_data) == 0 else True
# Create your views here.

@api_view(["GET"])
def login(request) -> HttpResponse: # username and password
    user_exists = validator(request=request)
    received_data = json.loads(request.body)
    if user_exists == True:
        try:
            data = Login.objects.filter(username = received_data['username']).first()
        except:
            return HttpResponse(
                json.dumps({"error":"try again later"}),
                content_type='application/json',
                status=200)
        else:
            if received_data['password'] == data.password:
                #Colocar o redirect da pg HTML
                return HttpResponse(
                    json.dumps({"message":"Successfully logged"}),
                    content_type="application/json",
                    status=200)
            else:
                return HttpResponse(
                    json.dumps({"message":"Incorrect password"}),
                    content_type="application/json",
                    status=203)
    else:
    #Fazer o redirect da página p/ pagina de cadastro
        return HttpResponse(
            json.dumps({"message":"Unregistered user"}),
            content_type="application/json",
            status=200
        )

@api_view(['POST'])
def create_user(request) -> HttpResponse: # All data
    received_data = json.loads(request.body)
    all_users = Login.objects.filter(username=received_data['username']).first()
    valid_cpf = CreateUser.objects.filter(cpf=received_data['cpf'])
    valid_email = CreateUser.objects.filter(email=received_data['email'])
    if len(valid_cpf) != 0:
        return HttpResponse(
                json.dumps({"message":"CPF already cadastred"}),
                content_type="application/json",
                status=200
            )
    if len(valid_email) != 0:
         return HttpResponse(
                json.dumps({"message":"e-mail already cadastred"}),
                content_type="application/json",
                status=200
            )
    if all_users != None:
        if all_users.username == received_data['username']:
            return HttpResponse(
            json.dumps({"message":"Username already used"}),
            content_type="application/json",
            status=203)
    else: 
        try:
            Login.objects.create(
                username = received_data['username'],
                password = received_data['password']
            )
            login_data = Login.objects.get(username=received_data['username'])
            Address.objects.create(
                user = login_data,
                street = received_data['street'],
                number = received_data['number'],
                complement = received_data['complement']
            )
            address_data = Address.objects.get(user=login_data)
            CreateUser.objects.create(
                initial_data = login_data,
                address = address_data,
                email =received_data['email'],
                phone = received_data['phone'],
                cpf = received_data['cpf'],
            )
        except:
            return HttpResponse(
                json.dumps({"message":"System Error, please try later's"}),
                content_type="application/json",
                status=201)
        else:    
            return HttpResponse(
            json.dumps({"message":"User created with Success!"}),
            content_type="application/json",
            status=201)

@api_view(["PATCH"])
def update_user(request) -> HttpResponse: # All data
    data = validator(request=request)
    received_data = json.loads(request.body)
    if data == True:
        try:
            login_data = Login.objects.get(username=received_data['username'])
            address = Address.objects.filter(user = login_data).update(
                    user = login_data,
                    street = received_data['street'],
                    number = received_data['number'],
                    complement = received_data['complement'])
            CreateUser.objects.filter(cpf=received_data['cpf']).update(
                    initial_data = login_data,
                    address = address,
                    email = received_data['email'],
                    phone = received_data['phone']
            )
        except Exception:
            return HttpResponse(
                json.dumps({"error":Exception}),
                content_type='application/json',
                status=200
            )
        else:
            return HttpResponse(
                json.dumps({"sucess":"sucess"}),
                content_type='application/json',
                status=200)
    else:
        return HttpResponse(
            json.dumps({"Unregistered User","user"}),
            content_type='application/json',
            status=200
        )

def validate_email(request) -> bool:
    received_data =json.loads(request.body)
    data = CreateUser.objects.filter(email=received_data['email'])
    return True if len(data) == 1 else False

@api_view(["DELETE"]) # Body ={"email":"e-mail_data"}
def delete_user(request) -> HttpResponse:
    data = validate_email(request=request)
    received_data = json.loads(request.body)
    user = CreateUser.objects.get(email = received_data['email'])
    if user is not None:
        address = user.address
        address.delete()
        login_data = user.initial_data.username
        Login.objects.get(username=login_data).delete()
        user.delete()
        return HttpResponse(
                json.dumps({"status":"deleted_with_success"}),
                content_type='application/json',
                status=200
                )
    else:
        return HttpResponse(
                json.dumps({"status":"failed_to_delete"}),
                content_type='application/json',
                status=200
                )

