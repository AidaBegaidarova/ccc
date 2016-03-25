from django import forms
from qa.models import Question


class AskForm(forms.Form):
    title = forms.CharField(max_length=250)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q