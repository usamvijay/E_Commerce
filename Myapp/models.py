from django.db import models

# Create your models here.

class User_data(models.Model):  
   firstname = models.CharField(max_length=20)
   lastname = models.CharField(max_length=100, null=True)  
   email = models.EmailField( null=True)  
   contact = models.CharField(max_length=15) 
   State = models.CharField(max_length=15) 
   password = models.CharField(max_length=100)  
   # Cpassword = models.CharField(max_length=20)



   
class Meta:  
        db_table = "User_data" 


class Catagories(models.Model):
   catagory = models.CharField(max_length=20)
   created_at=models.DateTimeField( auto_now=True )



class Meta:
   db_table="Catagories"



class Catagory(models.Model):
   
    Cat=models.CharField(max_length=30)

    



class Meta:
   db_table="Sub_Catagories"


class products(models.Model):    
   cat = models.ForeignKey(Catagory, on_delete=models.CASCADE,related_name="catgory")
   title = models.CharField( max_length=25)  
   image = models.ImageField(upload_to='media/images/') 
   offer_price = models.CharField(max_length=20)  
   final_price = models.CharField(max_length=20)  
   Description = models.CharField(max_length=200)  


   
class Meta:  
        db_table = "products" 





class cart(models.Model):    
   user = models.ForeignKey(User_data, on_delete=models.CASCADE,related_name="catgory")
   product = models.ForeignKey(products, on_delete=models.CASCADE,related_name="catgory")
   quantity = models.IntegerField()  
   stattus=models.BooleanField(default=False)
   added_on= models.DateTimeField(auto_now_add=True, null=True)
   updated_on= models.DateTimeField(auto_now_add=True, null=True)

  
class Meta:  
        db_table = "cart" 

   

