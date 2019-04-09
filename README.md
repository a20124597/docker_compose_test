# docker_compose_test
在centos虚拟机上安装docker,docker-compose
进入docker_compose_test下
运行sudo docker-compose up
访问http://127.0.0.1:5000/
如果要在虚拟机外即宿主机访问：首先在虚拟机里执行ifconfig查看当前虚拟机的ip地址192.168.159.130
然后在宿主机访问http://192.168.159.130:5000/

常用命令：
如果遇到一些无法解决的错误，可以尝试一下命令重启服务：
systemctl restart network
sudo service docker restart

遇到的坑：
开始无法访问，主要是app.run方法里没有加port=5000，加入后可以正常访问呢，具体原因未知
