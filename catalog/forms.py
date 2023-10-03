from django import forms

from catalog.models import Product, Version


class MixinForm:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['is_activ', 'is_active', 'is_superuser', 'is_staff']:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(MixinForm, forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'picture', 'category_id', 'price')
        # exclude = ()

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        wrong_worlds = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for item in wrong_worlds:
            if item in cleaned_data.lower():
                raise forms.ValidationError(f'Слово "{item}" недопустипо в названии!')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        wrong_worlds = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for item in wrong_worlds:
            if item in cleaned_data.lower():
                raise forms.ValidationError(f'Слово "{item}" недопустипо в описании!')

        return cleaned_data


class VersionForm(MixinForm, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    # def clean_is_activ(self):
    #     cleaned_data = self.cleaned_data['is_activ']
    #
    #     # print(cleaned_data)
    #     if cleaned_data:
    #         raise forms.ValidationError(f'Слово  недопустипо в описании!')
    #
    #     return cleaned_data
