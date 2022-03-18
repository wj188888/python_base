# locust
1. Taskset区别:
- TaskSequece: 这个是按用例的排序进行执行的
- Taskset: 不是按用户执行顺序的;
- @seq_task(1) 装饰器,定义执行顺序的任务,从小到大,任务就可以是一个接口请求
- client(catch_response=True) 允许为失败,name 设置任务标签名称 ---可选参数
- --web-host 指定web访问域名,ip
- --port Port 指定web的访问端口,port
- -f LOCUSTFILE.py ,如果你是locustfile.py那么可以不用写-f
- --no-web : 无图形模式.-c,-t
- -c: 设置运行的用户数
- -r: 指定每秒生产用户数
- -t: --run-time: 无图形模式,设置总运行时长(30s丶2m分钟丶1h丶1h30m)
2. 分布式模式参数
- --master 设置为主线程
- --master-bind-host 主进程,绑定ip地址,只用于 --master
- --master-bind-port 主进程,绑定端口,默认端口为5557,只用于主进程--master
- --slave 设置为助进程
- --master-host 助进程链接的主进程ip地址,只能用于--slave
- --master-port 助进程链接的主进程port,默认端口为5557,只能用于 --slave

3. 其他的参数
- --step-load: 步长加载模式,比如做负载测试,需要有--step-clients丶--step-time参数
- --steep-clients: 步长加载模式中,总共加载的用户数,仅用于--step-load一起使用
- --step-time : 加载用的时间,仅用于--step-load一起用
- --csv CSVFILEBASE, --csv-base-name, 将运行结果写入的哦啊指定前缀的csv文件中,默认为2s写一次,可自行设置
- --csv-full-history: 将每个统计信息都写入_stats_history.csv文件中
- --loglevel; -l: 设置日志级别
- --logfile: 日志输出文件,没有设置,日志将转到stdout丶stderr
- --print-stas: 控制台输出
- --only-summary: 仅输出概要报告

# 运行locust脚本
1. 可以main中运行
2. 可以在命令行运行
- locust -f locustfile.py --host=serverhost/ip

3. 加上 --step-load
- 步长,时间,多了step duration的内容
4. 图形界面运行模式
- 指定web地址命令: locust -f 被执行的文件.py --web-host 127.0.0.1 -P 8389
- 然后通过http://127.0.0.1:8389 来进行访问的