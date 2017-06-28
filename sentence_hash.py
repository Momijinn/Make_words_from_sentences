# -*- coding: utf-8 -*-
#coding:utf-8

'''
Create by Kaname Takano
文章から単語を抜き出し、ハッシュタグ化しTwitterでツイートするプログラム
お店の名前や商品名はシングルクォーテーションで結ぶと抜き出せるようにしている

ex: "WDが'東芝メモリ'の売却についてわーわー言っている理由がやっとわかった"
    result:['東芝メモリ', 'WD', '売却', '理由']
'''

import sys
import urllib.parse
import urllib.request
import json
from lxml import etree
from requests_oauthlib import OAuth1Session
import re


'''
お店の名前や商品名を抜き出す処理
シングルクォーテーション(')で囲まれている固有名詞を抜き出し配列へ入れている
'''
def free_word(sentence):
    words = []

    '''
    "'"の探索後,\nを入れる処理
    改行をいれないと固有名詞を抜き出せない
    '''
    char_list = list(sentence)
    cnt = 0
    for i in range(0, len(char_list)):
        if char_list[i] == "'":
            if (cnt % 2) != 0:
                char_list[i] = char_list[i] + '\n'
            cnt += 1
    out = ''.join(char_list)
    ##match
    pattern = r"'(.*)'"
    matchs = re.finditer(pattern, out)
    #result
    for match in matchs:
        #print("debug", match.groups()[0])
        words.append(match.groups()[0])

    #最後に連結して返す
    for word in words:
        sentence = sentence.replace("'" + word + "'", " ")

    return words, sentence



'''
Yahooの単語検索サービスに投げて、jsonをもらう処理
https://developer.yahoo.co.jp/
'''
def yaho_noun(sentence):
    url = "https://jlp.yahooapis.jp/MAService/V1/parse?"
    appid = "**********************************************" #your_API

    results = "ma"
    #results = "ma,uniq"

    filter = '9'
    #uniq_filter = '9|13'

    params = urllib.parse.urlencode({
                            'appid':appid,
                            'results':results,
                            #'uniq_filter':uniq_filter,
                            'filter':filter,
                            'sentence':sentence
                        })

    params = params.encode('ascii')
    req = urllib.request.Request(url, params)

    response = urllib.request.urlopen(req)
    return response.read()


'''
yahoo単語サービスからもらってきたデータに対して、欲しいでーた（単語）
'''
def output_word(words, xml):
    tree = etree.fromstring(xml, etree.XMLParser(recover=True))
    tree = tree[0][2] #不要タグの削除 <wordtag>にいる

    for child in tree:
        word = child[0].text
        words.append(word)

    return words



'''
Twitterへタグ付きで送信している処理
本当はインスタグラムにあげたいけど審査があるため諦めている
'''
def send_twitter(words, sentence):
    CK = '*************************'                            # Consumer Key
    CS = '**************************************************'   # Consumer Secret
    AT = '**************************************************'   # Access Token
    AS = '*********************************************'        # Accesss Token Secert

    # ツイート投稿用のURL
    url = "https://api.twitter.com/1.1/statuses/update.json"

    # ツイート本文
    hash_tags = ""
    for word in words:
        hash_tags += '#' + word + ' '

    sentence += '\n' + hash_tags
    print(sentence)
    params = {"status": sentence}

    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.post(url, params = params)

    # レスポンスを確認
    if req.status_code == 200:
        print ("OK")
    else:
        print ("Error: %d" % req.status_code)




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

    send_twitter(words, args[1])