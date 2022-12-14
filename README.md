# fampay_assignment

## Problem Statement 
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

Install mysql and redis in your system.


To Test the api run following commands
1. Clone the repository
```bash
git clone https://github.com/ssmharsh/fampay_assignment.git
```

2. Create a python virtual environment
```bash
python3 -m venv env
```

3. Install requirements 
```bash
pip install requirements.txt
```
Create a .env file to store API_KEY which is youtube api key
Also update mysql credentials in django settings

4. Run django server
```bash
python3 manage.py runserver
```
5. Run celery worker in separate terminal
```bash
python3 -m celery -A assignment worker
```
6. Run celery beat in separate terminal
```bash
python3 -m celery -A assignment beat -l info
```
