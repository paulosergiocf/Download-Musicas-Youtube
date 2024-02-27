# Download Musicas Youtube

> Ferramenta para baixar musica do youtube.

[![Python application](https://github.com/paulosergiocf/Download-Musicas-Youtube/actions/workflows/python-app.yml/badge.svg)](https://github.com/paulosergiocf/Download-Musicas-Youtube/actions/workflows/python-app.yml) [![Python application]
(https://github.com/paulosergiocf/Download-Musicas-Youtube/actions/workflows/python-app.yml/badge.svg?event=issues)](https://github.com/paulosergiocf/Download-Musicas-Youtube/actions/workflows/python-app.yml)

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
