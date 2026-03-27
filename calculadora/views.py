from django.shortcuts import render

from .calculator import Calculator
from .forms import CalculadoraForm


def index(request):
    resultado = None
    erro = None
    form = CalculadoraForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        n1 = form.cleaned_data["numero1"]
        n2 = form.cleaned_data["numero2"]
        operacao = form.cleaned_data["operacao"]

        calc = Calculator()

        try:
            if operacao == "add":
                resultado = calc.add(n1, n2)
            elif operacao == "sub":
                resultado = calc.subtract(n1, n2)
            elif operacao == "mul":
                resultado = calc.multiply(n1, n2)
            elif operacao == "div":
                resultado = calc.divide(n1, n2)
        except NotImplementedError as exc:
            erro = str(exc)
        except ZeroDivisionError:
            erro = "Nao e possivel dividir por zero."

    return render(
        request,
        "calculadora/index.html",
        {
            "form": form,
            "resultado": resultado,
            "erro": erro,
        },
    )
