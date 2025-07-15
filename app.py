import streamlit as st

st.title("庄家出牌预测系统（简易版）")

st.markdown("请填写以下数据，系统将自动预测庄家出牌概率：")

# 出牌输入（用四个数字选择）
st.subheader("出牌（填入1–4中任意一个数字）")
play = st.number_input("庄家出牌数字（1~4）", min_value=1, max_value=4)

# 对家猜测
st.subheader("对家猜测")
dj_win = st.text_input("胜区（如填入 1,2）")
dj_lose = st.text_input("负区（如填入 3,4）")
dj_draw = st.text_input("和局（如填入 0 或空）")

# 全场关系
st.subheader("全场关系")
col1, col2 = st.columns(2)

with col1:
    a = st.text_input("大胜区（如填入 1）")
    b = st.text_input("小胜区（如填入 2）")
    c = st.text_input("和局区（如填入 3）")

with col2:
    d = st.text_input("小负区（如填入 4）")
    e = st.text_input("大负区（如填入 空 或 0）")

# 预测按钮
if st.button("预测庄家出牌概率"):
    st.success("预测结果如下（仅为示例）：")
    st.write("1号出牌概率：12%")
    st.write("2号出牌概率：20%")
    st.write("3号出牌概率：58%")
    st.write("4号出牌概率：10%")
