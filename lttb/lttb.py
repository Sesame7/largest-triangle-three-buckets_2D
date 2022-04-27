import math


def largest_triangle_three_buckets(data, threshold):

    bucket_size = (len(data) - 2) / (threshold - 2)

    a = 0
    next_a = 0
    sampled = [data[0]]

    for i in range(0, threshold - 2):

        avg_x = 0
        avg_y = 0
        avg_range_start = int(math.floor((i + 1) * bucket_size) + 1)
        avg_range_end = int(math.floor((i + 2) * bucket_size) + 1)
        if avg_range_end > len(data):
            avg_range_end = len(data)

        avg_range_length = avg_range_end - avg_range_start

        for m in range(avg_range_start, avg_range_end):
            avg_x += data[m][0]
            avg_y += data[m][1]

        avg_x /= avg_range_length
        avg_y /= avg_range_length

        this_range_start = int(math.floor((i + 0) * bucket_size) + 1)
        this_range_end = int(math.floor((i + 1) * bucket_size) + 1)

        max_area = -1

        for n in range(this_range_start, this_range_end):
            area = 0.5 * math.fabs(
                (data[a][0] - avg_x)
                * (data[n][1] - data[a][1])
                - (data[a][0] - data[n][0])
                * (avg_y - data[a][1]))

            if area > max_area:
                max_area = area
                next_a = n

        a = next_a
        sampled.append(data[a])

    sampled.append(data[-1])

    return sampled
