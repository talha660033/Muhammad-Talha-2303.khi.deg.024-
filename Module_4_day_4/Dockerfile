FROM python:3.8-slim-buster
WORKDIR /home/app/
COPY ./ /home/app/
ENV PYTHONPATH=${PYTHONPATH}:/home/app/
# Configuring the volume
VOLUME /app/todo_data
# Change the DEBUG variable to 0 to run it in production mode and 1 to run in debug mode.
ENV DEBUG=0
COPY requirements.txt .
# Requiremnets.txt is now running in build time.
RUN pip install --no-cache-dir -r requirements.txt  
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000"]
