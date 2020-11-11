from django.shortcuts import render, redirect
from client.models import Houses
from django.contrib import messages
from django.core.mail import send_mail
from HouseBookingProject.settings import EMAIL_HOST_USER

# Create your views here.
def home(request):
    if request.method == "POST":    
        houses = Houses.objects.all()
        more = True
        house_id = int(request.POST["more_info"]) 
        return render(request, "index.html", {"houses": houses, "is_clicked": more, "houses_id": house_id})

    else:
        more = False
        houses = Houses.objects.all() 
        return render(request, "index.html", {"houses": houses ,"is_clicked": more})   
    
def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["user_name"].title().strip()
        email = request.POST["your_email"].strip()
        message = request.POST["your_message"].capitalize().strip()
        print(name)
        print(email)
        print(message)
        send_mail(
            name,
            message,
            email,
           [ EMAIL_HOST_USER ],
            fail_silently =False
        )
        return redirect("contact")
    else:
        return render(request, "contact.html")
def search(request):
    if request.method == "POST": 
        keywords = request.POST["keyword"].strip().title()
        my_houses = Houses.objects.all()
        for key_search in my_houses:
            if (keywords[0:4]  in key_search.county.title()) or (keywords[0:4]  in key_search.region.title()) or (keywords[0:4]  in key_search.estate.title()):
                push_details = Houses.objects.all()
                search = True
                slice_keyword = keywords[0:4]
                print("Congratulations! Search found")
                return render(request, "index.html", {"push_details": push_details, "is_search_true":search, "keyword" : slice_keyword})
            continue
        for key_search in my_houses:
            if (keywords[0:4] not in key_search.county.title()) or (keywords[0:4] not in key_search.region.title()) or (keywords[0:4] not in key_search.estate.title()):
            #     #continue
                print("We are not able to get your searches!")
                messages.warning(request, "Sorry! search not found!, kindly try other searches")         
                return redirect("/")
    else:
        houses = Houses.objects.all()
        return render(request, "index.html", {"houses": houses })


