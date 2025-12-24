from django.shortcuts import render
from django.contrib import auth
from .models import CustomUser, OTP

# # Create your views here.
# def login_register_view(request):
#     if request.method == "POST":
#         phone_number = request.POST.get("phone_number")
#         user, created = CustomUser.objects.get_or_create(phone_number=phone_number)
#         # Here you would typically send an OTP to the user's phone number
#         otp = OTP.objects.create(user=user)
#         # Send OTP to user's phone number (implement with your SMS provider)
#         send_otp_to_phone(phone_number, otp.code)
#         return render(request, "users/enter_otp.html", {"phone_number": phone_number})
#     return render(request, "users/login_register.html")
