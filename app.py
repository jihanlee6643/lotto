import random

def start_game():
    # 컴퓨터가 1부터 100 사이의 숫자를 하나 고릅니다.
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("✨ [UP & DOWN 게임]에 오신 것을 환영합니다! ✨")
    print("컴퓨터가 1부터 100 사이의 숫자를 생각했습니다.")
    print("------------------------------------------")

    while True:
        try:
            # 사용자에게 숫자 입력 받기
            guess = int(input("정답은 무엇일까요? 숫자를 입력하세요: "))
            attempts += 1
            
            if guess < secret_number:
                print("☝️ UP! 더 큰 숫자예요.")
            elif guess > secret_number:
                print("👇 DOWN! 더 작은 숫자예요.")
            else:
                print(f"🎉 정답입니다! {attempts}번 만에 맞히셨네요! 대단해요 공주님! 🎉")
                break # 정답을 맞히면 반복문 종료
                
        except ValueError:
            print("❌ 숫자만 입력해 주세요!")

# 게임 시작
start_game()
