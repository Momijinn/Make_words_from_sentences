Make_words_from_sentences
====
文章から単語を抜き出すプログラム

単語を抜き出した後、単語をハッシュ化しTwitterにてツイート

## Description
Yahooデベロッパーの日本語形態素解析を利用して文章から単語を抜き出し、それらをハッシュタグ化してTwitterへツイートするシステム

## Demo
```bash
$ python sentence_hash.py "これはてすとです"
['これ', 'てすと']
これはてすとです
#これ #てすと
OK
```
<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">これはてすとです<a href="https://twitter.com/hashtag/%E3%81%93%E3%82%8C?src=hash">#これ</a> <a href="https://twitter.com/hashtag/%E3%81%A6%E3%81%99%E3%81%A8?src=hash">#てすと</a></p>&mdash; みやかわのラズパイ (@momijinn_raspi) <a href="https://twitter.com/momijinn_raspi/status/879990918656344072">2017年6月28日</a></blockquote>

## Requirement
* 動作確認をしたPythonバージョン

    Python 3.5

* TwitterのAPI

* YahooデベロッパーのAPI

## Usage
```bash
$python sentence_hash.py "日本語文章"
```

お店の名前や商品の名前の場合、誤って違うところで切り出されるため、回避策としてこれらの単語のときはシングルクォーテーションで囲うことでうまく抜き出せるようにしました
```bash
$python sentence_hash.py "'おいしいぱんけーき'というお店に行きたい"
おいしいぱんけーきというお店に行きたい
['おいしいぱんけーき', 'お店']
```

## Install
* sentence_hash.pyに引数渡せば出力される

* YahooデベロッパーAPIを取得し,def yaho_nounのにあるappidにAPIを入力
    ```python
    def yaho_noun(sentence):
        url = "https://jlp.yahooapis.jp/MAService/V1/parse?"
        appid = "**********************************************" #your_API
    ```

* TwitterAPIを取得し、def send_twitterにAPIを入力
    ```python
    def send_twitter(words, sentence):
        CK = '*************************'                            # Consumer Key
        CS = '**************************************************'   # Consumer Secret
        AT = '**************************************************'   # Access Token
        AS = '*********************************************'        # Accesss Token Secert
    ```

## Licence
This software is released under the MIT License, see LICENSE.

## Author
[Twitter](https://twitter.com/momijinn_aka)

[Blog](http://www.autumn-color.com/)