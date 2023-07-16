## 概要

『Linux のしくみ』を MacOS で動かすためのリポジトリ。

Dockerfile で Linux 環境を立ち上げることで、MacOS で Linux コマンドを使用しながら学べる。

## 使い方

```bash
docker build -t linux-sandbox .

docker run -it --rm -v /path/to/linux-sandbox:/var/app linux-sandbox /bin/bash
```
