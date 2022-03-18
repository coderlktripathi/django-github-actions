from django.test import TestCase
from blog.models import Post

# Create your tests here.
class ModelTesting(TestCase):

    def setUp(self) -> None:
        self.post = Post.objects.create(
            title='django post',
            author='Adam',
            slug='adam-django'
        )
        return super().setUp()

    def test_post_model(self):
        post = self.post
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(str(post), 'django post')
