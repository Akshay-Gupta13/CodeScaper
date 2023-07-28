from django.db import models
 
# Create your models here.
class test_case(models.Model):
    tc_input = models.CharField(max_length=200)
    tc_output = models.CharField(max_length=200)
#  maybe count of test aslo added as t, n then x,y,z

class Problem(models.Model): 
    TOUGHNESS = (('Easy', 'Easy'),('Medium', 'Medium'),('Hard', 'Hard'))                   
    STATUS = (('Unsolved', 'Unsolved'),('Solved', 'Solved'))               
    problem_id = models.IntegerField(primary_key=True)                                 
    problem_name = models.CharField(max_length=200)   #question category bhi add karna hai
    problem_description = models.TextField()  
    problem_difficulty = models.CharField(max_length=20, choices=TOUGHNESS)
    problem_timelimit = models.IntegerField(default=2,help_text="in seconds")
    problem_memorylimit = models.IntegerField(default=8,help_text="in MB")
    test_cases = models.ManyToManyField(test_case)                                            
    # testcase bhi add karna hai                                                                                
    # problem_category = models.CharField(max_length=50)

class Submissions(models.Model):
        user_name = models.CharField(max_length=50)
        problem_id = models.IntegerField(primary_key=True)
        problem_name = models.CharField(max_length=200)
        submission_time = models.DateTimeField(auto_now_add=True)
        language_used = models.CharField(max_length=10)
        input_code = models.TextField()
        verdict_user = models.CharField(max_length=120)