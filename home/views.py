from django.shortcuts import render
from rest_framework.generics import listapiview
from.rest_framework.response import response
from django.utils.timezone import now
from.models import coupon
class couponvalidation(Apiview):
    def post(self,request):
        code=request.data.get('code')
        if not code:
            return response(
                {"error": "coupon code required"}
                status=status.http_400_bad_request
            )
            today=now().date()
            try:
                coupon=coupon.object.get(
                    code=code,
                    is_active=True,
                    valid_from_lte=today,
                    valid_until__gte=today
                )
                return response(
                    {
                        "success": True,
                        "discount_percentage": coupon.discount_percent


                    },
                    status=status.http_200_ok
                )
                except coupon.doesnotexist:
                    return response(
                        {"error": "invalid or expired coupon"},
                        status=status.http_400_bad_request

                        
                    )
# Create your views here.
