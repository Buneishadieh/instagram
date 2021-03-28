from django.test import TestCase
import datetime as dt
from .models import Profile,Image,Comment
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.Beryl= Profile(profile_photo = 'Cats',bio ='in the rari with no tint', user_id = 1)
    def test_instance(self):
        self.assertTrue(isinstance(self.Beryl,Profile))

    def test_save_method(self):
        self.Beryl.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_method(self):
        self.John.delete_profile
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)


class ImageTestClass(TestCase):
    def setUp(self):
        self.Cats= Image(photo='cats.jpg',image_name='rio',image_caption='cute cats',post_date='2019-07-30 11:30:33.999607+03',likes='t',profile =User.id)
    def test_instance(self):
        self.assertTrue(isinstance(self.cats,Image))

    def test_save_method(self):
        self.Cats.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.Cats.delete_image
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

def tearDown(self):
       Profile.objects.all().delete()
       Comment.objects.all().delete()
       Image.objects.all().delete()
class CommentTestClass(TestCase):
   def setUp(self):
     
        self.new_user = User.objects.create_user("testuser", "secret")

        self.new_profile = Profile(profile_pic='cats.jpg',bio="in the rari with no tint",owner=self.new_user)
        self.new_profile.save()

        self.new_image = Image(pic='cats.jpg',caption="this is a test image", profile='',profile_details=self.new_user)
        self.new_image.save()

        self.new_comment = Comment(
            image=self.new_image, comment_owner=self.new_profile, comment="this is a test comment on a post")

    def test_instance_true(self):
        self.new_comment.save()
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
        Comment.objects.all().delete()

