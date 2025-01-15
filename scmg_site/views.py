from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reading
from .serializers import ReadingSerializer
from django.shortcuts import render, redirect
from .forms import ReadingForm

class ReadingList(APIView):
    def get(self, request):
        items = Reading.objects.all()  # Get all items from the database
        serializer = ReadingSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new item to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def reading_create_view(request):
    if request.method == 'POST':
        form = ReadingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new item to the database
            return redirect('reading_list')  # Redirect to a page after saving
    else:
        form = ReadingForm()
    return render(request, 'item_create.html', {'form': form})
