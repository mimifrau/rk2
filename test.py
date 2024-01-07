import unittest
from main import *


class Test_Program(unittest.TestCase):
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
        Сonductor(2, 'Colton Parry', 1982, 2),
        Сonductor(3, 'Felix Damion', 1973, 3),
        Сonductor(4, 'Cam Raymond', 1988, 3),
        Сonductor(5, 'Armen Mackenzie', 1999, 3),
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

    def test_b1(self):
        one_to_many = [(p.name, p.date, d.name)
                       for d in orchestras
                       for p in conductors
                       if p.cond_id == d.id]

        self.assertEqual(b1_solution(one_to_many),
                         [('Topher Lyndon', 1965, 'Atlanta Symphony Orchestra')])

    def test_b2(self):
        one_to_many = [(p.name, p.date, d.name)
                       for d in orchestras
                       for p in conductors
                       if p.cond_id == d.id]

        self.assertEqual(b2_solution(one_to_many),
                         [('New York Philharmonic', 1999),
                          ('National Symphony Orchestra', 1982),
                          ('Atlanta Symphony Orchestra', 1965)])

    def test_b3(self):
        many_to_many_temp = [(d.name, ed.orch_id, ed.cond_id)
                             for d in orchestras
                             for ed in cio
                             if d.id == ed.cond_id]

        many_to_many = [(e.name, e.date, orch_name)
                        for orch_name, orch_id, cond_id in many_to_many_temp
                        for e in conductors
                        if e.id == cond_id]

        self.assertEqual(b3_solution(many_to_many),
                         {'Atlanta Symphony Orchestra': ['Topher Lyndon', 'Topher Lyndon'],
                          'Boston Symphony Orchestra': [],
                          'Cleveland Orchestra': [],
                          'National Symphony Orchestra': ['Colton Parry', 'Colton Parry'],
                          'New York Philharmonic': ['Felix Damion', 'Felix Damion'],
                          'Philadelphia Orchestra': []})


if __name__ == '__main__':
    unittest.main()
