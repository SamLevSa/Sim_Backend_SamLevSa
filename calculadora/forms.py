from django import forms


class CalculadoraForm(forms.Form):
    numero1 = forms.FloatField(label="Numero 1")
    numero2 = forms.FloatField(label="Numero 2")
    operacao = forms.ChoiceField(
        choices=[
            ("add", "Soma (+)"),
            ("sub", "Subtracao (-)"),
            ("mul", "Multiplicacao (*)"),
            ("div", "Divisao (/)"),
        ],
        label="Operacao",
    )
