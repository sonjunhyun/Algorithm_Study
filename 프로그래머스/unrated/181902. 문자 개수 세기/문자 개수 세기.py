def solution(my_string):
    uppercase = [my_string.count(chr(i)) for i in range(ord("A"), ord("Z")+1)]
    lowercase = [my_string.count(chr(i)) for i in range(ord("a"), ord("z")+1)]
    uppercase.extend(lowercase)
    return uppercase