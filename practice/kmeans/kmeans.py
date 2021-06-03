import numpy as np
import matplotlib.pyplot as plt


def main():
    classes_num = 5

    raw_data = generatorN(classes_num)  # k,2,num
    raw_data = np.transpose(raw_data, (0, 2, 1)).reshape(-1, 2)  # num*k,2
    starts = get_random_starts(raw_data, classes_num)  # k,2
    means = starts  # 迭代用
    while True:
        groups = group_by_means(raw_data, means)
        draw_data(groups)
        means = cal_new_means(groups)


# 得到随机的初始点
def get_random_starts(_data, k_classes):
    _starts = np.random.randint(0, 499, k_classes)
    _results = {}
    for idx, start in enumerate(_starts):
        _results[idx] = _data[start, :]
    return _results


# 随机生成大致是K个类别的点，用均匀分布生成中心点的位置，用高斯分布生成中心点周围的点
def generatorN(K):
    center = [[np.random.rand(1) * 20, np.random.rand(1) * 20] for _ in range(K)]
    _data = []
    for x, y in center:
        _data.append([np.random.randn(100) + x, np.random.randn(100) + y])

    return _data


# 每个点聚类到最近的中心点
def group_by_means(_data, _means):
    _groups = {(x, y): [] for x, y in _means.values()}
    for x, y in _data:
        min_distance = 10000000
        min_x = None
        min_y = None
        for center_x, center_y in _means.values():
            distance = (x - center_x) ** 2 + (y - center_y) ** 2

            if distance < min_distance:
                min_distance = distance
                min_x, min_y = center_x, center_y
        _groups[(min_x, min_y)].append([x, y])
    return _groups


# 计算每个簇的中心位置----累加每个点坐标，再除以点个数
def cal_new_means(_groups):
    new_means = {i: None for i in range(len(_groups))}
    for idx, key in enumerate(_groups):
        len_value = len(_groups[key])
        sum_x, sum_y = 0, 0
        for x, y in _groups[key]:
            sum_x += x
            sum_y += y
        new_means[idx] = [sum_x / len_value, sum_y / len_value]
    return new_means


# 画图
def draw_data(_groups):
    # fig=plt.figure(dpi=180)
    plt.title("画图")
    for xys in _groups.values():
        xs = [xy[0] for xy in xys]
        ys = [xy[1] for xy in xys]
        plt.scatter(xs, ys)
    plt.show()


if __name__ == '__main__':
    main()
