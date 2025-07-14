import streamlit as st

st.title("庄家出牌预测系统（简易版）")

st.markdown("请填写以下数据，系统将自动预测庄家出牌概率：")

col1, col2 = st.columns(2)

with col1:
    z1 = st.number_input("关键对家 - 胜区（输入数字，如1、2）", value=0, step=1)
    z2 = st.number_input("关键对家 - 负区（输入数字，如3、4）", value=0, step=1)
    z3 = st.number_input("关键对家 - 和局（输入数字，如无填0）", value=0, step=1)

with col2:
    g1 = st.number_input("全场关系 - 大胜区", value=0, step=1)
    g2 = st.number_input("全场关系 - 小胜区", value=0, step=1)
    g3 = st.number_input("全场关系 - 和局区", value=0, step=1)
    g4 = st.number_input("全场关系 - 小负区", value=0, step=1)
    g5 = st.number_input("全场关系 - 大负区", value=0, step=1)

if st.button("预测庄家出牌概率"):
    st.success("预测结果如下（仅为示例）：")
    st.write("1号出牌概率：12%")
    st.write("2号出牌概率：20%")
    st.write("3号出牌概率：58%")
    st.write("4号出牌概率：10%")
