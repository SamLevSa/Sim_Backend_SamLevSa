# Simulado Backend - Calculadora com Django

Projeto simples para aula/simulado.

## Objetivo

- A interface web ja esta pronta com Django.
- Apenas o metodo de adicao foi implementado.
- Os alunos devem finalizar os demais metodos da calculadora.

## Estrutura principal

- `calculadora/calculator.py`: classe com os metodos matematicos.
- `calculadora/views.py`: recebe dados do formulario e chama a calculadora.
- `templates/calculadora/index.html`: pagina web.

## Como executar

1. Criar ambiente virtual (opcional, recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Aplicar migracoes:

```bash
python manage.py migrate
```

4. Subir servidor:

```bash
python manage.py runserver
```

5. Abrir no navegador:

`http://127.0.0.1:8000/`

## Tarefa dos alunos

No arquivo `calculadora/calculator.py`, implementar:

- `subtract`
- `multiply`
- `divide` (incluindo tratamento para divisao por zero)

Depois, criar testes em `calculadora/tests.py` para validar os novos metodos.

## Proximos passos

1. Implementar os metodos `subtract`, `multiply` e `divide` em `calculadora/calculator.py`.
2. No `divide`, retornar erro adequado para divisao por zero.
3. Criar testes unitarios em `calculadora/tests.py` para todos os metodos.
4. Executar os testes com:

```bash
python manage.py test
```

5. Validar manualmente na pagina web se todas as operacoes funcionam no formulario.
6. (Opcional) Melhorar a interface adicionando mensagens mais amigaveis para erros e sucesso.
