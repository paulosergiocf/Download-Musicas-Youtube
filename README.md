# Download Musicas Youtube

> Ferramenta para baixar musica do youtube.
### Build

[![Versão do Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-380/) [![Cobertura de Testes](https://img.shields.io/badge/coverage-65%25-brightgreen)](link_para_relatorio_de_cobertura) [![Build](https://github.com/paulosergiocf/Download-Musicas-Youtube/actions/workflows/python-app.yml/badge.svg)](https://github.com/paulosergiocf/Download-Musicas-Youtube/actions/workflows/python-app.yml) 

## Aplicação

Inicio da aplicação.

![Captura de tela de 2024-02-28 00-26-55](https://github.com/paulosergiocf/Download-Musicas-Youtube/assets/49497668/68288d37-3126-4d42-a62f-997d04c1b75b)

Após seleção do arquivo ser realizada.

![Captura de tela de 2024-02-28 00-24-39](https://github.com/paulosergiocf/Download-Musicas-Youtube/assets/49497668/3507d416-22e2-4e73-b673-dff63bf5f72b)

Download em progresso.

![Captura de tela de 2024-02-28 00-25-18](https://github.com/paulosergiocf/Download-Musicas-Youtube/assets/49497668/db2e6efc-dfa1-488f-9f81-28605f6aae0d)


Operações concluídas.

![Captura de tela de 2024-02-28 00-24-58](https://github.com/paulosergiocf/Download-Musicas-Youtube/assets/49497668/c3802b77-cc58-4f32-b19b-ef8fa3850d72)


## Objetivo

O que motivou a criação dessa ferramenta foi a necessidade de adicionar musicas Mp3 a um pendrive para poder ouvir no carro.
Com o avanço das ferramentas de streaming houve uma queda em quantiade e qualidade nas ferramentas de downloads, principalmente para downloads em massa, quando surgiu a demanda, percebi que as ferramentas que utilizava ou estava defasadas e deixaram de funcionar ou passaram a cobrar pelo serviço.

## Critério de aceite:

### Primeira fase

- [x] efetuar upload de lista de videos e fazer download no formato mp3.
- [ ] cobertura de testes acima de 80%.
- [ ] Amplo tratamento de exceções.
- [ ] Interface de usuario simples.

### Melhorias

- [ ] Possibilidade de baixa midia individualmente.
- [ ] extender funcionalidades para videos tambem.

## Montagem de ambiente de desenvolvimento.

Criação de ambiente virtual.

```sh

    python -m venv .venv

```

Ativação de ambiente virtual.
```sh

    source .venv/bin/activate

```
Instalação de dependências.
```sh

    pip install -r requeriments.txt

```

Execução.
```sh

    python main.py

```


## Gerar executavel.

Execute script a partir da pasta do projeto.

```sh

    bash config/build.sh

```
Execute a aplicação clicando no executavel dentro da pasta __dist/audio_downloader_youtube__

