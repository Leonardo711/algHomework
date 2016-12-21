#! -*- coding:utf-8 -*-
from config import *
from solutions import *

#problem = None
#logger = None
problem, logger = buildProblem()
solution1 = anneal(problem, logger)
solution1.solve()

solution2 = backtrack(problem, logger)
solution2.solve()

solution3 = bound(problem, logger)
solution3.solve()

solution4 = dynamic(problem, logger)
solution4.solve()

solution5 = ga(problem, logger)
solution5.solve()

solution6 = greedy(problem, logger)
solution6.solve()
