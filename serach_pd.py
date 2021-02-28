import os
import csv
import pandas as pd

#csvファイル読み込み
#path = './lesson01.csv'
path = './lesson01_test2.csv'
source = []

csv_data = pd.read_csv(path)
source=list(csv_data["name"])
print(source)

# 検索ソース
#source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    for row in source:
        if word in row:
            print("{}が見つかりました".format(word))
            return 0

    print("リストにはありませんでした")
    source[0].append(word)
    
    #csvファイルに書き込み
    with open(path, 'w') as f:
        writer = csv.writer(f)
        for row in source:
            writer.writerow(row)

    print("{}を追加しました".format(word))

if __name__ == "__main__":

    print(1)
    #search()
