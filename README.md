# office_data_generate

>有问题随时微信联系我。

## 更新
重新定义了生成指令的字段，新增了facility accompaniment，删除了destination。在逻辑上，我对物品附带的动作进行了分类，

- 物品字段描述：
  - 关于指令涉及物品的动作：
    - 需要明确指定人：执行该操作的物品与物品所有者有紧密联系（签字，盖章）。此情况下，涉及该动作的人如果没有明确指出，可以进行澄清。
    - 不需要明确指定人：执行该操作的物品与物品所有者无密切联系（拿取操作）。此情况下，因为所有拥有此物品的人都可以完成该动作，所以即使没有明确哪个人，也无需澄清。

效果可以查看test.txt

接下来要把指令变得长一些，也就是生成逻辑上相连的动作。

## 对话生成
这部分正在做，json的格式后续肯定还要继续调整。
