#! -*- coding:utf-8 -*-
from __future__ import division
import random
import logging
from datetime import datetime
import os
from math import ceil
import pickle

def rel_function(weight):
    return ceil(0.9*weight)

class Config(object):
    def __init__(self,
                 # for test
                 #num_range = [5,10],
                 #weight_range =[1,10],
                 #price_range=[1,10],
                 num_range=[500, 1000],
                 weight_range= [1, 100],
                 price_range=[1, 100],
                 volumn_ratio_set=[0.5, 2/3],
                 weight_rel=[False, True],
                 ):
        self.num_range = num_range    # the number range of knapback
        self.price_range=price_range
        self.weight_range= weight_range
        self.weight_rel = weight_rel  # whether the weight and value are related
        self.volumn_ratio_set = volumn_ratio_set # ratio of volumn to total weight

class Problem(object):
    def __init__(self, config, rel_function):
        self.rel_function = rel_function
        self.config = config
        self.weights = []
        self.prices = []

    def generate(self, logger):
        if len(self.weights) + len(self.prices) != 0:
            logger.info('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            logger.info('本次背包问题实验规模为 %d' %self.num)
            logger.info('物品重量列表：\n%r' %self.weights)
            logger.info('物品总重量: %s' %self.weight_sum)
            if self.rel:
                logger.info('其中设置的价值与重量有关')
                logger.info('物品价值列表：\n%r' %self.prices)
                logger.info('物品总价值：%s' %self.price_sum)
            else:
                logger.info('其中设置的价值与重量无关')
                logger.info('物品价值列表：\n%r' %self.prices)
                logger.info('物品总价值：%s' %self.price_sum)
            logger.info('背包的松紧度是%s' %self.volumn_ratio)
            logger.info('背包的总容量是 %s' %self.volumn)
            logger.info('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            return
        logger.info('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        self.rel = random.choice(self.config.weight_rel)
        self.volumn_ratio = random.choice(self.config.volumn_ratio_set)
        self.num = random.randint(*self.config.num_range)

        logger.info('本次背包问题实验规模为 %d' %self.num)
        for i in range(self.num):
            self.weights.append(round(random.uniform(*self.config.weight_range),1))
        self.weight_sum = sum(self.weights)
        logger.info('物品重量列表：\n%r' %self.weights)
        logger.info('物品总重量: %s' %self.weight_sum)
        if self.rel:
            logger.info('其中设置的价值与重量有关')
            self.prices = map(self.rel_function, self.weights)
            self.price_sum = sum(self.prices)
            logger.info('物品价值列表：\n%r' %self.prices)
            logger.info('物品总价值：%s' %self.price_sum)
        else:
            logger.info('其中设置的价值与重量无关')
            for i in range(self.num):
                self.prices.append(round(random.uniform(*self.config.price_range), 1))
            self.price_sum = sum(self.prices)
            logger.info('物品价值列表：\n%r' %self.prices)
            logger.info('物品总价值：%s' %self.price_sum)
        logger.info('背包的松紧度是%s' %self.volumn_ratio)
        self.volumn = round(self.volumn_ratio * self.weight_sum, 1)
        logger.info('背包的总容量是 %s' %self.volumn)
        logger.info('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

def buildProblem():
    timing = datetime.now()
    filename = timing.strftime('%Y%m%d%H%M%S') + '.log'
    filedir = os.path.dirname(os.getcwd()) + '/log/'
    filepath = filedir + filename
    logger = logging.getLogger('KnapbackLogger')
    logger.setLevel(logging.DEBUG)
    fout = logging.FileHandler(filepath)
    pout = logging.StreamHandler()
    logger.addHandler(fout)
    logger.addHandler(pout)
    logger.info('------------Ubuntu 16.04 Python----------')
    logger.info('------------author:leo--------------')

    #rel_function = lambda weight: ceil(0.9 * weight)

    config = Config()
    problem = Problem(config, rel_function)
    if os.path.exists(filedir + 'problem.json'):
        with open(filedir+ 'problem.json', 'r') as fin:
            problem = pickle.load(fin)
        problem.generate(logger)
    else:
        problem.generate(logger)
        with open(filedir+ 'problem.json','w') as fout:
            pickle.dump(problem, fout)
    return problem, logger

