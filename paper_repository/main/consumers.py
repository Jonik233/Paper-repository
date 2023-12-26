from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.core.mail import send_mail
from asgiref.sync import sync_to_async
from .models import Articles

class MyAsyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json.get('action')

        if action == 'new_article':
            # Extract article details
            article_data = text_data_json.get('article')
            # Create a new article in the database
            await self.create_article(article_data)
            # Send an email notification about the new article
            await self.send_email(article_data['title'])

    @sync_to_async
    def create_article(self, article_data):
        # Create and save the new article to the database
        article = Articles.objects.create(
            title=article_data['title'],
            authors=article_data['authors'],
            content=article_data['content'],
            rating_points=article_data['rating_points'],
            publication_date=article_data['publication_date'],
            pdf_file=article_data['pdf_file'],
            field=article_data['field'],
        )
        article.save()

    @sync_to_async
    def send_email(self, article_title):
        # Use Django's send_mail function here
        send_mail(
            'New Article Created',
            f'A new article titled "{article_title}" has been added to the database.',
            'from@example.com',  # Sender's email
            ['to@example.com'],  # List of recipients
            fail_silently=False,
        )