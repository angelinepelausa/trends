from django.shortcuts import render

# Create your views here.

def index(request):
    obj=Member.objects.all()
    context={
        "obj":obj,
    }
    return render(request, "index.html", context)