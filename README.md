# markdown-maker-py
This app will read a yaml input file and create a markdown file from it,

## Installation and usage

```
docker build . -t markdown-maker
docker volume create --name markdown_maker_volume --opt type=none --opt device=$PWD --opt o=bind
docker run --mount source=markdown_maker_volume,target=/app markdown-maker:latest day_test.yml
```
