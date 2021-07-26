Deploying the application
# Configure the Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
# Run Django migrations
python manage.py migrate
# Create Django superuser (follow prompts)
python manage.py createsuperuser
# Run the dev server
python manage.py runserver


API documentation.

Administrator(Basic Auth)

1. Create poll
POST http:///localhost:8000/api/polls 
{
"poll":{
	"name":->str,
	"description":->str,
	"start_date":->datetime.date,
	"end_date":->datetime.date
	}
}

2. Update poll
PUT http:///localhost:8000/api/polls/{poll_id}
{
"poll":{
	"end_date":->datetime.date
	}
}

3. Delete poll
DELETE http:///localhost:8000/api/polls/{poll_id}

4. Create question
POST http:///localhost:8000/api/questions 
{
"question":{
	"text":->str,
	"q_type":->str,
	"poll_id":->int
	}
}

5. Update question
PUT http:///localhost:8000/api/questions/{question_id}
{
"question":{
	"text":->str,
	}
}

6. Delete question
DELETE http:///localhost:8000/api/questions/{question_id}

7. Get list of polls
GET http:///localhost:8000/api/polls 

User

1. Get active polls
GET http:///localhost:8000/api/active_polls

2. Create answer
POST http:///localhost:8000/api/answers 
{
"answer":{
	"user_id":->int,
	"question":->int,
	"answer":->str
	}
}

3. Update answer
PUT http:///localhost:8000/api/answers/{answer_id}
{
"answer":{
	"answer":->str,
	}
}

4. Delete question
DELETE http:///localhost:8000/api/answers/{answer_id}

5. Get user answers
GET http:///localhost:8000/api/answers/{user_id}