# python-pandas-analyzer

Projeto em evolução para automatizar o processamento de planilhas Excel. Ele aplica filtros e gera arquivos menores com os dados filtrados (ex.: separados por setor e turno).

## Funcionalidades

- Filtragem automática de dados em planilhas Excel.
- Geração de arquivos menores com base em critérios (setor, turno, etc.).
- Estrutura organizada em MVC simples com `helpers`, `models` e `services`.
- Planilha de teste incluída para facilitar o clone e testes rápidos.
- Validação de pré-requisitos (variáveis de ambiente, caminhos e permissões) antes de iniciar o processamento.
- Registro de logs em arquivo.

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

2. Edite o `.env` com os caminhos da planilha, da pasta de exportação e da pasta de logs:

```env
DIRETORIO_PLANILHA=./dados_ficticios_2025.xlsx
DIRETORIO_EXPORT=./exports
DIRETORIO_LOG=./logs
```

Notas:
- Você pode usar caminhos absolutos ou relativos.
- Garanta que as pastas de exportação e de logs existam antes de executar (e que você tenha permissão de escrita).

## Como usar

```bash
python main.py
```

O script lê a planilha configurada em `DIRETORIO_PLANILHA`, filtra por **SETOR** e **TURNO**, e exporta um arquivo Excel por combinação.

## Logs

Os logs são gravados em `DIRETORIO_LOG/app.log`.

## Requisitos da planilha de entrada

A planilha deve conter, no mínimo, as colunas:
- `SETOR`
- `TURNO`

Outras colunas são preservadas nos arquivos exportados.

## Estrutura do Projeto

```text
python-pandas-analyzer/
├─ main.py
├─ pytest.ini
├─ dados_ficticios_2025.xlsx
├─ .env.example
├─ README.md
├─ requirements.txt
├─ src/
│  ├─ main/
│  │  ├─ __init__.py
│  │  └─ start.py
│  ├─ helpers/
│  │  ├─ __init__.py
│  │  ├─ helper.py
│  │  └─ log.py
│  ├─ models/
│  │  ├─ __init__.py
│  │  ├─ filtro.py
│  │  └─ export.py
│  └─ services/
│     ├─ __init__.py
│     └─ service.py
└─ tests/
   ├─ __init__.py
   ├─ test_helper.py
   ├─ test_service.py
   └─ test_start.py
```

## Saída gerada

Os arquivos são salvos em `DIRETORIO_EXPORT` com o padrão:

```
Relatorio_{Setor}_{Turno}_{DD_MM_YYYY}.xlsx
```

## Testes

Execute os testes com:

```bash
pytest
```

## Problemas comuns

- `Variáveis de ambiente não encontradas: ...`: falta configurar alguma variável no `.env`.
- `Caminho informado ... não é um arquivo válido`: `DIRETORIO_PLANILHA` aponta para um caminho inválido.
- `Caminho informado ... não é um diretório válido`: `DIRETORIO_EXPORT`/`DIRETORIO_LOG` apontam para um caminho inválido.
- `Permissão negada para acessar o diretório ...`: pasta existe, mas sem permissão de escrita.
- `Coluna 'SETOR' não encontrada...` / `Coluna 'TURNO' não encontrada...`: a planilha não possui as colunas obrigatórias.

## Próximos Passos / Evolução

- **Tela/Interface (futuro)**: adicionar uma interface para o usuário selecionar a planilha e o diretório de exportação via "gerenciador de arquivos" (file picker).
- **Remover dependência de `.env` (futuro)**: substituir variáveis de ambiente por entradas do usuário na interface (caminhos/arquivos), mantendo as validações de pré-requisitos.

## Contribuição

Contribuições são bem-vindas! Abra uma issue ou envie um pull request.
