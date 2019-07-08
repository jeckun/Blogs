from django import forms


class PostAdminForm(forms.ModelForm):
    # 自定义Form
    # desc 代表文章描述字段
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    title = forms.CharField(label='文章标题', required=False)
