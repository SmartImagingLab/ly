import numpy as np
import pandas as pd

def getlist(listpth):
    img_size = 500
    # galaxymin不要小于2 会出问题
    # galaxymin = 2
    # galaxymax = 6
    # mag range
    star_range = [7, 18]  # 星等范围
    # galaxy_range = [0, 2]
    starmin, starmax = 1000, 1500  # 星数量范围
    
    # 随机生成恒星数目及星系数目
    star_num = int(np.random.uniform(starmin, starmax))
    # galaxy_num = int(np.random.uniform(galaxymin, galaxymax))

    # alltype = np.vstack((star, galaxy))

    # galaxyx = np.ones((galaxy_num, 1))
    ##########
    # 随机生成星的坐标
    starx = np.random.uniform(0, img_size, (star_num, 1))
    ##########
    # allx = np.vstack((starx, galaxyx))

    # galaxyy = np.ones((galaxy_num, 1))
    ##########
    stary = np.random.uniform(0, img_size, (star_num, 1))
    ##########
    # ally = np.vstack((stary, galaxyy))

    star_num = np.shape(starx)[0]

    # galaxy = np.ones((galaxy_num, 1)).astype(int) * 200
    star = np.ones((star_num, 1)).astype(int) * 100

    # 生成星等均匀分布
    starmag = np.random.uniform(star_range[0], star_range[1], (star_num, 1))
    # galaxymag = np.random.uniform(galaxy_range[0], galaxy_range[1], (galaxy_num, 1))
    # allmag = np.vstack((starmag, galaxymag))

    df = pd.DataFrame(star)
    df['1'] = starx
    df['2'] = stary
    df['3'] = starmag

    df.to_csv(listpth, sep=' ', index=False, header=None, float_format='%.8f')

    # 改变星系的细节参数
    # theta = np.random.uniform(30, 60, galaxy_num)
    # ori = np.array([0.42, 2.3, 0.8, 32.3, 4.0, 0.2, 31.3])
    # new = ori.copy()
    # for i in range(galaxy_num-1):
    #     ori = np.vstack((ori, new))
    # ori[:, 3] = 90 - theta
    # ori[:, 6] = theta

    # galaxydata = np.hstack((galaxy, galaxyx, galaxyy, galaxymag, ori))
    # dfg = pd.DataFrame(galaxydata)
    # dfg.to_csv(listpth, sep=' ', index=False, header=None, mode='a', float_format='%.8f')

if __name__ == '__main__':
    getlist('1.list')