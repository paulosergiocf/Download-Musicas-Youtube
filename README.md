# Download Musicas Youtube

> Ferramenta para baixar musica do youtube.
### Build

[![Versão do Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-380/) [![Cobertura de Testes](https://img.shields.io/badge/coverage-65%25-brightgreen)](link_para_relatorio_de_cobertura) [![Build](https://github.com/paulosergiocf/Download-Musicas-Youtube/actions/workflows/python-app.yml/badge.svg)](https://github.com/paulosergiocf/Download-Musicas-Youtube/actions/workflows/python-app.yml) 

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

