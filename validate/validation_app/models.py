from django.db import models



class claim(models.Model):
    claim_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
    	return str(self.claim_text)


class user_validation(models.Model):
    claim_text = models.ForeignKey(claim, on_delete=models.CASCADE)
    related = models.CharField(max_length=15)
    claim = models.CharField(max_length=15)
    def __str__(self):
    	return str(self.claim_text)