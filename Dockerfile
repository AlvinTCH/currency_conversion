# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the entire project directory
COPY . /app

# Install project dependencies
RUN pip install -r requirements.txt

ARG DJANGO_DEBUG
ARG DJANGO_SECRET

ENV DJANGO_DEBUG $DJANGO_DEBUG
ENV DJANGO_SECRET $DJANGO_SECRET

# Expose port
EXPOSE 8000

# Run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]