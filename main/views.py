from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def flight_tap(request):
    return render(request, 'main/flight_tap.html')

def place_share(request):
    return render(request, 'main/place_share.html')

def drone_trading(request):
    return render(request, 'main/drone_trading.html')

def kakaotalk_chat(request):
    return render(request, 'main/kakaotalk_chat.html')