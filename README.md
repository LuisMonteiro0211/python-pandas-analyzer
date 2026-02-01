# python-pandas-analyzer

Projeto em evolução para automatizar o processamento de planilhas Excel. Ele aplica filtros e gera arquivos menores com os dados filtrados (ex.: separados por setor e turno).

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

## Configuração do ambiente (.env)

1. Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

2. Edite o `.env` com os caminhos da planilha e da pasta de exportação:

```env
DIRETORIO_PLANILHA=./dados_ficticios_2025.xlsx
DIRETORIO_EXPORT=./exports
```

Notas:
- Você pode usar caminhos absolutos ou relativos.
- Garanta que a pasta de exportação exista antes de executar.

## Como usar

```bash
python main.py
```

O script lê a planilha configurada em `DIRETORIO_PLANILHA`, filtra por **Setor** e **Turno**, e exporta um arquivo Excel por combinação.

## Requisitos da planilha de entrada

A planilha deve conter, no mínimo, as colunas:
- `Setor`
- `Turno`

Outras colunas são preservadas nos arquivos exportados.

## Estrutura do Projeto

```text
python-pandas-analyzer/
├─ main.py
├─ dados_ficticios_2025.xlsx
├─ .env.example
├─ README.md
├─ requirements.txt
└─ src/
   ├─ main/
   │  ├─ __init__.py
   │  └─ start.py
   ├─ helpers/
   │  ├─ __init__.py
   │  └─ helper.py
   ├─ models/
   │  ├─ __init__.py
   │  ├─ filtro.py
   │  └─ export.py
   └─ services/
      ├─ __init__.py
      └─ service.py
```

## Saída gerada

Os arquivos são salvos em `DIRETORIO_EXPORT` com o padrão:

```
Relatorio_{Setor}_{Turno}_{DD_MM_YYYY}.xlsx
```

## Problemas comuns

- `TypeError: argument should be a str or an os.PathLike object...`: variável do `.env` não definida.
- `ValueError: Coluna 'Setor' não encontrada...`: a planilha não possui as colunas obrigatórias.

## Próximos Passos / Evolução

Implementação de funções de exportação adicionais.

Tratamento de erros mais robusto.

Configuração de .env para caminhos mais consistentes.

## Contribuição

Contribuições são bem-vindas! Abra uma issue ou envie um pull request.
