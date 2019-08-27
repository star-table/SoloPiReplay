#solopiReplay
		该项目是为了实现便捷的移动端自动化测试,达到随时录制脚本,上传云端并在多台设备中同时回放
		solopiReplay是基于silopi录制功能产出的json脚本,以python appium库进行解析,通过xpath以及换算坐标定位进行回放.
		(目前坐标换算存在手机兼容性问题,可能存在定位不准确)
##Requirements
####1.python 3.x(64位)
		依赖库:appium,jpype,configparser,logging
####2.jdk(64位)
####3.android sdk



##QUICK START
		准备一台安卓设备(后续将通过stf支持多台设备)
		cmd命令行中输入:adb devices 确保设备已连接
		将solopi录制后的脚本上传至data目录下
		修改config/config.ini,配置所需回放app的包名以及main activity
		执行runCase/start.py(python start.py)

###ACTIONCHAIN/NODE
		通过解析solopi导出的json脚本,将每一步的操作信息收纳在每个Node之中(即Node类)
		再将所有node对象添加进ACTIONINFO类中,达到json一个脚本作为一个ACTIONCHAIN(动作链)
![Image text](https://raw.githubusercontent.com/galaxy-book/SoloPiReplay/master/IMAGE/NODE.PNG)

###OPERATION
		Operation类作为所有事件的重写类,通过解析Node中method属性,使用类反射进行调用
![Image text](https://raw.githubusercontent.com/galaxy-book/SoloPiReplay/master/IMAGE/CLICK.PNG)

###LOG
		您可以在log目录下查看程序运行时的log日志
![Image text](https://raw.githubusercontent.com/galaxy-book/SoloPiReplay/master/IMAGE/log.PNG)

###FOLLOW UP
		1.使用坐标换算定位,不同手机兼容性差,后续将进行优化
		2.部分事件未进行重写,例如循环,断言,判断...
###您可以通过以下方式联系我们
钉钉:

<img src="https://raw.githubusercontent.com/galaxy-book/SoloPiReplay/master/IMAGE/pic.jpg" width=400 height=400>
