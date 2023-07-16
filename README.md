## 概要

『Linux のしくみ』を MacOS で動かすためのリポジトリ。

Dockerfile で Linux 環境を立ち上げることで、MacOS で Linux コマンドを使用しながら学べる。

## 環境構築

```bash
docker build -t linux-sandbox .

docker run -it --rm -v /path/to/linux-sandbox:/var/app linux-sandbox /bin/bash
```

## 書籍を進める上での Tips

ファイルのパーミッションがデフォルトで 644 になっているため、さまざまなコマンドが実行できない。

以下のコマンドで、このディレクトリ配下のファイルのパーミッションを 744 に変更する。

(umask を使って新規作成ファイルを自動で 744 にしようとしたが、ファイルのデフォルトのパーミッションが 644 なので umask では実行権限をつけることができなかった)

```bash
make chmod
```
