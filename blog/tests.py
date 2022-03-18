from django.db import IntegrityError
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

    def test_filter_post_by_author(self):
        author = self.post.author
        posts = Post.objects.filter(author=author)
        self.assertEqual(posts.count(), 1)

    def test_duplicate_slug_not_allowed_in_post(self):
        try:
            _ = Post.objects.create(title='test', author='me', slug=self.post.slug)
        except IntegrityError as ex:
            self.assertTrue('UNIQUE constraint failed: blog_post.slug' in ex.args)
