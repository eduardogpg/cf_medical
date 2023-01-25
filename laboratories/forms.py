from django import forms

class LaboratoryForm(forms.Form):
    name = forms.CharField(max_length=50)
    

    def __init__(self, *args, **kwargs):
        super(LaboratoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        