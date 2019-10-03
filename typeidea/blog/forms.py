from django import forms
from .models import Comment

"""
表单用来定义需要提交的内容和格式
"""


class CommentForm(forms.ModelForm):
    nickname = forms.CharField(
        label='昵称',
        max_length=50,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': "width: 60%;"}
        )
    )
    email = forms.CharField(
        label='Email',
        max_length=50,
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control', 'style': "width: 60%;"}
        )
    )
    website = forms.CharField(
        label='网站',
        max_length=100,
        widget=forms.widgets.URLInput(
            attrs={'class': 'form-control', 'style': "width: 60%;"}
        )
    )
    content = forms.CharField(
        label='内容',
        max_length=500,
        widget=forms.widgets.Textarea(
            # attrs={'rows': 6, 'cols': 60, 'class': 'form-control'}
            attrs={'class': 'form-control', 'style': "width: 60%;"}
        )
    )

    def clean_content(self):
        # 自定义数据校验
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('内容长度不能少于10个字符！')
        return content

    def as_p(self):
        "Return this form rendered as HTML <p>s."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(label)s  %(field)s%(help_text)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,
        )

    class Meta:
        model = Comment   # 绑定数据
        fields = ['nickname', 'email', 'website', 'content']  # 显示的字段

