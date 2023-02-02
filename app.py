# install


import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')       #서버에서, 화면에 표시하기 위해서 필요
import seaborn as sns               ##https://altair-viz.github.io/
from glob import glob
import koreanize_matplotlib
import time
from PIL import Image





# 1


df1 = pd.read_csv("KPU_18_20191231_C_001.csv",encoding="utf-8", header = None, names=['기준년도','시도','시군구','행정동','인구','신고성별남성','신고성별여성','신고성별불상','신고성별기타','접수긴급유형긴급','접수긴급유형중요','접수긴급유형일반','접수긴급유형민원','접수긴급유형기타',
            '발생요일일요일','발생요일월요일','발생요일화요일','발생요일수요일','발생요일목요일','발생요일금요일','발생요일토요일',
            '발생시간대00','발생시간대01','발생시간대02','발생시간대03','발생시간대04','발생시간대05','발생시간대06','발생시간대07','발생시간대08',
            '발생시간대09','발생시간대10','발생시간대11','발생시간대12','발생시간대13','발생시간대14','발생시간대15','발생시간대16','발생시간대17',
            '발생시간대18', '발생시간대19','발생시간대20','발생시간대21','발생시간대22','발생시간대23'])

df2 = pd.read_csv("KPU_18_20201231_C_001.csv",encoding="utf-8",header = None, names=['기준년도','시도','시군구','행정동','인구','신고성별남성','신고성별여성','신고성별불상','신고성별기타','접수긴급유형긴급','접수긴급유형중요','접수긴급유형일반','접수긴급유형민원','접수긴급유형기타',
            '발생요일일요일','발생요일월요일','발생요일화요일','발생요일수요일','발생요일목요일','발생요일금요일','발생요일토요일',
            '발생시간대00','발생시간대01','발생시간대02','발생시간대03','발생시간대04','발생시간대05','발생시간대06','발생시간대07','발생시간대08',
            '발생시간대09','발생시간대10','발생시간대11','발생시간대12','발생시간대13','발생시간대14','발생시간대15','발생시간대16','발생시간대17',
            '발생시간대18', '발생시간대19','발생시간대20','발생시간대21','발생시간대22','발생시간대23'])

df3 = pd.read_csv("KPU_18_20211231_C_001.csv",encoding="utf-8",header = None, names=['기준년도','시도','시군구','행정동','인구','신고성별남성','신고성별여성','신고성별불상','신고성별기타','접수긴급유형긴급','접수긴급유형중요','접수긴급유형일반','접수긴급유형민원','접수긴급유형기타',
            '발생요일일요일','발생요일월요일','발생요일화요일','발생요일수요일','발생요일목요일','발생요일금요일','발생요일토요일',
            '발생시간대00','발생시간대01','발생시간대02','발생시간대03','발생시간대04','발생시간대05','발생시간대06','발생시간대07','발생시간대08',
            '발생시간대09','발생시간대10','발생시간대11','발생시간대12','발생시간대13','발생시간대14','발생시간대15','발생시간대16','발생시간대17',
            '발생시간대18', '발생시간대19','발생시간대20','발생시간대21','발생시간대22','발생시간대23'])


df = pd.concat([df1,df2],axis=0)
df =  pd.concat([df,df3],axis=0)
df = df.drop([df.index[0],df.index[1],df.index[2675]])
df = df.reset_index(drop=True)





# 2 

df_age=pd.read_csv('age.csv', encoding='UTF-8')






# 3
df_time=pd.read_csv('경찰청_보이스피싱 월별 현황_20221031.csv',encoding = 'cp949')
df_2018 = df_time[df_time['년']==2018]
df_2019 = df_time[df_time['년']==2019]
df_2020 = df_time[df_time['년']==2020]
df_2021 = df_time[df_time['년']==2021]
df_2022 = df_time[df_time['년']==2022]






# [theme]
primaryColor="#6adbe6"
backgroundColor="#6adbe6"
secondaryBackgroundColor="#6adbe6"
textColor="#262730"
font="sans serif"

# 컨텐츠 구조 만들기
# from tkinter.tix import COLUMN
from pyparsing import empty

st.set_page_config(layout="wide")
empty1,con1,empty2 = st.columns([0.2,0.3,0.2])
empty1,con2,empty2 = st.columns([0.2,0.3,0.2])
empty1,con3,con4,empty2 = st.columns([0.1,0.5,0.5,0.1])
empty1,con5,con6,empty2 = st.columns([0.1,0.5,0.5,0.1])
empty1,con7,empty2 = st.columns([0.1,1.0,0.1])


