from django import forms
from .models import Task, Comment

class TaskFilterForm(forms.Form):
    status = forms.ChoiceField(
        choices=[
            ('', 'Всі'),  # Порожній вибір для всіх статусів
            ('completed', 'Завершені'),
            ('incomplete', 'Не завершені'),
        ],
        required=False,
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'attachment']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
