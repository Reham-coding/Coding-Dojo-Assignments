from django.db import models
class Dojo  (models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=255) 

    def __repr__(self):
        return f"<Dojo object: Name = {self.name}> , id: {self.id}"  
        
    def getninjas(self):
        return  self.Students.all()

class Ninja  (models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    dojo = models.ForeignKey(Dojo, related_name= "Students", on_delete = models.CASCADE)

    
    def __repr__(self):
        return f"<Student object: Name = {self.lastname}>, firstname= {self.lastname}, dojo =  {self.dojo} "  



