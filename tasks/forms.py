from django import forms
from tasks.models import Category

class SearchForm(forms.Form):
    search = forms.CharField(
    required = False,
    max_length = 100,

    widget=forms.TextInput(attrs={"placeholder":"Поиск", "class": "form-control"}))

    category = forms.ModelChoiceField(queryset=Category.objects.all(),
       required=False,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    orderings =  (
        ("title", "По названию"),
        ("description", "по описанию"),
        
        ("-title", "По названию (убыв.)"),
        ("-description", "по описанию (убыв.)"),

    )
    ordering = forms.ChoiceField(
        choices=orderings, required=False,
        widget=forms.Select(attrs={"class": "form-control"}))
    
class Post_Form(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    category = forms.ModelChoiceField( queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    def clean(self):
        data = super().clean()
        title = data.get("title")
        description = data.get("description")
        if title.lower() == description.lower():
            raise forms.ValidationError("Title and content must be different")
        return data