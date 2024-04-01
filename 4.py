sp = []
f = open('astronaut_time.csv', encoding='UTF-8').readlines()
f = f[1:]

ans = []

for a in f:
    a = a.strip('\n').split(',')
    sp.append(a)

for i in sp:
    if i[-1] == '9':
        ans.append(i[1])


with open('station_max_downtime.csv', 'w', encoding='UTF-8') as f:
    for j in ans:
        f.write(f'{j}\n')

