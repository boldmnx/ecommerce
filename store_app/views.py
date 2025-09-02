from django.shortcuts import render


def baraa_burtgel(request):
    return render(request, "baraa/baraaBurtgel.html", {"baraa": "tsunh"})
