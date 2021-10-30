from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import RoomSerializer
from .models import Room


@csrf_exempt
def room_list(request):
    try:
        rooms = Room.objects.filter(is_booked=True).all()
    except Room.DoesNotExist:
        return HttpResponse(status=404)

    serializer = RoomSerializer(rooms, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def join_room(request, room_id):
    try:
        room = Room.objects.get(pk=room_id, is_booked=False)
    except Room.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        serializer = RoomSerializer(room, data={"is_booked": True})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def room_detail(request, room_id):
    """
    Retrieve, update or delete a room
    """
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RoomSerializer(room)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RoomSerializer(room, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        room.delete()
        return HttpResponse(status=204)
