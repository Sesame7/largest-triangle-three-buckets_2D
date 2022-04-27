from lttb.lttb import largest_triangle_three_buckets
import csv


def main():
    with open('source.csv', 'r') as f:
        data = []
        csvf = csv.reader(f, delimiter=',')
        for row in csvf:
            data.append([float(row[0]), float(row[1])])

        sampled = largest_triangle_three_buckets(data, 202)
        with open('sampled.csv', 'w') as f2:
            csvf2 = csv.writer(f2, delimiter=',')
            for row in sampled:
                csvf2.writerow(row)


if __name__ == '__main__':
    main()
    exit()
