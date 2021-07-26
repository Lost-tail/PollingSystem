from datetime import date
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Poll, Question, Answer
from .serializers import PollSerializer, QuestionSerializer, AnswerSerializer

class PollView(APIView):

    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response({"polls": serializer.data})

    def post(self, request):
        poll = request.data.get('poll')
        serializer = PollSerializer(data=poll)
        if serializer.is_valid(raise_exception=True):
            poll_saved = serializer.save()
        return Response({"success": "poll '{}' created successfully".format(poll_saved.name)})

    def put(self, request, pk):
        saved_poll = get_object_or_404(Poll.objects.all(), pk=pk)
        data = request.data.get('poll')
        serializer = PollSerializer(instance=saved_poll, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            poll_saved = serializer.save()
        return Response({
            "success": "poll '{}' updated successfully".format(poll_saved.name)
        })

    def delete(self, request, pk):
        poll = get_object_or_404(Poll.objects.all(), pk=pk)
        poll.delete()
        return Response({
            "message": "poll with id `{}` has been deleted.".format(pk)
        }, status=204)

class QuestionView(APIView):

    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response({"questions": serializer.data})

    def post(self, request):
        question = request.data.get('question')
        serializer = QuestionSerializer(data=question)
        if serializer.is_valid(raise_exception=True):
            question_saved = serializer.save()
        return Response({"success": "question '{}' created successfully".format(question_saved.text)})

    def put(self, request, pk):
        saved_question = get_object_or_404(Question.objects.all(), pk=pk)
        data = request.data.get('question')
        serializer = QuestionSerializer(instance=saved_question, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            question_saved = serializer.save()
        return Response({
            "success": "question '{}' updated successfully".format(question_saved.text)
        })

    def delete(self, request, pk):
        question = get_object_or_404(Question.objects.all(), pk=pk)
        question.delete()
        return Response({
            "message": "question with id `{}` has been deleted.".format(pk)
        }, status=204)

class AnswerView(APIView):

    def get(self, request, pk):
        #answers = Answer.objects.filter(user_id__exact=pk)
        questions = Question.objects.filter(answers__user_id=pk)
        serializer = QuestionSerializer(questions, many=True)
        return Response({"questions": serializer.data})

    def post(self, request):
        answer = request.data.get('answer')
        serializer = AnswerSerializer(data=answer)
        if serializer.is_valid(raise_exception=True):
            answer_saved = serializer.save()
        return Response({"success": "answer '{}' created successfully".format(answer_saved.answer)})

    def put(self, request, pk):
        saved_answer = get_object_or_404(Answer.objects.all(), pk=pk)
        data = request.data.get('answer')
        serializer = AnswerSerializer(instance=saved_answer, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            answer_saved = serializer.save()
        return Response({
            "success": "answer '{}' updated successfully".format(answer_saved.answer)
        })

    def delete(self, request, pk):
        answer = get_object_or_404(Answer.objects.all(), pk=pk)
        answer.delete()
        return Response({
            "message": "answer with id `{}` has been deleted.".format(pk)
        }, status=204)

class ActivePollView(APIView):

    def get(self, request):
        polls = Poll.objects.filter(end_date__gte=date.today())
        serializer = PollSerializer(polls, many=True)
        return Response({"polls": serializer.data})