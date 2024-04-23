from rest_framework import serializers
from .models import Experience, Education, Certification, Skill

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [ 'company', 'title', 'location', 'start_date', 'end_date', 'description' ]

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [ 'university', 'college', 'degree_type', 'degree_field' ]

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = [ 'institution', 'name', 'date_achieved' ]

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [ 'name' ]