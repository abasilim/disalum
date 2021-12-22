from rest_framework import serializers
from users.models  import  NewUser
from alumniapp.models import School

# Serializers

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('id','user_name','first_name', 'email',) #I removed last_name. add later

class schoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'school_name', 'alumni_Name','town', 'state', 'slug',)

# class memberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Member
#         fields = '__all__'
    
# class setSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Set
#         fields = '__all__'
    
# class administratorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Administrator
#         fields = '__all__'

# class profileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'

# class yearSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Year
#         fields = '__all__'