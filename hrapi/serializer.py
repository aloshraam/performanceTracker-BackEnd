from rest_framework import serializers
from hrapi.models import *

class RegistrationSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)

    class Meta:
        model=Hr
        fields=["id","name","username","email_address","password","phoneno","home_address","job_title","position","department","prefferred_timezone","linkedin_profile","skills","certification","experience"]

    def create(self, validated_data):
        return Hr.objects.create_user(**validated_data)
    
    
class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hr
        fields=["name","email_address","phoneno","home_address","job_title","position","department","prefferred_timezone","linkedin_profile","skills","certification","experience"]
            
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=["id","name","email_address","phoneno","home_address","job_title","department","linkedin_profile","manager_name","resume","start_date","in_team"]
        

class TeamleadSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeamLead
        fields=["id","name","email_address","phoneno","home_address","job_title","position","department","prefferred_timezone","linkedin_profile","skills","certification","experience","user_type"]
        

class TeamsSerializer(serializers.ModelSerializer):
    teamlead=serializers.CharField(source='teamlead.name', read_only=True)
    members=serializers.SerializerMethodField()

    def get_members(self, obj):
        return [member.employee.name for member in obj.members.all()]
    
    class Meta:
        model=Teams
        fields="__all__"
        
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields="__all__"
        
        
class ProjectUpdatesSerializer(serializers.ModelSerializer):
    project=serializers.CharField(read_only=True)
    class Meta:
        model=ProjectUpdates
        fields="__all__"


class ProjectAssignSerializer(serializers.ModelSerializer):
    teamlead=serializers.CharField(source='teamlead.name', read_only=True)
    project=serializers.CharField(source='project.topic', read_only=True)
    team=serializers.CharField(source='team.name', read_only=True)
    class Meta:
        model=Project_assign
        fields="__all__"
 
 
class ProjectDetailSerializer(serializers.ModelSerializer):
    projectassigned=serializers.CharField(source='projectassigned.topic', read_only=True)
    teamlead=serializers.CharField(source='teamlead.name', read_only=True)
    assigned_person=serializers.CharField(source='assigned_person.name', read_only=True)
    class Meta:
        model=ProjectDetail
        fields="__all__"
        
        
class TaskChartSerializer(serializers.ModelSerializer):
    project_detail=ProjectDetailSerializer()
    assigned_person=serializers.CharField(source='assigned_person.name', read_only=True)
    project_name=serializers.CharField(source='project_detail.projectassigned.project', read_only=True)  #new field for project name
    class Meta:
        model=TaskChart
        fields="__all__"
        

class TaskUpdatesChartSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskUpdateChart
        exclude=('task','updated_by')
    
    
class PerformanceTrackSerializer(serializers.ModelSerializer):
    hr=serializers.CharField(read_only=True)
    performance=serializers.CharField(read_only=True)
    class Meta:
        model=Performance_assign
        fields="__all__"
        
        
class PerformanceTrackViewSerializer(serializers.ModelSerializer):
    hr=serializers.CharField(read_only=True)
    employee=serializers.CharField(source='employee.name', read_only=True)
    class Meta:
        model=Performance_assign
        fields="__all__"
        

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Meeting
        fields=["title","link","date","time"]
        

class MeetingListSerializer(serializers.ModelSerializer):
    organizer=serializers.CharField(read_only=True)
    class Meta:
        model=Meeting
        fields="__all__"
        
        
class ReviewSerializer(serializers.ModelSerializer):
    teamlead=serializers.CharField(read_only=True)
    emp=serializers.CharField(read_only=True)

    class Meta:
        model=Rating
        fields="__all__"

class PerformanceTrackSerializer2(serializers.ModelSerializer):
    
    class Meta:
        model=Performance_assign
        fields=["teamlead","performance","teamlead",]

# serializers.py
from rest_framework import serializers
from .models import DailyTask, Employee, TeamLead

class EmployeeMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name']

class TeamLeadMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamLead
        fields = ['id', 'name']