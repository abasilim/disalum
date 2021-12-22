
#from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils import timezone
#from django_resized import ResizedImageField

#Create your models here.
#class User():
    #pass
    # class Meta:
    #     ordering = ('-date_joined',)


class School(models.Model):
    # defining a custom manager for the school
    class schoolObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(active=True)


    school_name = models.CharField(max_length=255, null=True)
    alumni_Name = models.CharField(max_length=255, null=True, blank=True)
    alumni_name_abbreviation = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True)
    school_logo =models.ImageField(null=True, blank=True)
    national_Logo =models.ImageField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='all_users_of_school', on_delete=models.CASCADE)
    #logo = ResizedImageField(size=[100,120], quality=75, null=True, blank= True, upload_to = 'images/'),
    town = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=50, null=True)
    lga = models.CharField(max_length=255, null=True)
    #zip = models.CharField(max_length=10),
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="User_who_created", on_delete=models.PROTECT)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    confirmed = models.BooleanField(default=False )
    active = models.BooleanField(default=True)

    objects = models.Manager() # default manager
    schoolobj = schoolObject() # custom manager

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.school_name

# class Profile(models.Model):
#     profile = models.ForeignKey(User, null=True, related_name="all_users_profile", on_delete=models.CASCADE)
#     profile_Picture = models.ImageField(null=True)

#     def __str__(self):
#         return self.profile.username
        
# class Year(models.Model):
#     set_year = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.set_year


 
# class Member(models.Model):
#     first_Name = models.CharField(max_length=100, null=True)
#     last_Name = models.CharField(max_length=100, null=True)
#     middle_Name = models.CharField(max_length=100, null=True, blank=True)
#     user_member =models.ForeignKey(User, related_name='all_members', null=True, blank=True, on_delete=models.CASCADE)
#     email = models.EmailField(max_length=255, null=True)
#     school_Name = models.ForeignKey(School, null=True, related_name='school_members', on_delete=models.CASCADE)
#     set_year = models.ForeignKey(Year, null=True, related_name='all_set_years',  on_delete=models.CASCADE)
#     year_Admitted = models.CharField(max_length=10)
#     year_Graduated = models.CharField(max_length=10)
#     profession = models.CharField(max_length=100, null=True, blank=True)
#     occupation = models.CharField(max_length=100, null=True)
#     dob = models.CharField(max_length=50, null=True)
#     school_Position_Then = models.CharField(max_length=255, null=True, blank=True)
#     indepted =models.BooleanField(default=False)
#     active = models.BooleanField(default=True) 
    
#     def __str__(self):
#         return self.first_Name


# class Set(models.Model):
#     set_Name = models.CharField(max_length=255, null=True)
#     school_Name = models.ForeignKey(School, related_name='all_set_in_school', null=True,  on_delete=models.CASCADE)
#     set_year = models.ForeignKey(Year, null=True,  related_name='all_years', on_delete=models.CASCADE)
#     slogan = models.CharField(max_length=100, null=True, blank=True)
#     set_Logo =models.ImageField(null=True, blank=True)
#     branch_Name = models.CharField(max_length=100, null=True, blank=True),
#     date_created = models.DateTimeField(default=timezone.now)
#     members = models.ForeignKey(Member, null=True, related_name="get_school_belonged" , on_delete=models.CASCADE)
    
    
#     def __str__(self):
#         return self.set_Name


# class Administrator(models.Model):
#     administer = models.ForeignKey(User, related_name='leadership', max_length=200, null=True, on_delete=models.CASCADE)
#     school = models.ForeignKey(School, related_name='all_general_leaders', max_length=200, on_delete=models.CASCADE)
#     set = models.ForeignKey(Set, related_name='all_set_leaders', null=True, blank=True, on_delete=models.CASCADE)
#     active = models.BooleanField(default=False)

#     def __str__(self):
#         return self.administer

    

    
    

# class Member(models.Model):
#     first_Name = models.CharField(max_length=100, null=True)
#     last_Name = models.CharField(max_length=100, null=True)
#     middle_Name = models.CharField(max_length=100, null=True)
#     profilePix = models.ImageField(null=True)
#     e_mail = models.EmailField(max_length=255, null=True)
#     schoolName = models.OneToOneField(School,null=True, on_delete=models.CASCADE)
#     yearAdmitted = models.DateTimeField(default=timezone.now)
#     yearGraduated = models.DateTimeField(default=timezone.now)
#     profession = models.CharField(max_length=100, null=True)
#     occupation = models.CharField(max_length=100, null=True)
#     dob = models.CharField(max_length=50, null=True)
#     schoolPositionThen = models.CharField(max_length=255)
#     indepted =models.BooleanField(default=False) 
    
#     def serialize(self, member):
#         return {
#         "member_id": self.member.id,
#         "member_firstName": self.first_Name,
#         "member_lastName": self.last_Name,
#         "member_middlename": self.middle_Name
#         }
    
#     def __str__(self):
#         return self.first_Name


