import streamlit as st
import pandas as pd
import numpy as np
st.title('潜在性格挖掘')
"本网页是一个性格挖掘器，保护隐私，请您放心！"
"灵魂拷问："
if st.checkbox("准备好了吗？"):
    "我准备好啦！！！"
"       "
if st.button("点我开始"):
    "开始喽！"

name = st.text_input("您的姓名")
howold = st.number_input("您的年龄", value=20, min_value=0, max_value=100, step=1)
birthday1 = st.date_input("您明年的阳历生日")
birthday2 = st.date_input("您明年的阴历生日")
my_radio1 = st.radio("您最喜欢什么水果？",
                   ("苹果🍎","香蕉🍌","橘子🍊","哈密瓜🍈","猕猴桃🥝","芒果🥭"))
# if my_radio1:
#     f"您最喜欢{my_radio1}"
my_radio2 = st.radio("您最喜欢什么花？",
                   ("玫瑰","向日葵","康乃馨","薰衣草","百合","满天星","蔷薇"))
# if my_radio2:
#     f"您最喜欢{my_radio2}"
my_radio3 = st.radio("您最喜欢什么颜色的花？",
                   ("白色","粉色","红色","黄色","绿色","蓝色","紫色"))
# if my_radio3:
#     f"您最喜欢{my_radio3}的花"
Q1 = st.text_input("龟兔赛跑，猪当裁判，谁赢了？")
if Q1=="龟":
    f"哈哈哈哈哈哈哈哈，性格挖掘测试完毕，这都知道，{name}真是裁判猪猪呢🐷呢！"
elif Q1 == "兔":
    f"哈哈哈哈哈哈哈哈，性格挖掘测试完毕，这都知道，{name}真是裁判猪猪呢🐷呢！"
elif Q1 == "不知道":
    f"怎么什么都不知道，{name}不会是个猪猪🐷吧？"
else:
    "答案不合法，请输入正确答案！"
