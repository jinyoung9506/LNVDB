from django import forms

class UploadFileForm(forms.Form):
    upfile = forms.FileField(
        label='Select a file',
        help_text='Select a image'
    )