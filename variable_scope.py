FOO = 12

answer = 42  # global
# dir = "south"
toast = "hello"

def spam(ham):
    global answer  # BUT PLEASE DON'T DO THIS !!!!!!!
    answer = 1000  # local
    print("In spam(): answer is", answer)  # local->nonlocal->global->builtin
    question = "why?"  # local
#    dir = "north"
    print("dir is", dir)
    print("ham is", ham)
    ham = "goodbye"
    return answer

x = spam(toast)
print("in main: answer is", answer)
print("in main: toast is", toast)
