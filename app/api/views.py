from django.shortcuts import render

from .serializers import ExperienceSerializer, EducationSerializer, CertificationSerializer, SkillSerializer
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet
from .models import Experience, Education, Certification, Skill

class ResumeViewSet(ObjectMultipleModelAPIViewSet):
    querylist = [
        {
            'queryset': Experience.objects.values().order_by('-start_date'),
            'serializer_class': ExperienceSerializer,
            'label': 'experience',
        },
        {
            'queryset': Education.objects.values().order_by('-start_date'),
            'serializer_class': EducationSerializer,
            'label': 'education'
        },
        {
            'queryset': Certification.objects.values().order_by('-date_achieved'),
            'serializer_class': CertificationSerializer,
            'label': 'certification'
        },
        {
            'queryset': Skill.objects.values(),
            'serializer_class': SkillSerializer,
            'label': 'skills'
        }
    ]
