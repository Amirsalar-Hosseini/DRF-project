from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import Person, Question, Answer
from .serializers import PersonSerializer, QuestionSerializer
from permissions import IsOwnerOrReadOnly


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)


class QuestionListView(APIView):
    throttle_scope = 'questions'

    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    """
        Create a new question
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer

    def post(self, request):
        ser_data = QuestionSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = (IsOwnerOrReadOnly,)

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        ser_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = (IsOwnerOrReadOnly,)

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({"message": "question deleted"}, status=status.HTTP_200_OK)