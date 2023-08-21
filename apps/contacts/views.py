from django.shortcuts import render,redirect
from .models import Contacts
from apps.homepage.models import Umka
from apps.telegram.views import get_text

# Create your views here.
def contacts(request):
    umka =  Umka.objects.latest("id")
    contacts = Contacts.objects.latest("id")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        phone = request.POST.get('phone')
        
        review = Contacts.objects.create(name = name, email = email,phone = phone, message = message)

        get_text(f""" Оставлен отзыв для Умки
Имя пользователя: {review.name}
Адрес(email): {review.email}
Номер телефона: {review.phone}
Текст: {review.message}
""")
        return redirect("index")
        
    context ={
        'umka':umka,
        'contacts':contacts,
        
    }
    return render(request, 'contact.html',context)