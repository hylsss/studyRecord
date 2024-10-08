### 自动打卡

---

部署anaconda环境

```
conda create --name autooa python=3.10.14 //autooa  虚拟环境的名字可以改，python版本也可以手动改
conda activate autooa
pip install selenium
pip install webdriver-manager
```

安装**ChromeDriver**

```
https://googlechromelabs.github.io/chrome-for-testing/#stable  //根据你chrome的版本号下载对应的chromedriver
```

没找到你对应的版本号，直接在链接上改成你对应的版本号，再下载（ps:我没找到我谷歌的版本号也是这么干的。。。）

chromedriver存放位置  /usr/local/bin

![chromedriver](https://github.com/hylsss/studyRecord/blob/main/autoCheckIn/images/chromedriver%E5%AD%98%E6%94%BE%E4%BD%8D%E7%BD%AE.pic.jpg)


### 需要修改路径的地方

####  **oaLogin.py**文件中的存放的log的文件夹
![修改log路径](https://github.com/hylsss/studyRecord/blob/main/autoCheckIn/images/%E4%BF%AE%E6%94%B9log%E6%96%87%E4%BB%B6.jpg)

#### **oaLogin.py**中登录的账号密码,修改成自己的
![修改账号密码](https://github.com/hylsss/studyRecord/blob/main/autoCheckIn/images/%E4%BF%AE%E6%94%B9%E7%94%A8%E6%88%B7%E8%B4%A6%E5%8F%B7%E5%AF%86%E7%A0%81.pic.jpg)

#### **oa.sh** 运行python脚本的文件，需要把python的路径修改成你们自己的文件路径
```
source /opt/anaconda3/etc/profile.d/conda.sh   //本地安装anaconda的路径

conda info --envs

conda activate newenv   //最初指定的环境安装路径

python3 /Users/ina.h/Documents/closeWechat/oaLogin.py  //修改成你们文件夹的python路径
```
#### sleep.scpt  这里相当于整个操作的开关
修改,oa.sh脚本的路径，修改成你文件夹对应的
```
set shell_script_path to "/Users/ina.h/Documents/closeWechat/oa.sh"
```

修改log的路径，你可以把log文件删掉，创建自己的log文件
```
set logFile to "/Users/ina.h/Documents/closeWechat/log.log"
```

#### 修改完成后可以直接执行sleep.scpt脚本，验证你的脚本是否生效
![执行](https://github.com/hylsss/studyRecord/blob/main/autoCheckIn/images/%E8%84%9A%E6%9C%AC%E6%89%A7%E8%A1%8C%E9%AA%8C%E8%AF%81.pic.jpg)

### 最后配置一个定时任务
#### 修改com.user.sleepwatcher.plist,修改成你本地文件夹sleep.scpt的地址
```
<string>/Users/koki/checkin/oaCheck.scpt</string>
```
![定时任务修改](https://github.com/hylsss/studyRecord/blob/main/autoCheckIn/images/%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E4%BF%AE%E6%94%B9.jpg)

#####  创建定时任务，并且把com.user.sleepwatcher.plist的内容复制进去

#### ❗️❗️❗️最好是先下载lauchControl软件，然后 Reveal in finder确认一下你的定时任务是放在哪个目录的，不然放错目录定时任务是不生效的❗️❗️❗️直接把com.user.sleepwatcher.plist复制到对应文件夹也不能生效的，会报没权限，所以还是要用命令去创建比较好。

```
nano ~/Library/LaunchAgents/com.user.checkin.plist //
//ctrl + O 保存
//enter 
//ctrl + x 退出
```

#### 加载定时任务

```
加载任务：launchctl load /path/to/your.plist来激活.plist文件定义的任务
卸载任务：launchctl unload /path/to/your.plist来停止任务。
检查任务状态:launchctl list | grep com.example.taskname来检查特定任务的运行状态。
```

**❗️❗️❗️请注意 请注意 请注意❗️❗️❗️**

com.user.sleepwatcher.plist文件中打卡时间是

周一到周五 **早上7点28分打卡，中午11点38分打卡**，签出签入中间间隔**30秒**

具体时间大家可以根据自己的习惯打卡修改。

**需要注意的时候，熄屏情况下是打不了卡的！！！！**

**需要注意的时候，熄屏情况下是打不了卡的！！！！**

**需要注意的时候，熄屏情况下是打不了卡的！！！！**



文件中有一个管理定时任务的工具🔧，**如果你的定时任务添加成功，会在工具里面加载出来com.user.sleepwatcher.plist，管理器可以控制定时任务的开关。**

![管理工具](https://github.com/hylsss/studyRecord/blob/main/autoCheckIn/images/%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E7%AE%A1%E7%90%86.jpg)

---

#### 部署好之后最好还是监测一下是否按时打卡了！！！目前我自己用了一个月，打卡正常，祝大家不被薅羊毛。
