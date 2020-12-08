from .models import Report
from django import forms


# class DisabledFormMixin():
#     def __init__(self):
#         for (_, field) in self.fields.items():
#             field.widget.attrs['disabled'] = True
#             field.widget.attrs['readonly'] = True

class ReportCreateForm(forms.ModelForm):

    class Meta:
        model = Report
        exclude = ['user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'report_url': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'custom-file-input'}),

        }
        fields = '__all__'

        def __init__(self, *args, **kws):
            # To get request.user. Do not use kwargs.pop('user', None) due to potential security hole
            self.user = kws.pop('user')
            super().__init__(*args, **kws)
            self.fields['user'].initial = self.user


# class ReportDeleteForm(ReportCreateForm, DisabledFormMixin):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         DisabledFormMixin.__init__(self)

class FilterForm(forms.Form):
    ORDER_ASC = 'asc'
    ORDER_DESC = 'desc'

    ORDER_CHOICES = (
        (ORDER_ASC, 'Ascending'),
        (ORDER_DESC, 'Descending'),
    )

    text = forms.CharField(
        required=False,
    )
    order = forms.ChoiceField(
        choices=ORDER_CHOICES,
        required=False,
    )
