from rest_framework.generics import (ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView)
from .serializers import (ListSerializer, DetailsSerializer, UpdateSerializer)
from classes.models import Classroom


# Create your views here.

class ClassList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ListSerializer


class ClassDetails(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = DetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'


class UpdateClass(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'


class CancelClass(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'


class CreateClass(CreateAPIView):
    serializer_class = UpdateSerializer

    def perform_create(self, serializer):
    	serializer.save(teacher=self.request.user)
