from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from django.views.decorators.csrf import csrf_exempt

from housing import housing

import json

# Create your views here.
def home(request):
    return render(request,'core/home.html')

@require_http_methods(["GET", "POST"])
@csrf_exempt
def get_results(request):
    if request.is_ajax():
        city_id = request.POST.get('city_id')
        locality_id = request.POST.get('locality_id')
        results=housing.parse_content(city_id,locality_id)
        if results:
            return HttpResponse(json.dumps(results),content_type="application/json")
        else:
            return HttpResponse("Sorry No matching results found",content_type="application/text")
    else:
        return HttpResponse("Failed",content_type="application/json")