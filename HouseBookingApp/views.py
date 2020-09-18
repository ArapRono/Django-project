from django.shortcuts import render
from client.models import Houses

# Create your views here.
def home(request):
    if request.method == "POST":
        
        houses = Houses.objects.all()
        more = True
        house_id = int(request.POST["more_info"]) 
        print("The primary key is : {} ".format(house_id))
        print(type(house_id))
       
        return render(request, "index.html", {"houses": houses, "is_clicked": more, "houses_id": house_id})

    else:
        more = False
        houses = Houses.objects.all()
    
        return render(request, "index.html", {"houses": houses ,"is_clicked": more})       
def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")

