# Microsoft-appearance-score [![PyPI version](https://badge.fury.io/py/appearance-score.svg)](https://badge.fury.io/py/appearance-score)

> 微软小冰颜值测试命令行工具

最近发现微小冰有这个颜值测试功能，挺有趣的，就整合了下接口顺手给写了个命令行工具。

### 安装

```bash
$ pip install appearance-score
```

### 使用
```bash
$ mas
usage: mas [-i IMAGES] [-v] [-h]

微软小冰颜值测试命令行工具

optional arguments:
  -i IMAGES, --images IMAGES
                        测试照片
  -v, --version         版本信息
  -h, --help            帮助页面
```

### 示例

**范冰冰**

![范冰冰](https://user-images.githubusercontent.com/19553554/39816061-b220e34e-53cc-11e8-83ae-e380f9fd6b61.jpg)
```
$ mas -i 范冰冰.jpg
范冰冰.jpg : 数据显示，这张脸与中国00后女性审美相符，分数为9.8分。同时法国小姐姐和法国小哥哥也对这相貌给予了高度肯定。  等等！是范冰冰的话，这样的颜值也就不奇怪了。
```

**吴亦凡**

![吴亦凡](https://user-images.githubusercontent.com/19553554/39816063-b2941616-53cc-11e8-86b3-983a15591112.jpeg)
```
$ mas -i 吴亦凡.jpeg
吴亦凡.jpeg : 科学地分析，这张脸最符合中国00后女性的审美，经鉴定打分9.3。甚至法国小姐姐和法国小哥哥也都为这张脸的颜值所 折服。 等等不对！别告诉我你就是吴亦凡……
```

**再测一下我的吧**

![chenjiandongx](https://user-images.githubusercontent.com/19553554/39816062-b2581f4e-53cc-11e8-8865-4dc538b34d8d.jpg)
```
$ mas -i chenjiandongx.jpg
chenjiandongx.jpg : 数据表明，这相貌最符合法国小姐姐的审美，9.5分，远远超过英国90后男性给出的6.1分。 虽然我知道这人是吴 彦祖，但我的评价可是很客观的。
```

嗯，看起来还是蛮 OK 的。


# License

MIT [©chenjiandongx](https://github.com/chenjiandongx)
