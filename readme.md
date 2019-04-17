# Document_Processor

### 使い方

```
# 初期セットアップ
./setup.sh
pip install jinja2

# setup.shを実行することで、config.iniが生成されるので、
# 必要に応じて編集する。
vim config.ini

# 実行
python main.py
```

上記の手順を実行すると、destディレクトリに変数を埋め込んだマークダウンファイルが生成される。