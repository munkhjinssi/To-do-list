from rest_framework import serializers
from .models import Task
 
# Task model iin buh fields iig serialize hiine 
class TaskSerializer(serializers.ModelSerializer):   

	class Meta:
		model = Task
		fields ='__all__'