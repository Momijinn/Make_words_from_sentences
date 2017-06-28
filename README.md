# Make_words_from_sentences
文章から単語を抜き出すプログラム

単語を抜き出した後、単語をハッシュ化しTwitterにてツイートをします

## 動作環境 & 必要なもの
* Python 3.5系

* TwitterのAPI(単語のみの出力であれば不要)

* YahooデベロッパーのAPI

## 使い方
このプログラムを動作させる前にYahooデベロッパーとTwitterデベロッパーからAPIを入手してください！！

下記のようにプログラムを起動すると引数の文章から単語を抜き出してきます
そして、Twitterへツイートします
```bash
$python sentence_hash.py "これはてすとです"
```
```
result
['これ', 'てすと']
これはてすとです
#これ #てすと
OK
```
<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">これはてすとです<a href="https://twitter.com/hashtag/%E3%81%93%E3%82%8C?src=hash">#これ</a> <a href="https://twitter.com/hashtag/%E3%81%A6%E3%81%99%E3%81%A8?src=hash">#てすと</a></p>&mdash; みやかわのラズパイ (@momijinn_raspi) <a href="https://twitter.com/momijinn_raspi/status/879990918656344072">2017年6月28日</a></blockquote>

<br><br>
お店の名前や商品の名前の場合、誤って違うところで切り出されてしまいます

そのため、回避策としてこれらの単語のときはシングルクォーテーションで囲うことでうまく抜き出せるようにしました
```bash
$python sentence_hash.py "'おいしいぱんけーき'というお店に行きたい"
```
```
result
おいしいぱんけーきというお店に行きたい
['おいしいぱんけーき', 'お店']
```

<br><br>
Twitterへツイートしてほしくない場合は、プログラム内のsend_twitter()をコメントアウト化するとツイートしなくなります
```python
if __name__ == '__main__':
    args = sys.argv
    if not(len(args) == 2):
        print("Argument error")
        sys.exit()

    if (args[1].count("'") % 2) != 0:
        print("Single quotation error")
        sys.exit()


    ##あんなことやこんなことをしている
    words, sentence = free_word(args[1])
    json_str = yaho_noun(sentence)
    words = output_word(words, json_str)

    #最後に'を消しにかかる
    args[1] = args[1].replace("'", '')

    #debug
    print(args[1])
    print(words)

    ####ここ#####
    #send_twitter(words, args[1])
```