from django.test import TestCase
from django.db.models import CharField
from django.urls import reverse
from .models import Sentiment
from .admin import AdminSentimentModelList

class SentimentTest(TestCase):
    def define_data(self, word = 'love', sentiment ='Good'):
        return Sentiment.objects.create(word='word', sentimant='sentment')

    def test_should_have_field(self):
        wordfield = Sentiment._meta.get_field('word')
        sentimetfield = Sentiment._meta.get_field('sentiment')

        self.assertTrue(isinstance(sentimetfield, CharField))
        self.assertTrue(isinstance(wordfield, CharField))

class SentimentTestView(TestCase):
    def test_get_status_is_success(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)

    def test_should_call_index_template(self):
        response = self.client.get(reverse('index'))

        self.assertTemplateUsed(response, 'index.html')

    def test_should_show_text_django(self):
        response = self.client.get(reverse('index'))

        self.assertContains(response, 'django')

class AdminClass(TestCase):
    def test_should_get_view(self):
        expected = ['word', 'sentiment']

        self.assertEqual(AdminSentimentModelList.list_view, expected)

    def test_should_get_filter(self):
        expected = ['word']

        self.assertEqual(AdminSentimentModelList.list_filter, expected)
