
from E_Shopper.Myapp.models import Catagories, cart, products
from django import forms  
from Myapp.models import user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User_data




class User_dataForm(forms.ModelForm):  
    class Meta:  
      model = user  
      fields = "__all__"



class CatagoriesForm(forms.ModelForm):  
    class Meta:  
      model = Catagories  
      fields = "__all__"



class Sub_CatagoriesForm(forms.ModelForm):  
    class Meta:  
      model = Sub_Catagories  
      fields = "__all__"


class productsForm(forms.ModelForm):  
    class Meta:  
      model = products  
      fields = "__all__"



class cartForm(forms.ModelForm):  
    class Meta:  
      model = cart  
      fields = "__all__"


