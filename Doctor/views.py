from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Doctor.models import *
# Create your views here.



class AccessView:
    @staticmethod
    @csrf_exempt
    def verify_card(request):
        data = dict(request.POST)
        access = Access.objects.filter(card_uid=data['card_number'])
        if access.exists() and access.count() == 1:
            user = access.first().user
            doctor = Doctor.objects.get(user=user)
            if doctor.checked_in:
                doctor.checked_in = False
                doctor.save()
                return JsonResponse({'status': 'checked_out'})
            else:
                doctor.checked_in = True
                doctor.save()
                return JsonResponse({'status': 'checked_in'})
        else:
            if not access.exists():
                return JsonResponse({'status': 'not_registered'})

            if access.count() > 1:
                return JsonResponse({'status': 'multiple_registered'})

            return JsonResponse({'status': 'error'})

    @staticmethod
    def check_in(request, id):
        doc = Doctor.objects.filter(card_id=id).first()
        if doc and not doc.checked_in:
            doc.checked_in = True
            doc.save()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error'})

    @staticmethod
    def check_out(request, id):
        doc = Doctor.objects.filter(card_id=id).first()
        if doc and doc.checked_in:
            doc.checked_in = False
            doc.save()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error'})

    @staticmethod
    def verify_pin(request):
        pass

    @staticmethod
    def set_card(request):
        pass

    @staticmethod
    def get_data(request):
        data = {}
        docs = Doctor.objects.all()
        for doc in docs:
            x = dict({
                'name': doc.name,
                'pin': 'NA',
                'present': doc.checked_in,
                'id': doc.card_id
            }),
            data[doc.card_id] = x
        print(data)

        return JsonResponse(data)
