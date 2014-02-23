from post.models import Post
from django import forms
from ckeditor.widgets import CKEditorWidget



class PostForm(forms.ModelForm):
        post_content = forms.CharField(widget=CKEditorWidget(config_name="default"))
        class Meta:
            model = Post
