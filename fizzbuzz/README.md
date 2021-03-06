# 問題文

バージョン番号を示すクラス（や構造体）をつくりたい。 そのクラスから作られたバージョンオブジェクトは major, minor, patch フィールドから構成され、そのオブジェクトは文字列表現も返せる。 semver においてバージョンの各フィールドはゼロ、または正の整数であり、それ以外のものは使えない。 バージョンオブジェクトは等価性比較や大小比較ができる。 （注: プログラミング言語の等価性比較メソッドや大小比較メソッド、文字列表現メソッドなどのイディオムに従うこと）

```
例:
* major が 1, minor が 4, patch が 2 のバージョンの文字列表現は "1.4.2"
* バージョン 1.4.2 は バージョン 2.1.0 と等しくない
* バージョン 10.3.5 は バージョン 10.3.5 と等しい
* バージョン 2.23.1 は バージョン 5.1.2 より小さい
* バージョン 10.3.5 は バージョン 2.23.1 より大きい
```

# TODO

- [x] バージョン番号を示すクラスを作る
    - [x] semver (major, minor, patch) においてバージョンの各フィールドは
        - [x] stringは使えない
        - [x] 正以外のものは使えない。
    - [x] オブジェクトは文字列表現も返せる。
    - [x] バージョンオブジェクトは等価性比較や大小比較ができる。
        - [x] バージョン 1.4.2 は バージョン 2.1.0 と等しくない
        - [x] バージョン 10.3.5 は バージョン 10.3.5 と等しい
        - [x] バージョン 2.23.1 は バージョン 5.1.2 より小さい
        - [x] バージョン 10.3.5 は バージョン 2.23.1 より大きい
        - [x] バージョン 2.23.1 は バージョン 5.1.2 以上
        - [x] バージョン 10.3.5 は バージョン 10.3.5 以下

# Other

## テスト実行

```
$ python -m pytest test_version.py
```

## Cycle

1. 次の目標を考える
2. その目標を示すコードを書く
3. そのテストを実行して失敗させる - Red
4. 目的のコードを書く
5. 2で書いたテストを成功させる - Green
6. テストが通るまでリファクタリングを行う - Refactor
7. 1-6を繰り返す

## Memo

```python
class Version():
    int major
    int minor
    int patch

a = Version()
b = Version()

a > b = True/False

a.toString = 1.3.9
```
