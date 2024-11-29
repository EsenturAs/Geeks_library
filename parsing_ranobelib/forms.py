from django import forms
from . import models, parser_ranobelib


class ParserForm(forms.Form):
    MEDIA_CHOICES = (("ranobelib", "ranobelib"),)
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            "media_type",
        ]

    def parser_data(self):
        if self.data["media_type"] == "ranobelib":
            ranobelib_pars = parser_ranobelib.parsing()
            for i in ranobelib_pars:
                models.Ranobelib.objects.create(**i)
