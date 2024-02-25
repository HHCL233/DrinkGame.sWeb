'''我的主页
下载 （注意版本）streamlit 1.28.2
运行后在输出中复制python -m“streamlit run ···.py”到终端按回车
如果终端无法输入，按Ctrl+C'''
import streamlit as st
from PIL import Image
st.sidebar.image('LOGO.png')
page=st.sidebar.radio("DrinkGame饮料游戏",["关于我们","推荐游戏","轻功能-图片改色","词典","评论留言","《饮料大作战2》","《饮料大作战》"])
def page_1():
    st.write("DrinkGame饮料游戏")
    st.write("一片游戏创作者自由耕耘的天地！")
    st.write("")
    st.write("产品")
    st.write("—")
    st.write("[2024.3.2即将上线]DrinkDO饮料大作战2：有事无事，来场试试！")
    st.write("[2023上线]横纵轴编辑器")
    st.write("[2022上线]KAKA大作战")
    st.write("[2022上线]AllRun一起跑步")
    st.write("[2021上线]饮料大作战")
    st.write("")
    st.write("联动招募与商业合作")
    st.write("—")
    st.write("请QQ联系宣发负责人@未来世界302：938767093")
    st.write("")
    st.write("加入我们 ")
    st.write("—")
    st.write("加入无任何要求")
    st.write("请进入QQ群：767528545")
    st.write("")
    st.write("特别鸣谢")
    st.write("—")
    st.write("CODEMAO编程猫（点猫科技）")
    st.write("")
    st.write("健康游戏忠告")
    st.write("—")
    st.write("抵制不良游戏，拒绝盗版游戏。")
    st.write("注意自我保护，谨防受骗上当。")
    st.write("适度游戏益脑，沉迷游戏伤身。")
    st.write("合理安排时间，享受健康生活。")
    #st.video()
def page_2():
    DrinkDO()
def DrinkDO():
    st.write("《DrinkDO饮料大作战2》")
    st.write("有事无事，来场试试！")
    st.write("")
    st.write("版本更新")
    st.write("—")
    st.write("V0.0.2 2024.2.22")
    st.write("新活动 - 龙虎对对碰修复BUG，增加体验版按钮，统一UI，心愿池优化")
    photoA,photoB,photoC=st.columns([1,1,1])
    with photoA:
        st.image('饮料大作战2图片1.png')
    with photoB:
        st.image("饮料大作战2图片2.png")
    with photoC:
        #st.image("")
        pass
    button1,button2,button3,button4=st.columns([1,1,1,1])
    with button1:
        st.link_button('链接秒开玩', 'https://shequ.codemao.cn/work/212942827')
    with button2:
        st.link_button('下载(密码：bmo1)', 'https://www.lanzouw.com/ixaW71pc6j9i')
    st.write("加入饮料们的QQ群：")
    st.code("560903509")
def YLDZZ():
    st.write("《饮料大作战》")
    st.write("不停服开源！")
    st.link_button('直接访问链接', 'https://shequ.codemao.cn/work/46693614')
def page_3():
    st.write(":sunglasses:轻功能-图片改色:sunglasses:")
    uploaded_file=st.file_uploader("上传图片",type=["png","jpeg","jpg"])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4=st.tabs(["原图","处理效果1","效果2","效果3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
def page_4():
    '''我的智慧词典'''
    st.write("智慧词典")
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list=f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split("#")
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open("check_out_times.txt",'r',encoding='utf-8') as f:
        times_list=f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split("#")
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    #输入框
    word=st.text_input("查询单词")
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open("check_out_times.txt",'w',encoding="utf-8") as f:
            message=""
            for k,v in times_dict.items():
                message+=str(k)+"#"+str(v)+"\n"
            message=message[:-1]
            f.write(message)
                
        st.write("查询次数：",times_dict[n])
def page_5():
    "评论留言"
    st.write("评论留言")
    st.code("！请文明发言！！请文明发言！！请文明发言！！请文明发言！！请文明发言！！请文明发言！！请文明发言！")
    with open("leave_messages.txt",'r',encoding="utf-8") as f:
        messages_list=f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split("#")
    for i in messages_list:
        if i[1]=="阿短":
            with st.chat_message("🍸"):#将这个表情包当作这个人的头像显示
                #表情包前往https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/   查看
                st.write(i[1],"  :")#消息
                st.code(i[2])
        elif i[1]=="编程猫":
            with st.chat_message("🍹"):
                st.write(i[1],"  :")#消息
                st.code(i[2])
        elif i[1]=="饮料":
            with st.chat_message("🍺"):
                st.write(i[1],"  :")#消息
                st.code(i[2])
        elif i[1]=="饮料游戏官方":
            with st.chat_message("✅"):
                st.write(i[1])#消息
                st.caption("饮料官方认证")
                st.code(i[2])
    name=st.selectbox("用户名",["阿短","编程猫","饮料","饮料游戏官方"])#下拉框
    new_message=st.text_input("说些什么...")#输入框
    if st.button("发送"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open("leave_messages.txt",'w',encoding='utf-8') as f:
            message=""
            for i in messages_list:
                message+=i[0]+'#'+i[1]+"#"+i[2]+'\n'
            message=message[:-1]
            f.write(message)
def img_change(img,rc,gc,bc):
    '''为page_3提供图片处理'''
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img
if page=="关于我们":
    '''关于我们'''
    page_1()
elif page=="推荐游戏":
    '''推荐游戏'''
    page_2()
elif page=="轻功能-图片改色":
    '''轻功能-图片改色'''
    page_3()
elif page=="词典":
    '''词典'''
    page_4()
elif page=="评论留言":
    '''评论留言'''
    page_5()
elif page=="《饮料大作战2》":
    DrinkDO()
elif page=="《饮料大作战》":
    YLDZZ()