from .models import Report
from django import forms


class ReportCreateForm(forms.ModelForm):

    class Meta:
        model = Report
        exclude = ('added_by',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'report_url': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'custom-file-input'}),

        }




class FilterForm(forms.Form):
    ORDER_ASC = 'asc'
    ORDER_DESC = 'desc'

    ORDER_CHOICES = (
        (ORDER_ASC, 'Ascending'),
        (ORDER_DESC, 'Descending'),
    )

    CATEGORY_CHOICES = (
        ('', 'ALL'),
        ('AEX', 'AEX'),
        ('ETC', 'ETC'),
        ('OTHER', 'OTHER')
    )

    title = forms.CharField(
        required=False,
    )

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        required=False,
    )

    order = forms.ChoiceField(
        choices=ORDER_CHOICES,
        required=False,
    )
