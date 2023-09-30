from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

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

class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
