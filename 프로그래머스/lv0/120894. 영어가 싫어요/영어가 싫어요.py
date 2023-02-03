#dictionary의 key, value 활용
def solution(numbers):
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for k, v in num_dict.items():
        numbers = numbers.replace(k, str(v))
    return int(numbers)

#enumerate 활용
def solution(numbers):
    num_dict = {}
    for k, v in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        numbers = numbers.replace(k, str(v))
    return int(numbers)
