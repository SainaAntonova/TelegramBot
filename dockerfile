FROM python:3.10-slim
ENV TOKEN='6920243355:AAFcTjFdwkuVG1_EiIsw2ZCwn7OXpU2MjgE'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]