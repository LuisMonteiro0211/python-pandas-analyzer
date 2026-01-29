# python-pandas-analyzer

Projeto em evolução para automatizar o processamento de planilhas Excel. Ele aplica uma sequência de filtros e gera arquivos menores com os dados filtrados (ex.: arquivos separados por setor e turno).

## Funcionalidades

- Filtragem automática de dados em planilhas Excel.
- Geração de arquivos menores com base em critérios (setor, turno, etc.).
- Estrutura organizada em MVC simples com `helpers`, `models` e `services`.
- Planilha de teste incluída para facilitar o clone e testes rápidos.

## Pré-requisitos

- Python 3.x
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone o repositório:

```bash
git clone <https://github.com/LuisMonteiro0211/python-pandas-analyzer>
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Rodar o Projeto

```bash
python main.py
```

Os demais módulos (helpers, models, services) são utilizados pelo main.py.

Comentários nos scripts explicam o funcionamento dos filtros aplicados.

## Estrutura do Projeto

```text
python-pandas-analyzer/
├─ main.py
├─ dados_ficticios_2025.xlsx
├─ src/
│  ├─ helpers/
│  │  ├─ __init__.py
│  │  └─ helper.py
│  ├─ models/
│  │  ├─ __init__.py
│  │  └─ filtro.py
│  └─ services/
│     ├─ __init__.py
│     └─ service.py
├─ README.md
└─ requirements.txt
```

## Próximos Passos / Evolução

Implementação de funções de exportação adicionais.

Tratamento de erros mais robusto.

Configuração de .env para caminhos mais consistentes.

## Contribuição

Contribuições são bem-vindas! Abra uma issue ou envie um pull request.
