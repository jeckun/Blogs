from django import forms
from .models import Student


# 定义一个新的Form
# class StudentForm(forms.Form):
#     name = forms.CharField(label='姓名', max_length=128)
#     sex = forms.ChoiceField(label='性别', choices=Student.SEX_ITEMS)
#     profession = forms.CharField(label='职业', max_length=128)
#     email = forms.EmailField(label='邮箱', max_length=128)
#     qq = forms.CharField(label='QQ', max_length=128)
#     phone = forms.CharField(label='手机', max_length=128)


# 代码重用
class StudentForm(forms.ModelForm):
    # 添加校验：QQ必须为数字。添加clean_字段名的方法
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            # 错误信息通过forms.ValidationError渲染到页面上
            raise forms.ValidationError('必须是数字！')
        return int(cleaned_data)

    # Meta Data：元数据。
    # 声明Meta类的model为Student,可以重用Form中Student的定义。
    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession', 'email', 'qq', 'phone'
        )
