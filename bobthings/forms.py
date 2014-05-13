from django import forms
from models import Comment

from crispy_forms.helper import FormHelper

class TodoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = '/projects/create/'
        self.helper.form_method = 'post'

    class Meta:
        model = Comment