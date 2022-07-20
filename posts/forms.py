from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field,Submit
from .models import *
from django import forms
from tinymce.widgets import TinyMCE



class PostCreationForm(forms.ModelForm):
    content = forms.CharField(
        widget = TinyMCE(attrs={"cols": 80, "rows": 15, "class": "form-control"})
    )

    class Meta:
        model = Post
      
        fields = [
            'title',
            'category',
            'content',
            'image',

        ]

class PostUpdateForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(PostUpdateForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method='post'
        self.helper.field_class='mt-10'
        self.helper.layout = Layout(
            Field("title",css_class="single-input",placeholder="Title"),
            Field("category",css_class="single-input"),
            Field("content",css_class="single-input",placeholder="Your Content"),
            Field("image",css_class="single-input"),
            Field("tag",css_class="single-input",placeholder="Your Tags",value=self.instance.post_tag()),

        )
        self.helper.add_input(Submit('submit','Update',css_class="genric-btn success circle"))


    tag = forms.CharField()
    class Meta:
        model = Post
        fields = [
            'title',
            'category',
            'content',
            'image',

        ]

class CreateCommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    def __init__(self,*args,**kwargs):
        super(CreateCommentForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method="post"
        self.helper.layout = Layout(
            Field("name",css_class="form-control"),
            Field("email",css_class="form-control"),
            Field("content",css_class="form-control mb-10"),
            Field("captcha"),
        )

        self.helper.add_input(Submit('submit','Post Comment',css_class="primary-btn submit_btn"))


    class Meta:
        model = Comment
        fields = [
            'name',
            'email',
            'content'
        ]