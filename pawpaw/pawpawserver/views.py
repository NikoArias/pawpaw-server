from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pawpawserver.models import TimeSeriesDatum, Instrument
from pawpawserver.serializers import TimeSeriesDatumSerializer,InstrumentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt





def papaw_index(request):
    return JsonResponse(data = "Welcome.", safe=False)

@api_view(['GET', 'POST'])
def pawpaw_tsd(request):
    if request.method == 'GET':
        TimeSeriesData = TimeSeriesDatum.objects.all()
        serializer = TimeSeriesDatumSerializer(TimeSeriesData, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TimeSeriesDatumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def pawpaw_instrument(request):
    if request.method == 'GET':
        instruments = Instrument.objects.all()
        serializer = InstrumentSerializer(instruments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InstrumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def instrument_detail(request, pk):
    try:
        instrument = Instrument.objects.get(pk=pk)
    except Instrument.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = InstrumentSerializer(instrument)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InstrumentSerializer(instrument, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        instrument.delete()
        return HttpResponse(status=204)

@csrf_exempt
def tsd_detail(request, pk):
    try:
        instrument = Instrument.objects.get(pk=pk)
    except Instrument.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = InstrumentSerializer(instrument)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InstrumentSerializer(instrument, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        instrument.delete()
        return HttpResponse(status=204)
