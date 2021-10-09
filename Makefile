clean-run:
	pip install -r sigloChallenge/requirements.txt && \
	python sigloChallenge/SetupDB/create_db.py && \
	python manage.py migrate && \
	python manage.py runserver
run:
	python manage.py runserver