#! -*- coding:utf-8 -*-
from config import *
from solutions import *
from timeit import timeit


#problem = None
#logger = None
problem, logger = buildProblem()
annealStart = timeit()
solution1 = anneal(problem, logger)
solution1.solve()
annealEnd = timeit()
annealTime = annealEnd - annealStart

backtrackStart = timeit()
solution2 = backtrack(problem, logger)
solution2.solve()
backtrackEnd = timeit()
backtrackTime = backtrackEnd - annealStart

#solution3 = bound(problem, logger)
#solution3.solve()

dynamicStart = timeit()
solution4 = dynamic(problem, logger)
solution4.solve()
dynamicEnd = timeit()
dynamicTime = dynamicEnd - dynamicStart

#solution5 = ga(problem, logger)
#solution5.solve()

greedyStart = timeit()
solution6 = greedy(problem, logger)
solution6.solve()
greedyEnd = timeit()
greedyTime = greedyEnd - greedyStart


logger.info('模拟退火算法运行时间： %r  秒' %annealTime)
logger.info('回溯算法运行时间： %r  秒' %backtrackTime)
logger.info('动态规划算法运行时间： %r  秒' %dynamicTime)
logger.info('贪心算法算法运行时间： %r  秒' %greedyTime)
