import os
import csv

#csvファイル読み込み
#path = './lesson01.csv'
#path = './lesson01_test2.csv'
path = './lesson01_ans.csv'
source = []
if os.path.isfile(path) == True:
    with open(path) as f:
        reader = csv.reader(f)
        source = [row for row in reader]

print(source)

# 検索ソース
#source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く

    #listにある場合、リストに存在する出力をして、終了
    # for row in source:
    #     for sourceWord in row:
    #         if sourceWord == word:
    #             print("{}が見つかりました".format(word))
    #             return 0

    for row in source:
        if word in row:
            print("{}が見つかりました".format(word))
            return 0

    #リストにない場合、リストにないことを出力
    print("リストにはありませんでした")
    
    source[0].append(word)
    source.append([str(int(source[-1][0]) + 1), word])
    
    #csvファイルに書き込み
    with open(path, 'w') as f:
        writer = csv.writer(f)
        for row in source:
            writer.writerow(row)

    print("{}を追加しました".format(word))

if __name__ == "__main__":
    search()
