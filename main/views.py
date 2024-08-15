from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Cahya Bagus Gautama Gozales',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)