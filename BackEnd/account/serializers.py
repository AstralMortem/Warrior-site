from rest_framework.serializers import ModelSerializer,RelatedField,SlugRelatedField
from .models import BaseUser,Belt,BeltDescription



class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = BaseUser
        fields = "__all__"   

class BeltListSerializer(ModelSerializer):
    class Meta:
        model = Belt
        fields = "__all__"

class BeltDescriptionSerializer(ModelSerializer):
    class Meta:
        model = BeltDescription
        exclude=['id']

class BeltDetailSerializer(ModelSerializer):
    description = BeltDescriptionSerializer(read_only=True)
    class Meta:
        model = Belt
        fields = ['code','title','photo','description']



class UserListSerializer(ModelSerializer):
    belt = BeltListSerializer(many=False)
    class Meta:
        model = BaseUser
        fields = ['id','full_name','photo', 'is_staff','mobile','belt']