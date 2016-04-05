#!usrbinenv python

def reverse(ss):
    result = []
    for s in ss:
        if 'a' <= s <= 'z':
            result.append(s.upper())
        elif 'A' <= s <= 'Z':
            result.append(s.lower())
        else:
            result.append(s)
    return ''.join(result)

print reverse('Mr.Ed')
