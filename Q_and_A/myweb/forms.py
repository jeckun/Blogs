from django import forms
from .models import Questions, Answer


class AnswerForm(forms.ModelForm):

    content = forms.CharField(
        label="回答",
        widget=forms.widgets.Textarea(
            attrs={'class': 'form-control col-md-10'}
        )
    )

    class Meta:
        model = Answer
        fields = (
            'question', 'content', 'owner'
        )


class QuestionsForm(forms.ModelForm):
    title = forms.CharField(
        label="标题",
        max_length=100,
        widget=forms.widgets.Input(
            attrs={'type': "text", 'class': 'form-control col-md-10', 'placeholder': "请输入标题"}
        )
    )

    content = forms.CharField(
        label="内容",
        widget=forms.widgets.Textarea(
            attrs={'rows': 6, 'cols': 30, 'class': 'form-control col-md-10'}
        )
    )

    class Meta:
        model = Questions
        fields = (
            'title', 'content'
        )

