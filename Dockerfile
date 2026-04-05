FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# We use Gunicorn to run the 'core_site' WSGI application
# --bind 0.0.0.0:8000 tells it to listen on port 8000
# --workers 3 allows it to handle multiple users at once
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "core_site.wsgi:application"]