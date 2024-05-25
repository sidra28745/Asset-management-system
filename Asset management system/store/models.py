from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone


class Item(models.Model):
    code=models.CharField(max_length=100,blank=True, null=True)
    name=models.CharField(max_length=250,blank=True, null=True) 
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.code + ' - ' + self.name
    
class IssueItem(models.Model):
        department_choices =(
            ('P.E', 'P.E'),
            ('IT', 'IT'),
            ('Maths', 'Maths'),
            
        )
        item = models.ForeignKey(Item, on_delete=models.CASCADE)
        issued_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
        issued_to = models.CharField(max_length=100)
        department = models.CharField(max_length=30, choices=department_choices)
        issued_date = models.DateTimeField(auto_now_add=True)
        return_date = models.DateField()
        is_returned = models.BooleanField(default=False)
        
        def __str__(self):
            return f'{self.item} - {self.issued_to}'
        
class ReturnItem(models.Model):
        item = models.ForeignKey(Item, on_delete=models.CASCADE)    
        returned_date = models.DateTimeField(default=timezone.now)
        returned_by = models.CharField(max_length=100)
        
        def __str__(self):
            return f'{self.item} - {self.returned_by}'
    

