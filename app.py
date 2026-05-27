import streamlit as st
import random

st.title("✨ 공주님의 UP & DOWN 게임 ✨")

# 컴퓨터의 비밀 숫자를 웹브라우저 기억장치(session_state)에 저장
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0

st.write("컴퓨터가 1부터 100 사이의 숫자를 생각했습니다. 맞혀보세요!")

# 스트림릿 전용 입력창
guess = st.number_input("숫자를 입력하세요:", min_value=1, max_value=100, step=1)

if st.button("정답 확인하기"):
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        st.warning("☝️ UP! 더 큰 숫자예요.")
    elif guess > st.session_state.secret_number:
        st.warning("👇 DOWN! 더 작은 숫자예요.")
    else:
        st.success(f"🎉 정답입니다! {st.session_state.attempts}번 만에 맞히셨네요!")
        # 게임 리셋 버튼
        if st.button("다시 하기"):
            del st.session_state.secret_number
