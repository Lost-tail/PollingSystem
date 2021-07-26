from django.db import models

Q_TYPE_CHOICES = [
    ('TA', 'Text answer'),
    ('SA', 'Single choice answer'),
    ('MA', 'Multiple choice answer')
]

class Poll(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

class Question(models.Model):
    text = models.TextField()
    q_type = models.CharField(max_length=2, choices=Q_TYPE_CHOICES)
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s)' % (self.text, self.q_type)

class Answer(models.Model):
    user_id = models.IntegerField()
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return '%s' % (self.answer)