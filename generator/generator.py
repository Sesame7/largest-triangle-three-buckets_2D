import csv
import random


def signal_generator():
    seed = 7
    max_y = 250
    min_y = 100
    max_x = 250
    min_x = 100
    point_num = 3002

    random.seed(seed)
    prev_y = random.random()*(max_y-min_y)+min_y
    prev_x = random.random()*(max_x-min_x)+min_x

    with open('source.csv', 'w') as f:
        csvf = csv.writer(f, delimiter=',')
        for i in range(1, point_num):
            sign_y = random.choice([-1, 1])
            amp_y = random.random()*5
            gen_y = random.random()*amp_y*sign_y+prev_y
            sign_x = random.choice([-1, 1])
            amp_x = random.random()*5
            gen_x = random.random()*amp_x*sign_x+prev_x
            prev_y = gen_y
            prev_x = gen_x
            csvf.writerow([gen_x, gen_y])


if __name__ == '__main__':
    signal_generator()
    exit()
