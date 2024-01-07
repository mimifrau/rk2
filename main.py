from operator import itemgetter

class Сonductor:

    def __init__(self, id, name, date, cond_id):
        self.id = id
        self.name = name
        self.date = date
        self.cond_id = cond_id


class Orchestra:

    def __init__(self, id, name):
        self.id = id
        self.name = name


class СonductorInOrchestra:

    def __init__(self, orch_id, cond_id):
        self.orch_id = orch_id
        self.cond_id = cond_id

def b1_solution(one_to_many):
    arr =  sorted(one_to_many, key=itemgetter(2))
    ans = []
    for el in arr:
        if el[2][0] == 'A':
            ans.append(el)
    if len(ans) != 0 : return (ans)
    else : return "Оркестров на А нет!"

def b2_solution(one_to_many):
    arr0 = []
    for d in orchestras:
        d_dets = list(filter(lambda i: i[2]==d.name, one_to_many))
        if len(d_dets) > 0:
            d_date = [date for _,date,_ in d_dets]
            d_dates_max = max(d_date)
            arr0.append((d.name, d_dates_max))
    res = sorted(arr0, key=itemgetter(1), reverse=True)
    return res

def b3_solution(many_to_many):
    arr = {}
    for d in orchestras:
        d_emps = list(filter(lambda i: i[2]==d.name, many_to_many))
        d_emps_names = [x for x,_,_ in d_emps]
        arr[d.name] = d_emps_names
    arr = dict(sorted(arr.items()))
    return arr

orchestras = [
    Orchestra(1, 'Atlanta Symphony Orchestra'),
    Orchestra(2, 'National Symphony Orchestra'),
    Orchestra(3, 'New York Philharmonic'),

    Orchestra(11, 'Boston Symphony Orchestra'),
    Orchestra(22, 'Philadelphia Orchestra'),
    Orchestra(33, 'Cleveland Orchestra'),
]


conductors = [
    Сonductor(1, 'Topher Lyndon', 1965, 1),
    Сonductor(2, 'Colton Parry',  1982, 2),
    Сonductor(3, 'Felix Damion',  1973, 3),
    Сonductor(4, 'Cam Raymond',  1988, 3),
    Сonductor(5, 'Armen Mackenzie',  1999, 3),
]

cio = [
    СonductorInOrchestra(1, 1),
    СonductorInOrchestra(2, 2),
    СonductorInOrchestra(3, 3),
    СonductorInOrchestra(3, 4),
    СonductorInOrchestra(3, 5),

    СonductorInOrchestra(11, 1),
    СonductorInOrchestra(22, 2),
    СonductorInOrchestra(33, 3),
    СonductorInOrchestra(33, 4),
    СonductorInOrchestra(33, 5),
]


def main():
    def main():
        one_to_many = [(p.name, p.date, d.name)
                       for d in orchestras
                       for p in conductors
                       if p.cond_id == d.id]

        many_to_many_temp = [(d.name, ed.cond_id, ed.orch_id)
                             for d in orchestras
                             for ed in cio
                             if d.id == ed.cond_id]

        many_to_many = [(e.name, e.date, sup_name)
                        for sup_name, sup_id, det_id in many_to_many_temp
                        for e in conductors
                        if e.id == det_id]

        print('Задание Б1')
        print(b1_solution(one_to_many))

        print('\nЗадание Б2')
        print(b2_solution(one_to_many))

        print('\nЗадание Б3')
        print(b3_solution(many_to_many))


main()
