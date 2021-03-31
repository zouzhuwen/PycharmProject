class MusicPlayer(object):
    instance = None
    flag = False

    def __new__(cls, *args, **kwargs):
        #创建对象时new方法会被自动调用
        print("创建对象分配空间... ")

        #为对象分配空间 #返回对象引用
        if  cls.instance is  None:
            cls.instance=super().__new__(cls)
            return  cls.instance
        return cls.instance





    def __init__(self):
        if MusicPlayer.flag is False:
            MusicPlayer.flag = True
            print("播放器初始化...")
        return



# 创建播放器对象
player = MusicPlayer()
player1 = MusicPlayer()
print(player)
print(player1)
object1=object()
print(object1)