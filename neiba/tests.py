from django.test import TestCase


from django.test import TestCase
from .models import Profile,NeighbourHood,Business,Join,Social

# Create your tests here.
class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.mariam= Profile(first_name = 'Mariam', last_name ='Mohammed', email ='umarsamiya@gmail.com')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.mariam,Profile))

       # Testing Save Method
    def test_save_method(self):
        self.mariam.save_user()
        users = Profile.objects.all()
        self.assertTrue(len(users) > 0)

class BusinessTestClass(TestCase):
# Create your tests here.
