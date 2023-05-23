from django.shortcuts import render
from django.http import HttpResponse
import joblib


def home(request):
    return render(request,'home.html')

def result(request):

    cls = joblib.load('tourProject')

    lis = []

    lis.append(request.POST.get('customer_id'))
    lis.append(request.POST.get('age'))
    lis.append(request.POST.get('City Tier'))
    lis.append(request.POST.get('Duration Of Pitch'))
    lis.append(request.POST.get('Occupation'))
    lis.append(request.POST.get('Gender'))
    lis.append(request.POST.get('no_person_visiting'))
    lis.append(request.POST.get('Product Pitched'))
    lis.append(request.POST.get('Preffered Property Star'))
    lis.append(request.POST.get('Passport'))
    lis.append(request.POST.get('own_vehicle'))
    lis.append(request.POST.get('Number Of Children Visiting'))
    lis.append(request.POST.get('Monthly Income'))

    # id = request.POST.get('Monthly Income')
    # return HttpResponse(id)

    
    

    ans = cls.predict([lis])


    # return HttpResponse([lis])
    return render(request,'result.html',{'ans':ans})
