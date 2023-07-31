from django.db import models
from django.contrib.auth.models import User



# Create your models here.

#class Deposit for the deposited mney

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    interest = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Investment by {self.user} - ${self.deposit}"
    

def add_deposit(self, new_deposit):
    self.deposit += new_deposit
    self.save()
    return self.total_deposit



    
