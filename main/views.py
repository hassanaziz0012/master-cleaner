from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from main.utils import send_email


# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class CustomerFormView(View):
    def get(self, request, format=None):
        return render(request, "main/customer_form.html")

    def post(self, request, format=None):
        company = request.POST.get('company')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')

        estimator = request.POST.get('estimator')
        quotation = request.POST.get('quotation')
        payment_structure = request.POST.get('payment_structure')
        quotation_date = request.POST.get('quotation_date')


        desc1 = request.POST.get('desc1')
        area1 = request.POST.get('area1')
        price1 = request.POST.get('price1')

        desc2 = request.POST.get('desc2')
        area2 = request.POST.get('area2')
        price2 = request.POST.get('price2')

        desc3 = request.POST.get('desc3')
        area3 = request.POST.get('area3')
        price3 = request.POST.get('price3')

        desc4 = request.POST.get('desc4')
        area4 = request.POST.get('area4')
        price4 = request.POST.get('price4')

        subtotal = request.POST.get('subtotal')
        hst = request.POST.get('hst')
        total = request.POST.get('total')
        price4 = request.POST.get('price4')

        emailreport = request.POST.get('emailreport') # Send PDF to customer if this is 1, otherwise don't send if this is 0.

        send_email(request.POST)

        return JsonResponse({'emailreport': emailreport})