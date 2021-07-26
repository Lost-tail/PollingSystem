from django.urls import path
from .views import PollView, QuestionView, AnswerView, ActivePollView

urlpatterns = [
    path('polls/', PollView.as_view()),
    path('active_polls/', ActivePollView.as_view()),
    path('polls/<int:pk>', PollView.as_view()),
    path('questions/', QuestionView.as_view()),
    path('questions/<int:pk>', QuestionView.as_view()),
    path('answers/', AnswerView.as_view()),
    path('answers/<int:pk>', AnswerView.as_view()),
    path('useranswers/<int:user_id>', AnswerView.as_view())
]