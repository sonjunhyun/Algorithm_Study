# dictionary를 활용한 풀이
def solution(s):
    dic = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }    # 대응하는 영단어-숫자 dictionary 생성

    for key, value in dic.items():
        s = s.replace(key, value)  # 문자열에 포함되는 key(영단어) 값을 value(숫자)로 replace
            
    return int(s)   # 문자열 데이터를 정수형으로 변환

# list와 enumerate를 활용한 풀이
def solution(s):
    num_word_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']    # 0~9까지의 영단어 list 생성

    for num, word in enumerate(num_word_list):    # 0 'zero', 1 'one', 2 'two' , ...
        s = s.replace(word, str(num))    # 영단어를 숫자로 replace, replace 함수 사용을 위해 str으로 형변환

    return int(s)    # 문자열 데이터를 정수형으로 변환
