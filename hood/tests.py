from django.test import TestCase
from .models import Neighborhood,Profile,Business
from django.contrib.auth.models import User


class Neighborhood_TestCases(TestCase):
    def setUp(self):
        self.user1= User(id=1,username='yan',email='yan@gmail.com',password='1234')
        self.user1.save()
        self.profile = Profile(user_id=1,bio='GRIT',profile_pic='images/default.jpg')
        self.profile.save_profile()
        self.neighborhood =Neighborhood(id=1,name='eASTLANDO', health_department_address='199', health='Dispensary', count='2')
        self.neighborhood.create_neighborhood()
        self.business = Business(id=1, business_name = 'Samaki', business_email='samaki@gmail.com')


    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Neighborhood.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.user1,User))
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.neighborhood,Neighborhood))

    def test_save_method(self):
        self.neighborhood.create_neighborhood()
        all_objects = Neighborhood.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        self.neighborhood.create_neighborhood()
        filtered_object = Neighborhood.objects.filter(name='eASTLANDO')
        filtered_object.delete()
        all_objects = Neighborhood.objects.all()
        self.assertTrue(len(all_objects) == 0)

    def test_display_all_objects_method(self):
        self.neighborhood.create_neighborhood()
        all_objects = Neighborhood.retrieve_all()
        self.assertEqual(all_objects.name,'eASTLANDO')

    def test_update_single_object_property(self):
        self.neighborhood.create_neighborhood()
        filtered_object =Neighborhood.update_occupants('1','2')
        fetched = Neighborhood.objects.get(count='2')
        self.assertEqual(fetched.count,'2')

    def test_find_neighborhood_by_id(self):
        self.neighborhood.create_neighborhood()
        fetched_neighborhood = Neighborhood.find_neighborhood_by_id(1)
        self.assertEqual(fetched_neighborhood.id,1)

    def test_search_by_neighborhood(self):
        self.neighborhood.create_neighborhood()
        fetch_specific = Neighborhood.objects.get(name='eASTLANDO')
        self.assertTrue(fetch_specific.name,'eASTLANDO')
