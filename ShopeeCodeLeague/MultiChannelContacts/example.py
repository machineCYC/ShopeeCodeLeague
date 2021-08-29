import os
import json
import pandas as pd


project_folder = os.path.dirname(__file__)
filepath = os.path.join(project_folder, 'data/contacts.json')

with open(filepath, "r") as f:
    json_data = json.load(f)
data = pd.DataFrame(json_data)
example_data = data[data['Id'].isin([1, 2458, 98519, 115061, 140081, 165605, 476346])]

# Union-Find Structrue
class UF:
  def __init__(self, node_list):
    self.data = {nd: nd for nd in node_list}

  def _find_deepest_node(self, node):
    if self.data[node] != node:
      self.data[node] = self._find_deepest_node(self.data[node])
      return self.data[node]
    else:
      return node

  def connect(self, node_1, node_2):
    if node_1 > node_2: node_1, node_2 = node_2, node_1
    self.data[self._find_deepest_node(node_2)] = self._find_deepest_node(node_1)

  def get_data(self):
    return {k: self._find_deepest_node(v) for k, v in self.data.items()}


node_list = example_data['Id'].unique().tolist()
uf = UF(node_list)

for col in ["OrderId", "Phone", "Email"]:
    val_cnt = example_data[col].value_counts()
    candidate = {x for x in val_cnt[(val_cnt > 1)].index if x != ""}
    for _, grp in data[data[col].isin(candidate)].groupby(col):
        group_ids = set(grp.Id)
        pivot_id = min(group_ids)
        for id_ in group_ids:
            if id_ != pivot_id:
                uf.connect(pivot_id, id_)

    dict_id_newid = uf.get_data()
    example_data['NewId'] = example_data["Id"].map(lambda x:dict_id_newid.get(x))
    print(f"After {col}")
    print(example_data)

'''
            Id                           Email         Phone  Contacts                    OrderId   NewId
1            1                                  329442681752         4  vDDJJcxfLtSfkooPhbYnJdxov  140081
2458      2458            ULziZaVD@hotmail.com     069988936         1  vDDJJcxfLtSfkooPhbYnJdxov  140081
98519    98519            ULziZaVD@hotmail.com                       2  mwVhJZGKtahXEdLMwVLcOAxXG  140081
115061  115061  JmMSyjzmxdelSmeAHBUi@yahoo.com     069988936         4                             140081
140081  140081            xXwrpkygOe@yahoo.com                       1                             140081
165605  165605            xXwrpkygOe@yahoo.com                       0  mwVhJZGKtahXEdLMwVLcOAxXG  140081
476346  476346     WXJDcOYGapCzchhwH@gmail.com                       0  vDDJJcxfLtSfkooPhbYnJdxov  140081

After OrderId
            Id                           Email         Phone  Contacts                    OrderId   NewId
1            1                                  329442681752         4  vDDJJcxfLtSfkooPhbYnJdxov       1
2458      2458            ULziZaVD@hotmail.com     069988936         1  vDDJJcxfLtSfkooPhbYnJdxov       1
98519    98519            ULziZaVD@hotmail.com                       2  mwVhJZGKtahXEdLMwVLcOAxXG   98519
115061  115061  JmMSyjzmxdelSmeAHBUi@yahoo.com     069988936         4                             115061
140081  140081            xXwrpkygOe@yahoo.com                       1                             140081
165605  165605            xXwrpkygOe@yahoo.com                       0  mwVhJZGKtahXEdLMwVLcOAxXG   98519
476346  476346     WXJDcOYGapCzchhwH@gmail.com                       0  vDDJJcxfLtSfkooPhbYnJdxov       1

After Phone
            Id                           Email         Phone  Contacts                    OrderId   NewId
1            1                                  329442681752         4  vDDJJcxfLtSfkooPhbYnJdxov       1 140081
2458      2458            ULziZaVD@hotmail.com     069988936         1  vDDJJcxfLtSfkooPhbYnJdxov       1
98519    98519            ULziZaVD@hotmail.com                       2  mwVhJZGKtahXEdLMwVLcOAxXG   98519  1
115061  115061  JmMSyjzmxdelSmeAHBUi@yahoo.com     069988936         4                                  1
140081  140081            xXwrpkygOe@yahoo.com                       1                             140081
165605  165605            xXwrpkygOe@yahoo.com                       0  mwVhJZGKtahXEdLMwVLcOAxXG   98519  1
476346  476346     WXJDcOYGapCzchhwH@gmail.com                       0  vDDJJcxfLtSfkooPhbYnJdxov       1
'''

print("GG")
