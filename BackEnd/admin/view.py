from account.serializers import UserListSerializer
from news.serializers import NewsSerializer
from gyms.serializers import GymSerializer


from news.models import News
from gyms.models import Gym
from django.contrib.auth import get_user_model


from rest_framework.response import Response
from rest_framework.views import APIView

class MainPageView(APIView):
    coaches_q = get_user_model().objects.filter(is_staff=True,is_active=True)[:5]
    participants_q = get_user_model().objects.filter(is_staff=False,is_active=True)[:5]
    gyms_q = Gym.objects.all()[:2]
    news_q = News.objects.filter(is_archived=False)[:5]

    coaches_d = UserListSerializer(coaches_q,many=True)
    participants_d = UserListSerializer(participants_q,many=True)
    gyms_d = GymSerializer(gyms_q, many=True)
    news_d = NewsSerializer(news_q, many=True)

    def get(self,request,*args,**kwargs):
        return Response({
            'coaches': self.coaches_d.data,
            'participants': self.participants_d.data,
            'news': self.news_d.data,
            'gyms': self.gyms_d.data
        })
    
