from rest_framework import serializers
from .models import Poll, Question, Answer, Q_TYPE_CHOICES

class PollSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    questions = serializers.StringRelatedField(many=True, read_only=True)
    
    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance

class QuestionSerializer(serializers.Serializer):
    text = serializers.CharField()
    q_type = serializers.ChoiceField(Q_TYPE_CHOICES)
    poll_id = serializers.IntegerField()
    answers = serializers.StringRelatedField(many=True, read_only=True)
    
    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.q_type = validated_data.get('q_type', instance.q_type)
        instance.poll = validated_data.get('poll_id', instance.poll)
        instance.save()
        return instance

class AnswerSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    question_id = serializers.IntegerField()
    answer = serializers.CharField()

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.question = validated_data.get('question_id', instance.question)
        instance.answer = validated_data.get('answer', instance.answer)
        instance.save()
        return instance

class UserAnswerSerializer(serializers.Serializer):
    poll = PollSerializer
    answer = AnswerSerializer