# wechat_applet

简介：微信小程序-前端搭建与后端联动（以搭建chatgpt问答机器人小程序为例）

# 1.搭建过程

## 1.1 搭建前端

 - 下载[微信开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)
 - 选择目录，打开mp-weixin文件夹(别人的代码拿过来稍微改改)，AppID选择wx8***dd50（不使用云服务）
 - 稍微修改下内容，以及pages/index/index.js中修改下apiurl地址（自己做内网穿透的地址https://b**u.mynat.cc）
 - 完成后点击右上角的上传按钮
 - 登录[开发网页](https://mp.weixin.qq.com/wxamp/wacodepage)，版本管理中先选择体验版，没有问题再提交审核进行发布
 
【注意】<br>
小程序-开发管理-开发设置-服务器域名：配置下https开头的后端域名，这样进入小程序才能有调用后端的展示出来；如果没有https域名，
则可以开启开发调试来进行展示
 
## 1.2 搭建后端

 - 后端用python flask写的比较简单，需要注意的启动flask时需要ip=127.0.0.1, port=80；因为natapp（公网）的隧道域名映射的是本地的80端口
 - 其他就正常python开发，正常调用chatgpt接口（需要apikey）

