#!-*- coding=utf-8 -*-
import abc
import random
from math import ceil
from math import exp
class solutionBase(object):
    @abc.abstractmethod
    def solve(self):
        return

# solution1: simulated annealing
class anneal(solutionBase):
    def __init__(self, problem, logger, run=30, T = 200, alpha = 0.8):
        self.problem = problem
        self.logger = logger
        self.run = run
        self.T = T
        self.alpha = alpha
        self.logger.info('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        self.logger.info('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        self.logger.info('-------模拟退火算法初始化成功-------')
        self.logger.info('-------初始温度：%d' %self.T)
        self.logger.info('-------退火率:%s' %self.alpha)
        self.logger.info('-------运行次数限制: %s' %self.run)

    def solve(self):
        self.logger.info('-------模拟退火算法开始计算-------')
        # ratio 0.2
        self.logger.info('-------生成初始解中------------')
        opt =[0]*self.problem.num
        cur_weight =0
        for index, weight in enumerate(self.problem.weights):
            tmp_weight = cur_weight+weight
            if tmp_weight > self.problem.volumn:
                break
            opt[index] = 1
            cur_weight = tmp_weight
        cur_price = sum(opt[i]*self.problem.prices[i] for i in range(self.problem.num))
        if cur_weight != sum(opt[i]*self.problem.weights[i] for i in range(self.problem.num)):
            raise ValueError('Initial error')
        self.logger.info('--------初始解生成结束----------')
        self.logger.info('初始解总重量: %s' % cur_weight)
        self.logger.info('初始解总价值: %s' % cur_price)
        iter = 0
        change_num = int(ceil(self.problem.num*0.01))
        T = self.T
        while iter < self.run:
            tmp_opt = opt[:]
            for _ in range(change_num):
                index = random.randint(0, self.problem.num-1)
                tmp_opt[index] = 1- tmp_opt[index] if random.uniform(0,1)<0.9 else tmp_opt[index]# if 0 then 1 elseif 1 then 0
            tmp_weight = sum(tmp_opt[i]*self.problem.weights[i] for i in range(self.problem.num))
            T *= self.alpha
            print ('T:') ,T
            if tmp_weight > self.problem.volumn:
                iter += 1
                self.logger.info('迭代次数：%d' %iter)
                self.logger.info('当前背包内物品总重量: %s' %cur_weight)
                self.logger.info('当前背包内物品总价值: %s' %cur_price)
                continue
            else:
                tmp_price = sum(tmp_opt[i]*self.problem.prices[i] for i in range(self.problem.num))
                delta_price = tmp_price - cur_price
                if delta_price > 0 or random.uniform(0,1) <= exp(delta_price/T):
                    cur_price  = tmp_price
                    opt = tmp_opt
                    cur_weight = tmp_weight
                iter += 1
                self.logger.info('迭代次数：%d' %iter)
                self.logger.info('当前背包内物品总重量: %s' %cur_weight)
                self.logger.info('当前背包内物品总价值: %s' %cur_price)

        self.logger.info('**************************************************************************************************')
        self.logger.info('计算结果最大价值为%d' %cur_price)
        self.logger.info('其中物品总重量为%s' %cur_weight)
        self.logger.info('具体的选择为\n%r' %opt)
        self.logger.info('**************************************************************************************************')
        self.logger.info('-------模拟退火算法结束计算-------')
        self.logger.info('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# solution2: backtrack
class backtrack(solutionBase):
    def __init__(self, problem, logger):
        pass

    def solve(self):
        pass

# solution3: branch and bound method
class bound(solutionBase):
    def __init__(self, problem, logger):
        pass

    def solve(self):
        pass

# solution4: dynamic programming
class dynamic(solutionBase):
    def __init__(self, problem, logger):
        self.problem = problem
        self.logger = logger
        self.logger.info('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        self.logger.info('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        self.logger.info('-------动态规划算法初始化成功-------')
        pass


    def solve(self):
        def getTmp(jump, wv):
            tmp_list = []
            w_tmp, v_tmp = wv
            for point, price in jump:
                w = round(point + w_tmp, 1)
                v = round(price + v_tmp, 1)
                wv_tuple = (w,v)
                tmp_list.append(wv_tuple)
            return tmp_list

        def getJump(jumptmp, jump):
            a = jump[:]
            b = jumptmp[:]
            a.extend(b)
            a.sort()
            maxJump = a[0]
            result = [a[0]]
            for wv_tmp in a:
                if wv_tmp[0]>maxJump[0] and wv_tmp[1] > maxJump[1]:
                    maxJump = wv_tmp
                    result.append(maxJump)
            return result

        def findMax(jump_list, volumn):
            i = len(jump_list)-1
            while jump_list[i][0]>volumn:
                i-=1
            opt_jump = jump_list[i]
            return opt_jump

        def traceback(wv_tmp, jump_tmp, weights, prices):
            trace = [0] * (len(jump_tmp)-1)
            for i in range(1,len(jump_tmp)):
                print 'i:', i
                if wv_tmp in jump_tmp[i]:
                    w_tmp = round(wv_tmp[0] - weights[i-1],1)
                    v_tmp = round(wv_tmp[1] - prices[i-1], 1)
                    wv_tmp = (w_tmp, v_tmp)
                    print i-1
                    trace[i-1] = 1
                else:
                    print wv_tmp, jump_tmp[i]
            return trace

        self.logger.info('-------动态规划算法开始计算-------')
        weights = self.problem.weights
        prices = self.problem.prices
        volumn  = self.problem.volumn
        num = self.problem.num
        jump = [[]]*(num+1)
        jump_tmp = [[]]*(num+1)
        for i in range(num, -1, -1):
            if i==num:
                jump[i] = [(0,0)]
                self.logger.info('跳跃表 p 的第 %d 项是:\n%r' %(i, jump[i]))
                continue
            else:
                wv = (weights[i], prices[i])
                jump_tmp[i+1] = getTmp(jump[i+1], wv)
                if len(jump) - i < 11: # only print front 10
                    self.logger.info("跳跃表中间表 q 的第 %d 项是:\n%r" %(i+1, jump_tmp[i+1]))
                jump[i] = getJump(jump_tmp[i+1], jump[i+1])
                if len(jump) -i < 11:
                    self.logger.info('跳跃表 p 的第 %d 项是:\n%r' %(i, jump[i]))
        opt = findMax(jump[0], volumn)
        total_weight, total_value = opt
        trace = traceback(opt, jump_tmp, weights, prices)

        self.logger.info('**************************************************************************************************')
        self.logger.info('计算结果最大价值为%d' %total_value)
        self.logger.info('其中物品总重量为%s' %total_weight)
        self.logger.info('具体的选择为\n%r' %trace)
        self.logger.info('**************************************************************************************************')
        self.logger.info('-------动态规划算法结束计算-------')
        self.logger.info('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        pass

# solution5: genetic algorithm
class ga(solutionBase):
    def __init__(self, problem, logger):
        pass

    def solve(self):
        pass

# solution6: greedy method
class greedy(solutionBase):
    def __init__(self, problem, logger):
        pass

    def solve(self):
        pass
