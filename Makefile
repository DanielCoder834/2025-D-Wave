virtual: 
	. ocean/bin/activate

create-virtual: 
	python3.11 -m venv ocean 

example: 
	cd job-shop-scheduling-cqm && python app.py

example-requirements: 
	cd job-shop-scheduling-cqm && pip install -r requirements.txt