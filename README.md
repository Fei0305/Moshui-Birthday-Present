# 送给🐷的20岁生日礼物

## 成品展示
嘿嘿，不给看，最下面有
![IMG_20220311_111837_compressed.jpg](https://s2.loli.net/2022/03/11/WPZJpo9hGYRqU3M.jpg)


## 需要的材料
- ESP8266单片机（NodeMCU）
- 4.2寸微雪三色墨水屏
- 2500mAh锂电池
- 微雪墨水屏驱动板
- 开关
- 锂电池充放电模块
- 积木

## 接线
大概就是这样，画的好丑，其中驱动板和NodeMCU引脚都是匹配的，所以不需要怎么调整，插上就行，需要注意的一点是NodeMCU的RST和D1引脚需短接在一起，从而实现深度睡眠（DeepSleep）的唤醒，后面会讲到。

Tip：还有！焊接的时候一定小心点！
![IMG_20220310_174917_compressed.jpg](https://s2.loli.net/2022/03/10/7cBjKRVzAiayOMS.jpg)
![PXL_20220307_075922489_compressed.jpg](https://s2.loli.net/2022/03/10/qjmxYB7LvzdtfHs.jpg)

## 思路
刚开始我的想法比较简单粗暴，直接NodeMCU开启HTML服务监听，等待上位机指令，这样的好的一点是墨水屏可以随时刷新，只要服务器发送指令就可以更新，我也比较相信ESP8266的功耗水平，但是我用8000mAh锂电池测试过后发现续航极差，8000mAh只能坚持不到3天，这可怎么行，我这墨水屏8000mAh电池3天一充电岂不是被人笑话，查阅资料后发现ESP8266说是低功耗但是开启HTML服务时也确实没那么”低功耗“，所以我改变思路结合图中提到的DeepSleep模式设计了一个功耗低了一点的系统，比较粗糙缺点也比较明显，就是他是30分钟刷新一次，想要自定义刷新只能重启一下，就这样吧，总比成天插着数据线美观 
<center>测试dome</center>  

![PXL_20220212_212835121.jpg](https://s2.loli.net/2022/03/10/AzUXhxf4LTZtdOC.jpg)
 
<center>流程图</center>

![mmexport1646931479547.png](https://s2.loli.net/2022/03/11/EnatmIMORLgz4b6.png)
![mmexport1646931027699.png](https://s2.loli.net/2022/03/11/h5bMvtHnWk8ILog.png)

## 开学！！
要开学了，我的烦恼有俩个，分别是：
- UI要怎么设计
- 金贵的屏幕怎么带过去
- 积木在学校，能赶在3月13号拼好吗

### 1.UI设计
看到这个我是真的头疼，毫无艺术细胞的我要在400x300的屏幕上搞出一个漂亮能拿得出手送给女朋友的界面，主要的限制是这个屏幕只有三种颜色并且没有灰度同时分辨率也低的可怜，最开始的的设计是这样的，自己品品，把自己丑哭😂
![mmexport1646894458203_compressed.png](https://s2.loli.net/2022/03/10/VT9jihZdDrNLtKS.jpg)

后来我的手机刚好升级，看到了MIUI12.5的负一屏，我突然来了灵感
要不然搞个圆角矩形？

![Screenshot_2022-03-03-11-35-41-559_com.miui.home_compressed.jpg](https://s2.loli.net/2022/03/10/RGJOwbtXacv4nDk.jpg)
![PXL_20220301_030957227_compressed.jpg](https://s2.loli.net/2022/03/10/Bx7UQeEwhuWvTMN.jpg)

经过不懈努力（触摸板画图人都麻了）终于画了出来，嘿嘿，一般吧，至少不丑
![矢量图.PNG](https://s2.loli.net/2022/03/11/IvZfi1wWP26rpcD.png)

### 2.金贵的屏幕怎么带到学校
嘿嘿，屏幕厚度不到1mm，我想到拿海绵双面胶把屏幕和纸板粘在一起，然后找到祖传8年的磁带盒，将他塞满卫生纸，将屏幕放进去，外面贴上海绵胶带，再放到柔软的衣服里，再放到行李箱

![PXL_20220307_081013809_compressed.jpg](https://s2.loli.net/2022/03/10/6oUbaIA1mXZuOMf.jpg)
![PXL_20220305_150235734_compressed.jpg](https://s2.loli.net/2022/03/10/eFCiM7SgTBEpHxf.jpg)
嘿嘿，还好没坏！  
![PXL_20220307_082520650_compressed.jpg](https://s2.loli.net/2022/03/10/IXxfSl6b91ncBsF.jpg)


### 3.积木
这部分，我只能说，太爽了，积木主体是在6号和7号集中拼的，但是因为零件在积木里的布局，比如说给电池安个框架，把开关卡在积木中，屏幕的保护等等等等，我只能一遍一遍的拆了拼拼了拆，这个积木也非常小，手都给我按秃噜皮了，本来还想拼个花，但是这么一折腾，弄了半天才弄了个方盒子，至于配色丑，是因为买的5000个积木却有21个颜色，每个颜色都是雨露均沾，最后面的红色不够只能把黑色补上，太惨了。  
3月7日，🐷给我送来了我的生日礼物，是什么呢？是乐高！当我知道是时候，我的心情比较的复杂🤣，还有这事，哈哈哈哈哈，早上中午还在拼命的拼小积木改小积木，心里想，干完这单，再也不碰积木了，下午就收到了乐高🤣  
8号和9号慢慢悠悠的又改了改  
同时很感谢老王，给我提供了工位（它没来😏）才能让我自由的发挥  
![PXL_20220308_072236619_compressed.jpg](https://s2.loli.net/2022/03/10/isJhzgvpOkS1dAq.jpg)
![PXL_20220308_080431356_compressed.jpg](https://s2.loli.net/2022/03/10/JHXlAm2v1Wwke3c.jpg)
![PXL_20220308_074054385_compressed.jpg](https://s2.loli.net/2022/03/10/5lFEJkYhgUP4Zib.jpg)  
最后再加上小天线，方盒子立马就精致了起来！！还挺好看！
![PXL_20220308_084742179_compressed.jpg](https://s2.loli.net/2022/03/10/qKOCuFG7hzBN9lf.jpg)


## 注入灵魂
墨水屏放在这没有灵魂，那不就是花瓶，难道要供着吃电？所以我打算给他注入有趣的灵魂，打算实现的功能：
- 日期星期
- 课程表
- 每日单词
- 天气
- 饭卡余额
- 在一起天数
- 打卡信息
- 自定义显示
- 搭个Hexo博客

这些功能虽然简单但是因为前期需求不明确，所以慢慢悠悠也写了一段时间，代码又丑又长，这是一部分，全部代码在我github

![IMG_20220312_105944_compressed.png](https://s2.loli.net/2022/03/12/QR8lBhrXFqvWJ56.jpg)

成品图：

![PXL_20220312_022119755_compressed.jpg](https://s2.loli.net/2022/03/12/zuZkVi4tCFPAdwb.jpg) ![PXL_20220312_010115218_compressed.jpg](https://s2.loli.net/2022/03/12/hRguLZfBN2yVH76.jpg)

当然，自定义图片也非常方便，我用基于go-cqhttp的qq机器人监听我的图片消息，然后自动处理居中，在下一次刷新时就可以显示了
![PXL_20220308_151629705_compressed.jpg](https://s2.loli.net/2022/03/10/AewWtX59Q3ryED4.jpg)
嘿嘿，真好看！

# 最后
## 🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
## 🎉🎉祝🐖宝生日快乐呀！🎂 🎉🎉
## 🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
