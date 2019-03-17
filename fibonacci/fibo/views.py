from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import NFibo
from fibo.serializers import NFiboSerializer

""" Calculate nth Fibonacci number by Fast doubling method"""
def calculateFibo(n):
    steps = []
    nc = n
    while(nc):
        steps.append(nc)
        nc //= 2
        if nc == 0:
            arr = [0, 1]
    while(steps):
        pos = steps[-1]
        a = arr[0]
        b = arr[1]
        c = a * (2 * b - a)
        d = a ** 2 + b ** 2
        if pos % 2:
            arr[0], arr[1] = d, c + d
        else:
            arr[0], arr[1] = c, d
        steps.pop()
    return arr[0]

@api_view(['GET'])
def GetFibo(request, num):
    queryset = NFibo.objects.filter(number = num)
    """ If already in DB send else calculate """
    if not queryset:
        fibo_num = calculateFibo(num)
        NFibo.objects.create(number=num, fibo=fibo_num)

    queryset = NFibo.objects.filter(number = num)
    serialized_data = NFiboSerializer(queryset, many=True)
    return JsonResponse(serialized_data.data, safe=False)
