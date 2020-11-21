from django import forms
from .models import ProcessCatalogue

class ProcessGroupForm(forms.Form):
    group_name=forms.CharField(max_length=100)
    group_description=forms.CharField(max_length=5000,required=False,widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    
class ProcessCatalogueForm(forms.ModelForm):
    class Meta:
        model=ProcessCatalogue
        exclude=(
            'created_at',
            'updated_at',
            'process_id',
            
        )
        widgets={
            'group_id':forms.SelectMultiple(attrs={'style':"height:10em"}),
            'process_description':forms.Textarea(attrs={'rows': 4, 'cols': 40})
        }
