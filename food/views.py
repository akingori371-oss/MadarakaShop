
from django.shortcuts import render


def display(request):
    result = None

    if request.method == "POST":
        try:
            age = int(request.POST["age"])
            sex = request.POST["sex"]
            weight = float(request.POST["weight"])
            height = float(request.POST["height"])
            activity = float(request.POST["activity"])
        except (KeyError, TypeError, ValueError):
            return render(request, "display.html", {"result": None})

        if sex == "male":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        else:
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

        result = round(bmr * activity)

    return render(request, "display.html", {"result": result})