def main():
    with empty1:
        empty()
        
    with con1:
        st.title('사이버 범죄 예방을 위한 데이터 시각화')
        st.subheader('동국대X네이버 부스트코스 4팀')
        st.title('\n')
        st.title('\n')
        
        
    with con2:
        image = Image.open('전화금융사기워드클라우드.png')
        st.image(image, width = 800 ,caption='\'전화금융사기\'를 키워드로 크롤링한 네이버 뉴스 기사의 워드클라우드')
        st.title('\n')
        st.title('\n')

        
    with con3:
        st.subheader("지역별로 살펴보는 \n")
        st.subheader("전화금융사기 데이터")

        tab1, tab2, tab3, tab4, tab5, tab6,tab7, tab8 ,tab9= st.tabs(['시도별 전화사기 건수',"경기도", "서울특별시", "경상남도","경상북도","전라북도",'전라남도','충청남도','강원도'])


        with tab1:
            st.header("시도별 전화사기 건수")
            fig = plt.figure(figsize=(10, 4))
            sns.countplot(y="시도", data=df, order = df["시도"].value_counts().index)
            st.pyplot(fig)
            
            
        with tab2:
            st.header("경기도 - 시군구별 전화사기 건수")
            fig = plt.figure(figsize=(10, 10))
            sns.countplot(y="시군구", data=df[df["시도"]=='경기도'],order = df[df["시도"]=='경기도']["시군구"].value_counts().index)
            st.pyplot(fig)


        with tab3:
            st.header("서울특별시 - 시군구별 전화사기 건수")
            fig = plt.figure(figsize=(10, 10))
            sns.countplot(y="시군구", data=df[df["시도"]=='서울특별시'],order = df[df["시도"]=='서울특별시']["시군구"].value_counts().index)
            st.pyplot(fig)

        with tab4:
            st.header("경상남도 - 시군구별 전화사기 건수")
            fig = plt.figure(figsize=(10, 10))
            sns.countplot(y="시군구", data=df[df["시도"]=='경상남도'],order = df[df["시도"]=='경상남도']["시군구"].value_counts().index)
            st.pyplot(fig)

        with tab5:
            st.header("경상북도 - 시군구별 전화사기 건수")
            fig = plt.figure(figsize=(10, 10))
            sns.countplot(y="시군구", data=df[df["시도"]=='경상북도'],order = df[df["시도"]=='경상북도']["시군구"].value_counts().index)
            st.pyplot(fig)
            
        with tab6:
            st.header("전라북도 - 시군구별 전화사기 건수")
            fig = plt.figure(figsize=(10, 10))
            sns.countplot(y="시군구", data=df[df["시도"]=='전라북도'],order = df[df["시도"]=='전라북도']["시군구"].value_counts().index)
            st.pyplot(fig)
            
        with tab7:
            st.header("전라남도 - 시군구별 전화사기 건수")
            fig = plt.figure(figsize=(10, 10))
            sns.countplot(y="시군구", data=df[df["시도"]=='전라남도'],order = df[df["시도"]=='전라남도']["시군구"].value_counts().index)
            st.pyplot(fig)
            
        with tab8:
            st.header("충청남도 - 시군구별 전화사기 건수")
            fig = plt.figure(figsize=(10, 10))
            sns.countplot(y="시군구", data=df[df["시도"]=='충청남도'],order = df[df["시도"]=='충청남도']["시군구"].value_counts().index)
            st.pyplot(fig)
            
        with tab9:
            st.header("강원도 - 시군구별 전화사기 건수")
            fig = plt.figure(figsize=(10, 10))
            sns.countplot(y="시군구", data=df[df["시도"]=='강원도'],order = df[df["시도"]=='강원도']["시군구"].value_counts().index)
            st.pyplot(fig)


    with con4:
        st.header("전화사기 피해 연령대")
        # df_age.plot.bar(x='구분',rot=30)
        st.bar_chart(data=df_age, x="구분")
        
        
    with con5:
        st.header('\'수사기관사칭형\'사례 워드클라우드')
        image = Image.open('다운로드 (7).png')
        st.image(image, width = 800 ,caption='수사기관사칭형')
        st.title('\n')
        st.title('\n')
        df_a = pd.read_csv("수사기관사칭형.csv")
        df_a
        st.title('\n')
        st.title('\n')
        
    with con6:
        st.header('\'대출사기형\' 사례 워드클라우드')
        image = Image.open('다운로드 (9).png')
        st.image(image, width = 800 ,caption='대출사기형')
        st.title('\n')
        st.title('\n')
        df_b = pd.read_csv("대출사기형.csv")
        df_b
        st.title('\n')
        st.title('\n')


    with con7:
        st.header("<2018~2022년 전체 월별 추이>")
        fig = plt.figure(figsize=(10, 4))

        sns.lineplot(data=df_2018, x='월',y='전화금융사기 발생건수', label='2018')
        sns.lineplot(data=df_2019, x='월',y='전화금융사기 발생건수', label='2019')
        sns.lineplot(data=df_2020, x='월',y='전화금융사기 발생건수', label='2020')
        sns.lineplot(data=df_2021, x='월',y='전화금융사기 발생건수', label='2021')
        sns.lineplot(data=df_2022, x='월',y='전화금융사기 발생건수', label='2022')

        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        st.pyplot(fig)
        st.title("\n")
        st.title("\n")
        st.title("\n")
        
        st.title("보이스피싱 실제 음성 사례 들어보기")
        st.title("\n")
        st.title("\n")
        st.audio("보이스피싱실제음성.mp3", format="audio/mp3")
    with empty2:
        empty()
        


