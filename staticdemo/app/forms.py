from django import  forms
from django.core import validators
from .models import registermodel
# def start_with_r(value):
#     if value[0]!='r':
#         raise forms.ValidationError('name must be start with r')
def gmail_validation(value):
    if value[len(value)-9:]!='gmail.com':
        raise  forms.ValidationError('must be @gmail')




class staticforms(forms.Form):
    # name=forms.CharField(validators=[start_with_r])
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField(validators=[gmail_validation])
    pwd=forms.CharField(widget=forms.PasswordInput)
    repwd=forms.CharField(label='password(again)',widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(20),validators.MinLengthValidator(12)])
    bot_handler=forms.CharField(widget=forms.HiddenInput,required=False)
### multiple validation atatym

    ## user defined validation/explcitly validation
    # def clean_name(self):
    #     inputname=self.cleaned_data['name']
    #     if len(inputname)<4:
    #         raise forms.ValidationError('name must be 4 letters')
    #
    def clean(self):
        data=super().clean()
        inputpwd=self.cleaned_data['pwd']
        inputrepwd=self.cleaned_data['repwd']
        if inputrepwd!=inputpwd:
            raise  forms.ValidationError('pwd not matched ')
    def clean_bot_handler(self):
        print('bot validation')
        inputbothandler=self.cleaned_data['bot_handler']
        if len(inputbothandler)>0:
            raise forms.ValidationError('thanks bot')


class registerform(forms.ModelForm):
    class Meta:
        model=registermodel
        fields='__all__'

        # def clean_name(self):
        #     inputname=self.cleaned_data['name']
        #     if len(inputname)>10:
        #         raise forms.ValidationError('name should be bellow 10 char')
        # def clean_dept(self):
        #     inputdept = self.cleaned_data['dept']
        #     if len(inputdept) > 10:
        #         raise forms.ValidationError('dept should be bellow 10 char')
        # def clean_sal(self):
        #     inputsal=self.cleaned_data['sal']
        #     if inputsal>=50000:
        #         raise  forms.ValidationError('sal must be above 50000')
        #
class nameform(forms.Form):
    name=forms.CharField(max_length=20)
class ageform(forms.Form):
    age=forms.IntegerField()
class gfnameform(forms.Form):
    gf=forms.CharField(max_length=20)