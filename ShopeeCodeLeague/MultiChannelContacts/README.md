# Multi Channel Contacts

User 使用產品所留下的資料可能每次都不同，可能第一次使用留 A 電子郵件信箱，第二次使用留 B 電子信箱 (電話號碼、或是訂單編號同理)

希望藉由上述各式各樣的資訊來判斷是不是來自同一個 User

下面資料主要為這次競賽主要的資料，其中希望透過 Email、Phone、OrderId 重新判定是否為同一個 user，下面這個例子主要都是同個 user 的資料

**Example**

| Id | Email | Phone | Contacts | OrderId |
| --- | --- | --- | --- |--- |
| 1 | | 329442681752 | 4 | vDDJJcxfLtSfkooPhbYnJdxov |
| 2458 | ULziZaVD@hotmail.com | 069988936 | 1 | vDDJJcxfLtSfkooPhbYnJdxov |
| 98519 | ULziZaVD@hotmail.com | | 2 | mwVhJZGKtahXEdLMwVLcOAxXG |
| 115061 | JmMSyjzmxdelSmeAHBUi@yahoo.com | 069988936 | 4 | |
| 140081  | xXwrpkygOe@yahoo.com | | 1 | |
| 165605 | xXwrpkygOe@yahoo.com | | 0 | mwVhJZGKtahXEdLMwVLcOAxXG |
| 476346 | WXJDcOYGapCzchhwH@gmail.com | | 0 | vDDJJcxfLtSfkooPhbYnJdxov |

# Reference

- [Shopee Code League - Multi-Channel Contacts](https://www.kaggle.com/c/scl-2021-da/overview)

- [Shopee Code League 2021：數據分析問題解法與 Union-Find 演算法教學](https://haosquare.com/shopee-code-league-2021-data-analytics/)