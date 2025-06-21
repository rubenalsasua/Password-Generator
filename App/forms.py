from django import forms


class PasswordForm(forms.Form):
    longitud_minima = forms.IntegerField(min_value=1, label="Longitud Mínima")
    longitud_maxima = forms.IntegerField(min_value=2, label="Longitud Máxima")
    incluir_mayus_minus = forms.BooleanField(required=False, label="Incluir Mayúsculas y Minúsculas")
    incluir_digitos_especiales = forms.BooleanField(required=False, label="Incluir Dígitos y Caracteres Especiales")

    def clean(self):
        cleaned_data = super().clean()
        longitud_minima = cleaned_data.get("longitud_minima")
        longitud_maxima = cleaned_data.get("longitud_maxima")
        if longitud_minima and longitud_maxima and longitud_minima > longitud_maxima:
            error_msg = "La longitud mínima no puede ser mayor que la longitud máxima."
            self.add_error(None, error_msg)
        return cleaned_data
