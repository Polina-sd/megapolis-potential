# №1
sp = []
sp1 = []
f = open('astronaut_time.csv', encoding='UTF-8').readlines()
f = f[1:]

for a in f:
    a = a.strip('\n').split(',')
    sp.append(a)
    sp1.append(a)

for i in sp:
    t = i[3].split(':')
    h_new = int(t[0]) + int(i[-1])
    if h_new > 24:
        h_new = h_new - 24
    t_new = f'{h_new}:{t[1]}:{t[2]}'
    i[3] = t_new

with open('new_time.txt', 'w', encoding='UTF-8') as f:
    for j in sp:
        f.write(f'На станции {j[1]} в каюте {j[2]} восстановлено время. Актуальное время: {t_new}\n')