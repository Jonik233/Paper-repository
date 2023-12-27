import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.mail import send_mail
from asgiref.sync import sync_to_async
from .models import Articles
from registration.models import CustomUser

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
            await self.create_article(article_data)
            
            # Get all user emails
            user_emails = await self.get_all_user_emails()
            for email in user_emails:
                await self.send_email(article_data['title'], email)

    @sync_to_async
    def create_article(self, article_data):
        # Create and save the new article to the database
        article = Articles.objects.create(
            title=article_data['title'],
            authors=article_data['authors'],
            content=article_data['content'],
            publication_date=article_data['publication_date'],
            pdf_file=article_data['pdf_file'],
            field=article_data['field'],
        )
        article.save()


    @sync_to_async
    def get_all_user_emails(self):
        user_emails = CustomUser.objects.values_list('email', flat=True)
        return list(user_emails)
    
    
    @sync_to_async
    def send_email(self, article_title, recipient_email):
        send_mail(
            'New Article Created',
            f'A new article titled "{article_title}" has been published !',
            'vmashtaler5@gmail.com',  # Sender
            [recipient_email],  # List of recipients
            fail_silently=False,
        )