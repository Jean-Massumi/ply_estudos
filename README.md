# Notas - estudos de PLY

## Configuração do ambiente (fazer uma vez)

python -m venv venv

## Ativar o venv (sempre que abrir um terminal novo)

Windows: venv\Scripts\activate
Linux/Mac: source venv/bin/activate

## Instalar o PLY (com o venv ativo)

pip install ply

## Conferir

python -c "import ply; print(ply.**version**)"

## Desativar

deactivate

## Convenções do PLY

- tokens = [...] lista obrigatória
- t_NOME = r'regex' token simples
- def t_NOME(t): r'regex' token com lógica
- t_ignore = ' \t' caracteres ignorados
- t_error(t) tratamento de erro léxico
