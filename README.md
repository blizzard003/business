# business
ros2 package
# multiコマンド
![test](https://github.com/blizzard003/business/actions/workflows/test.yml/badge.svg)
↑テスト結果

このコマンドは、serviceで読み込んだ曜日に応じて、営業日か休業日か判定するものである。

## multiコマンドの使い方
- テスト環境で、ros2 run mypkg talkerと入力する。
- もう一つ端末を開き, ros2 service call query person_msgs/srv/Query "day: 曜日"と入力するとresponceで営業日か休業日か返ってくる。
- 例) 端末1 入力: ros2 run mypkg talker
-　　 端末2 入力: ros2 service call query person_msgs/srv/Query "day: 月"
-           出力: response:
                  person_msgs.srv.Query_Response(business='営業日') 
## 必要なソフトウェア
- python
  - テスト済み

## 対応環境
- Linux
  
### テスト環境
- ubuntu22-04 LTS
- ros2

## ros2をインストールする方法
- 
  
## ros2の通信手順
- 
## ライセンス
- このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布および使用が許可されます。
- このパッケージのコードは、下記のスライド（（CC-BY-SA 4.0 by Ryuichi Ueda)のものを本人の許可を得て自身の著作としたものです。
- [RyuichiUeda/my_sides robosys2022](http://github.com/ryuichiueda/my_slides/tree/masterrobosys_2022)

Ⓒ 2024 Yuki Kasama
