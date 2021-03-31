import  re


def main():
    names = ["age","age1","_age_","1age","##$%·age1","a%123"]

    for name in names:
        #ret = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*",name)
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)
        if ret:
            print("变量名:%s 符合要求...通过正则提取出来的是%s"%(name,ret.group()))
        else:
            print("变量名:%s 不符合要求..."%name)

def email():
    email = input("请输入一个邮箱地址:")
    # 如果正则表达式需要用到某些特殊的字符，比如. 需要使用反斜杠 \
    ret = re.match(r"^[a-zA-Z_0-9]{4,20}@(163|126|qq)\.com$",email)
    if ret:
        print("%s符合要求..."%ret.group())

    else:
        print("%s不符合要求..."%ret.group())

def lagou():
    s = r"""<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div class="job-detail">
        <p>1、参与使用Solidity（Ethereum），Truffle框架等进行智能合约的开发。</p><p>2、负责结合游戏业务场景，基于Ethereum技术架构设计与开发包括共识机制、电子资产智能合约标准、数据隐私保护及授权管理、私钥管理、<a class="jd-ad" href="https://kaiwu.lagou.com/course/courseInfo.htm?courseId=2&amp;sid=6-%E6%80%A7%E8%83%BD%E8%B0%83%E4%BC%98-1573655679926" target="_blank" rel="nofollow" data-ad="6" data-lg-tj-id="1kcw" data-lg-tj-no="idnull" data-lg-tj-cid="61573655679926" data-lg-tj-content="性能调优">性能调优</a>；</p><p>3、搭建开发区块链平台和基础框架，作为云服务输出；</p><p>4、参与区块链技术在行业应用中的衔接与落地；</p><p>5、从事区块链产品的设计和研发工作，研究区块链的协议，运行机制和底层实现。</p><p>6、按计划完成项目产品模块的代码编写，产品模块测试，保证代码质量；</p><p>7、编写项目文档，优化服务器逻辑代码；</p><p>8、完成所承担功能模块与其他模块的集成、部署、修改、重构与调优；</p><p>岗位要求：</p><p>1、要求3年及以上工作经验，计算机相关专业本科及以上学历；</p><p>2、研究区块链的协议，运行机制和底层实现；</p><p>3、精通比特币/以太坊/HyperLedger Fabric等区块链相关机制与原理；</p><p>4、熟练各类主流的共识算法，包括不限于PoW，PoS，DPoS，PBFT，Paxos，Raft等；</p><p>5、熟练掌握c++/python/<a class="jd-ad" href="https://kaiwu.lagou.com/course/courseInfo.htm?courseId=1&amp;sid=3-java-1573655679926" target="_blank" rel="nofollow" data-ad="3" data-lg-tj-id="1kcw" data-lg-tj-no="idnull" data-lg-tj-cid="31573655679926" data-lg-tj-content="java">java</a>/GoLang中的两种以上，参与各个区块链开发社区并贡献源码者优先；</p><p>6、熟练使用solidity编写智能合约。</p><p>7、熟悉linux操作系统；</p><p>8、熟悉HTTP/2协议，理解g<a class="jd-ad" href="https://kaiwu.lagou.com/course/courseInfo.htm?courseId=2&amp;sid=6-RPC-1573655679926" target="_blank" rel="nofollow" data-ad="6" data-lg-tj-id="1kcw" data-lg-tj-no="idnull" data-lg-tj-cid="61573655679926" data-lg-tj-content="RPC">RPC</a>框架；</p>
        </div>
    </dd>"""
    print(s)



def egg():
    print(re.match("[.]ello","hello world!"))

    ret = re.match(r"速度激情\d{1,2}","速度激情189")

    print(ret.group())


    print(re.match(r"\d{11}","01234567891 ").group())

    print(re.match(r"\d{3,4}-?\d{7,8}","002187871758").group())

    html_str = "<body><h1>hahahaha</h1></body>"
    ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>",html_str).group()
    ret = re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>", html_str).group()
    print(ret)

if __name__ == '__main__':
    lagou()