if __name__ == "__main__" :
    main()




# col1, col2= st.columns([3,1])

# with col1:
#     st.header("지역별로 살펴보는 전화금융사기 데이터")

#     tab1, tab2, tab3, tab4, tab5, tab6,tab7, tab8 ,tab9= st.tabs(['시도별 전화사기 건수',"경기도", "서울특별시", "경상남도","경상북도","전라북도",'전라남도','충청남도','강원도'])


#     with tab1:
#         st.header("시도별 전화사기 건수")
#         fig = plt.figure(figsize=(10, 4))
#         sns.countplot(y="시도", data=df, order = df["시도"].value_counts().index)
#         st.pyplot(fig)
        
        
#     with tab2:
#         st.header("경기도 - 시군구별 전화사기 건수")
#         fig = plt.figure(figsize=(10, 10))
#         sns.countplot(y="시군구", data=df[df["시도"]=='경기도'],order = df[df["시도"]=='경기도']["시군구"].value_counts().index)
#         st.pyplot(fig)


#     with tab3:
#         st.header("서울특별시 - 시군구별 전화사기 건수")
#         fig = plt.figure(figsize=(10, 10))
#         sns.countplot(y="시군구", data=df[df["시도"]=='서울특별시'],order = df[df["시도"]=='서울특별시']["시군구"].value_counts().index)
#         st.pyplot(fig)

#     with tab4:
#         st.header("경상남도 - 시군구별 전화사기 건수")
#         fig = plt.figure(figsize=(10, 10))
#         sns.countplot(y="시군구", data=df[df["시도"]=='경상남도'],order = df[df["시도"]=='경상남도']["시군구"].value_counts().index)
#         st.pyplot(fig)

#     with tab5:
#         st.header("경상북도 - 시군구별 전화사기 건수")
#         fig = plt.figure(figsize=(10, 10))
#         sns.countplot(y="시군구", data=df[df["시도"]=='경상북도'],order = df[df["시도"]=='경상북도']["시군구"].value_counts().index)
#         st.pyplot(fig)
        
#     with tab6:
#         st.header("전라북도 - 시군구별 전화사기 건수")
#         fig = plt.figure(figsize=(10, 10))
#         sns.countplot(y="시군구", data=df[df["시도"]=='전라북도'],order = df[df["시도"]=='전라북도']["시군구"].value_counts().index)
#         st.pyplot(fig)
        
#     with tab7:
#         st.header("전라남도 - 시군구별 전화사기 건수")
#         fig = plt.figure(figsize=(10, 10))
#         sns.countplot(y="시군구", data=df[df["시도"]=='전라남도'],order = df[df["시도"]=='전라남도']["시군구"].value_counts().index)
#         st.pyplot(fig)
        
#     with tab8:
#         st.header("충청남도 - 시군구별 전화사기 건수")
#         fig = plt.figure(figsize=(10, 10))
#         sns.countplot(y="시군구", data=df[df["시도"]=='충청남도'],order = df[df["시도"]=='충청남도']["시군구"].value_counts().index)
#         st.pyplot(fig)
        
#     with tab9:
#         st.header("강원도 - 시군구별 전화사기 건수")
#         fig = plt.figure(figsize=(10, 10))
#         sns.countplot(y="시군구", data=df[df["시도"]=='강원도'],order = df[df["시도"]=='강원도']["시군구"].value_counts().index)
#         st.pyplot(fig)
        


# with col2:
#     st.header("A dog")

