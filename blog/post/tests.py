from django.test import *
from django.utils import timezone
from post.models import Post
from author.models import User


class PostTest(TestCase):
    def test_create_post(self):
        #create a post
        post = Post()
        post.title = "My post"
        post.post_content = "This is content of a post"
        post.tag = "test tag"
        post.pub_date = timezone.now()
        post.save()
        #checking if we can find post by atributes and so on
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEqual(only_post, post)
        self.assertEqual(only_post.title, "My post")
        self.assertEqual(only_post.post_content, "This is content of a post")
        self.assertEqual(only_post.tag, "test tag")
        self.assertEqual(only_post.pub_date.day, post.pub_date.day)
        self.assertEqual(only_post.pub_date.month, post.pub_date.month)
        self.assertEqual(only_post.pub_date.year, post.pub_date.year)
        self.assertEqual(only_post.pub_date.hour, post.pub_date.hour)
        self.assertEqual(only_post.pub_date.minute, post.pub_date.minute)
        self.assertEqual(only_post.pub_date.second, post.pub_date.second)


class UserTest(LiveServerTestCase):
    def test_login(self):
        u = User(username='john', password='lambda8', name='Janek')
        #get login page
        response = u.get('/login/')
        self.assertEquals(response.statuse_code, 200)
        self.assertTrue('Log in' in response.content)
