fl = open('data.dat', 'r+')
data = fl.read()
fl.close()
employees = data.splitlines()  # [[01:5000], [02:6000]]
emplist = list(map(lambda x: x.split(':'), employees))
# [['1', '5000'], ['2', '7000']]
def save():
    if len(emplist) > 0:  # Sort based on salary
        emplist.sort(key=lambda els: int(els[1]))

    fle = open('data.dat', 'w')  # Write to file
    res = ''
    for i in emplist: res += i[0]+':'+i[1]+'\n'
    fle.write(res)
    fle.close()

def read():
    id, sal = input('Enter ID'), input('Enter salary')
    for i in emplist:
        if i[0] == id:
            i[1] = sal
            return save()
    emplist.append(list([id, sal]))
    save()
while True: read()
