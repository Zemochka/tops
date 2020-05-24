from django.shortcuts import render

def home(request):
    return render(request, 'games/home.html')

def codenames(request):
    return render(request, 'games/codenames.html')

def pandemic(request):
    return render(request, 'games/pandemic.html')

def cats(request):
    return render(request, 'games/cats.html')

def plunkingPairs(request):
    return render(request, 'games/plunking-pairs.html')

def spyfall(request):
    return render(request, 'games/spyfall.html')

def ticketToRide(request):
    return render(request, 'games/TtR.html')

def stupidCasual(request):
    return render(request, 'games/stupid-casual.html')

def celestia(request):
    return render(request, 'games/celestia.html')

def citadels(request):
    return render(request, 'games/citadels.html')