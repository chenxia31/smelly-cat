import os
import streamlit as st
import pandas as pd 

df_data = pd.read_excel("/home/step/data/python-smelly-cat/zoo_module/streamlit/score.xlsx")

# 创建一个文件夹用于保存上传的文件
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# 页面标题和说明文字
st.title("课程作业提交例子")
st.write("请上传csv类型的文件,并输入学号+姓名来命名该文件")

# 选择学号
file_name = st.selectbox("选择学号", df_data["number"].unique())
uploaded_file = st.file_uploader("选择文件", type="xlsx")


# 保存文件
if uploaded_file is not None:
    file_path = os.path.join("uploads", str(file_name)+".xlsx")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    # 更新对应number的score
    df_data.loc[df_data["number"] == file_name, "score"] += 1
    # 更新excel文件
    df_data.to_excel("/home/step/data/python-smelly-cat/zoo_module/streamlit/score.xlsx", index=False)
    st.success(f"已保存文件: {file_path}")

# 显示最新的top 20的分数，可视化柱状图,
st.write("最新的top 20的分数")
data = df_data.sort_values("score", ascending=False).head(20)
# 横轴为number，纵轴为score
st.bar_chart(data["score"])
# 显示表格
st.write(data)
