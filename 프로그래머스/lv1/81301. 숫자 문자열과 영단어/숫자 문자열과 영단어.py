def solution(s):
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}    # 대응하는 영단어-숫자 딕셔너리 생성

    for key, value in dic.items():
        s = s.replace(key, value)  # 문자열에 포함되는 key(영단어) 값을 value(숫자)로 replace
            
    return int(s)   # 문자열 데이터를 정수형으로 변환