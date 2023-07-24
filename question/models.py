from django.db import models
 
# Create your models here.
class test_case(models.Model):
    tc_input = models.CharField(max_length=200)
    tc_output = models.CharField(max_length=200)
#  maybe count of test aslo added as t, n then x,y,z

class Problem(models.Model):                                   
    problem_id = models.IntegerField(primary_key=True)                                 
    problem_name = models.CharField(max_length=200)   #question category bhi add karna hai
    problem_description = models.TextField()  
    # problem_difficulty = models.CharField(max_length=20)
    problem_attempted = models.BooleanField(default = False)                 
    test_cases = models.ManyToManyField(test_case)                                            
    # testcase bhi add karna hai                                                                                
    # problem_category = models.CharField(max_length=50)