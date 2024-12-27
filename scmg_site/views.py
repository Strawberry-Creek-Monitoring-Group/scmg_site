from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from django.shortcuts import render, redirect
from .forms import ItemForm

class ItemList(APIView):
    def get(self, request):
        items = Item.objects.all()  # Get all items from the database
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new item to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def item_create_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new item to the database
            return redirect('item_list')  # Redirect to a page after saving
    else:
        form = ItemForm()

    return render(request, 'item_create.html', {'form': form})