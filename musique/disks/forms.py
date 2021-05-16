from django import forms


class SearchTitleForm(forms.Form):
    title = forms.CharField(label='Research', max_length=200, required=False)

