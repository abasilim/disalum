from django.test import TestCase
from alumniapp.models import User, School

# Create your tests here.
class Test_Create_School(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='test_user1', password="123456789!")
        test_school_name = School.objects.create(school_name='Madonna')
        test_School = School.objects.create(school_name='Madonna', 
                   adress="Nnobi", user=1, town="Ifite", city='ifi', 
                   lga="me", state="anm", country='Ng' )
    
    def test_school_content(self):
        user1 = User.objects.get(id=1)
        school = School.schoolobj.get(id=1)
        school_name = f'{school.school_name}'
        address = f'{school.address}'
        user = f'{school.user}'
        town = f'{school.town}'
        city = f'{school.city}'
        lga = f'{school.lga}'
        state = f'{school.state}'
        country = f'{school.country}'
        self.assertEqual(school_name, 'Madonna')
        self.assertEqual(address, 'Nnobi')
        self.assertEqual(user, 'test_user1')
        self.assertEqual(town, 'ifite')
        self.assertEqual(city, 'ifi')
        self.assertEqual(lga, 'me')
        self.assertEqual(state, 'anm')
        self.assertEqual(country, 'Ng')
        self.assertEqual(str(school), 'Madonna')



