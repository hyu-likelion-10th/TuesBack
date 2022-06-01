from django import forms
from .models import Survey, Answer

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['question', 'ans1', 'ans2', 'ans3', 'ans4']
        labels = {'question': '질문', 'ans1': '보기1', 'ans2': '보기2', 'ans3': '보기3', 'ans4': '보기4'}
    
    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)

        self.fields['question'].widget.attrs = {
            'class': 'form-control',
            'placeholder': '질문을 입력해주세요',
            'cols': 20
        }

        self.fields['ans1'].widget.attrs = {
            'class': 'form-control',
            'placeholder': '보기를 입력해주세요',
            'cols': 20,
        }

        self.fields['ans2'].widget.attrs = {
            'class': 'form-control',
            'placeholder': '보기를 입력해주세요',
            'cols': 20
        }

        self.fields['ans3'].widget.attrs = {
            'class': 'form-control',
            'placeholder': '보기를 입력해주세요',
            'cols': 20
        }

        self.fields['ans4'].widget.attrs = {
            'class': 'form-control',
            'placeholder': '보기를 입력해주세요',
            'cols': 20
        }
