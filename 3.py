sp = []
f = open('astronaut_time.csv', encoding='UTF-8').readlines()
f = f[1:]

for a in f:
    a = a.strip('\n').split(',')
    sp.append(a)

nums = [i[1].strip(' ') for i in sp]

n = 0
while n != 'stop':
    n = input()
    if n == 'stop':
        break
    elif n not in nums:
        print('На этой станции все хорошо')
    elif n in nums:
        ind = n.index(n)
        s = sp[ind]
        t = s[3].split(':')
        h_new = int(t[0]) + int(s[-1])
        if h_new > 24:
            h_new = h_new - 24
        time_new = f'{h_new}:{t[1]}:{t[2]}'
        ans = f' На станции {n} восстановлено время (время остановки: {s[3]}). Актуальное время: {time_new}'
        print(ans)