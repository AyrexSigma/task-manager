from django import forms
from .models import Task, Comment

class TaskFilterForm(forms.Form):
    status = forms.ChoiceField(
        choices=[
            ('all', 'All'),
            ('completed', 'Completed'),
            ('incomplete', 'Incomplete'),
        ],
        required=False,
        label='Status',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'attachment']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Напишіть коментар...'
            }),
            'attachment': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']