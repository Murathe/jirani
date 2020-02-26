from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    jirani_pic = models.ImageField(upload_to = 'images/',default='images/christine.jpg')
    location = models.CharField(max_length=100, null=True)
    posted_by =  models.CharField(max_length=100, null=True)
    count = models.CharField(max_length=100)
    police = models.CharField(max_length=100)
    police_department_address = models.CharField(max_length=100)
    health = models.CharField(max_length=100)
    health_department_address = models.CharField(max_length=100)


    def __str__(self):
        return f' {self.name} Neighborhood'


    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood_by_id(cls,id):
        neighborhood_result = cls.objects.get(id=id)
        return neighborhood_result

    @classmethod
    def update_occupants(cls,current_value,new_value):
        fetched_object = cls.objects.filter(count=current_value).update(count=new_value)
        return fetched_object

    @classmethod
    def update_neighborhood(cls,current_value,new_value):
        fetched_object = cls.objects.filter(count=current_value).update(count=new_value)
        return fetched_object


    @classmethod
    def retrieve_all(cls):
        all_objects = Neighborhood.objects.all()
        for item in all_objects:
            return item


class Business(models.Model):
    business_name = models.CharField(max_length=100, unique= True)
    business_user = models.ForeignKey(User,on_delete=models.CASCADE)
    business_neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    business_email = models.EmailField(max_length=100, unique= True)
    business_pic = models.ImageField(upload_to = 'images/',default='images/christine.jpg')

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()


    @classmethod
    def find_business_by_id(cls,id):
        business_result = cls.objects.get(id=id)
        return business_result


    @classmethod
    def update_business(cls,current_value,new_value):
        fetched_object = cls.objects.filter(business_name=current_value).update(business_name=new_value)
        return fetched_object


    def search_by_business(self, cls,search_term):
        search_result = cls.objects.filter(business_name__icontains=search_term)
        return search_result


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/',default='images/agie.jpg')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, related_name='population')

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def image(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url

    @classmethod
    def search_by_username(cls,search_term):
        search_result = cls.objects.filter(user__username__icontains=search_term)
        return search_result

    def save_profile(self):
        self.save()


class Post(models.Model):
    description =  models.CharField(max_length=70)
    post_image = models.ImageField(upload_to='images/', null=True,blank=True)
    categories = models.CharField(max_length=70)
    time_created =  models.DateTimeField(auto_now=True, null =True)
    location=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
