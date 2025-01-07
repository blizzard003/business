# business
ros2 package
# business dayパッケージ
![test](https://github.com/blizzard003/business/actions/workflows/test.yml/badge.svg)
↑テスト結果

このbusiness dayパッケージは、Service通信を用いて、listenerがある処理のリクエストを送信するros2のパッケージである。talkerはそれを受け取り、処理を行った結果をレスポンスとして返す。listenerに曜日を入力にし、talkerが営業日か休業日か答えるものである。

## business dayパッケージの使い方
- linux環境で、ros2 run mypkg talkerと入力する。
- もう一つ端末を開き, ros2 service call query person_msgs/srv/Query "day: 曜日"と入力すると、レスポンスでその曜日が営業日か休業日か返ってくる。
- 例) 端末1 入力: ros2 run mypkg talker

     端末2 入力: ros2 service call query person_msgs/srv/Query "day: 月"

　　　　　 出力: requester: making request: person_msgs.srv.Query_Request(day='月')

　               response:  person_msgs.srv.Query_Response(business='営業日')

## 必要なソフトウェア
- ros2
  
### 開発環境
- ubuntu22-04 LTS
- python3
 - テスト済み
  
## ライセンス
- このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布および使用が許可される。

Ⓒ 2024 Yuki Kasama
