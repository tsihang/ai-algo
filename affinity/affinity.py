import numpy as np
from collections import defaultdict
from operator import itemgetter

valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)

dataset = "dataset.txt"
datas = np.loadtxt(dataset)

goods = ("Bread", "Milk", "Butter", "Apple", "Banana")

valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)

# Initialize associativity from dataset.
# We want to build up an associativity between A and B.
# Thererfore, there implies a Hypothetical Proposition, A -> B, goods A is a premise of this judgement, 
# which will be false only if A=false and B=true.
def associativity(goodsA, goodsB):
    buy_goodsA = 0
    for data in datas:
        if data[goodsA] == 0:
            continue
        buy_goodsA += 1

        if(data[goodsB] == 1):
            # Buy A and buy B
            valid_rules[(goodsA, goodsB)] += 1
        else:
            # Buy A but don't buy B
            invalid_rules[(goodsA, goodsB)] += 1

    return buy_goodsA

def get_confidence():
    confidence = defaultdict(float)
    for premise, feature in valid_rules.keys():
        rule = (premise, feature)
        # The associativity confidence of 2 kinds of goods is a ratio.
        confidence[rule] = valid_rules[rule] / \
            (valid_rules[rule] + invalid_rules[rule])
        
    return confidence

if __name__ == "__main__":
    for i in range(len(goods)):
        for j in range(len(goods)):
            if(i == j):
                continue
            associativity(i,j)

    confidence = get_confidence()

    sort_dict = sorted(confidence.items(), key=itemgetter(1), reverse=True)
    for index in range(5):
        rule = sort_dict[index][0]
        print("The confidence of buying {0} then buying {1} is: {2:0.3f}" .format(goods[rule[0]].ljust(8), goods[rule[1]].ljust(8), confidence[rule]))