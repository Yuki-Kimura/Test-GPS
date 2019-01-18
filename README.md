# Test-GPS
## やること
仮想環境の導入
```
$ python3 -m venv venv
$ source ./venv/bin/activate
```
参考: https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e 

pipパッケージのインストール
```
pip install -r packages.txt
```

## ファイルの説明
- mylib/sample_photo
  - テスト用写真フォルダ
- 　mylib/photo2exif.py
  - 実行することでテスト写真からExif情報を取り出して表示させる
