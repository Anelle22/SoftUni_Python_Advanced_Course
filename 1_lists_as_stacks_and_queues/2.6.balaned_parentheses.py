text = input()
stack = []
pairs = {')': '(', ']': '[', '}': '{'}

for ch in text:
    if ch in '([{':
        stack.append(ch)
    elif ch in ')]}':
        if not stack or stack[-1] != pairs[ch]:
            print("NO")
            break
        stack.pop()
else:
    print("YES" if not stack else "NO")