# class Set(models.Model):
#     setName = models.CharField(max_length=255, null=True)
#     schoolName = models.OneToOneField(School, null=True,  on_delete=models.CASCADE)
#     shortName = models.CharField(max_length=100, null=True)
#     slogan = models.CharField(max_length=100, null=True)
#     logoSet =models.ImageField(null=True)
#     #branchName = models.CharField(max_length=100),
#     date_created = models.DateTimeField(default=timezone.now)
#     members = models.ForeignKey(Member, null=True, related_name="get_schhol_belonged" , on_delete=models.CASCADE)
    
#     def serialize(self, setName):
#         return {
#             "set_name_id": self.setName.id
#         }
    
#     def __str__(self):
#         return self.setName

# class National(models.Model):
#     national_name = models.CharField(max_length=255, null=True)
#     shortName = models.CharField(max_length=10, blank=True)
#     schoolName = models.ForeignKey(School, null=True, on_delete=models.CASCADE)
#     set = models.ForeignKey(Set,  null=True, on_delete=models.CASCADE)
#     slogan = models.CharField(max_length=100, null=True)
#     logoNational =models.ImageField(null=True)
#     date_created = models.DateTimeField(default=timezone.now)
#     all_members = models.ForeignKey(Member, null=True, related_name="get_schol", on_delete=models.CASCADE) 



# class Leadership(models.Model):
#     name = models.ForeignKey(Member, null=True, on_delete=models.CASCADE)
#     group_name = models.CharField(max_length=100, null=True)
#     position = models.CharField(max_length=100, null=True)
#     startYear = models.DateTimeField(default=timezone.now)
#     endYear = models.DateTimeField(default=timezone.now)
#     active = models.BooleanField(default=False)
    
    
#     def serialize(self, name):
#         return {
#             "leader_id": self.id
#         }
    
    
#     def __str__(self):
#         return self.name

# class Event(models.Model):
#     eventName = models.CharField(max_length=100),
#     venue =  models.CharField(max_length=100),
#     eventImage = ResizedImageField(size=[100,120], quality=75, null=True, blank=True, upload_to='images/'),
#     dateCreated = models.DateTimeField(),
#     eventDate = models.DateTimeField(),
#     attendance = models.ForeignKey(Member, on_delete=models.CASCADE),
#     active = models.BooleanField(default=True)

#     def serialize(self, eventName):
#         return {
#             "event_id": self.id,
#         }
#     def __str__(self):
#         return self.eventName

# class Contribution(models.Model):
#     event_name = models.ForeignKey(Event, on_delete=models.CASCADE),
#     Contributin_member = models.ForeignKey(Member, related_name="get_all_beneficialries", on_delete=models.CASCADE),
#     amount_donated = models.CharField(max_length=50),
#     datePaid = models.DateTimeField(),
#     amount_paid = models.IntegerField(),
#     balance = models.IntegerField()

#     def serialize(self, contributin_member):
#         return {
#             "contributor_id": self.id,
#         }
    
#     def __str__(self):
#         return f"{self.event_name} - {self.amount_donated}"

# class Fund(models.Model):
#     income = models.ForeignKey(Contribution, related_name="expenses", on_delete=models.CASCADE),
#     receivables = models.ForeignKey(Contribution, on_delete=models.CASCADE)

#     def serialize(self, income):
#         return {
#             "fund_id": self.id,
#         }
    
#     def __str__(self):
#         return f"{self.income} - {self.receivables}"


# class Announcement(models.Model):
#     title = models.CharField(max_length=100),
#     school_name = models.ForeignKey(School, on_delete=models.CASCADE ),
#     set_name = models.ForeignKey(Set, on_delete=models.CASCADE), 
#     anounceImage = models.ImageField(null=True),
#     details = models.CharField(max_length=100),
#     date_posted = models.CharField(max_length=100),
#     poster = models.CharField(max_length=100)
#     active = models.BooleanField(default=True)

#     def serialize(self, title):
#         return {
#             "announcement_id": self.id,
#         }
    
#     def __str__(self):
#         return f"{self.title} - {self.school_name}"

# class Charity(models.Model):
#     charityTitle = models.CharField(max_length=100),
#     school_name = models.ForeignKey(School, on_delete=models.CASCADE),
#     set_name = models.ForeignKey(Set, on_delete=models.CASCADE), 
#     beneficiary = models.CharField(max_length=100),
#     dateGiven = models.DateTimeField(),
#     amount = models.ForeignKey(Fund, on_delete=models.CASCADE)

#     def serialize(self, charityTitle):
#         return {
#             "charity_id": self.id,
#         }
    
#     def __str__(self):
#         return f"{self.charityTitle} - {self.school_name}"

# class Committee(models.Model):
#     event_name = models.ForeignKey(Event, on_delete=models.CASCADE),
#     committe_member = models.ManyToManyField(Leadership, related_name="get_all_committees_a_member_belongs")

#     def serialize(self, commtte_member):
#         return {
#             "committee_id": self.id,
#         }
    
#     def __str__(self):
#         return f"{self.event_name} - {self.committe_member}"

# class Comment(models.Model):
#     post = models.ForeignKey(Announcement, on_delete=models.CASCADE)
#     comment =  models.CharField(max_length=255),
#     author = models.ForeignKey(Member, on_delete=models.CASCADE),
#     likes = models.ManyToManyField(Member, related_name="get_all_likes")
#     date_created = models.DateTimeField(default=timezone.now)




