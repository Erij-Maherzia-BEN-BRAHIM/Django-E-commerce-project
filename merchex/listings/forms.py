from django import forms
from listings.models import Fournisseur, Produit
class ContactUsForm(forms.Form):
    name=forms.CharField(required=False)
    email=forms.EmailField()
    message=forms.CharField(max_length=1000)

class FournisseurForm(forms.ModelForm):
    class Meta:
        model =Fournisseur
        fields='__all__'
        
class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields='__all__'