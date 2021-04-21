from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pawpawserver.models import TimeSeriesDatum, Instrument
from pawpawserver.serializers import TimeSeriesDatumSerializer,InstrumentSerializer
from django.http import HttpResponse, JsonResponse





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
