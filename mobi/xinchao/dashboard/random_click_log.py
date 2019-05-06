# coding:utf-8

import sys
import time
import datetime
import random


def random_sn(count=100000):
    sns = []
    for i in range(1, count):
        sns.append("XC" + str(i).zfill(8))

    return sns


def random_project(count=20):
    projects = []
    for i in range(1, count):
        projects.append("project_" + str(i).zfill(4))

    return projects


def random_apiurl():
    urls = []
    for i in range(1, 6):
        for j in range(1, 6):
            for k in range(1, 4):
                urls.append("/a%d/b%d/c%d" % (i, j, k))

    return urls


def random_use_time(init=100, max=6000):
    use_times = []
    for i in range(init, max):
        use_times.append(i)

    return use_times


def random_now_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


def fill_log_record(now_time, project, sn, url, use_time):
    return ('%s [http-nio-thread-exec-%d] INFO  mobi.xinchao.%s - %d '
            '{"apiUrl":"%s?sn=%s","method":"GET",'
            '"param":"{"sn":"%s"}","responseCode":200,'
            '"sn":{"id":%d,"account":"%s","name":"no_random_name","org_id":"D00786","org_name":"区客","parent_org_id":"D02317","parent_org_name":"新潮传媒集团","user_type":1,"is_deleted":0,"level":2},'
            '"doTime":"%sms","addTime":"%s"}') % (
               now_time, random.randrange(1, 40000), project, use_time, url, sn, sn, int(sn.split('XC')[1]), sn,
               use_time * 2, now_time.split('.')[0])


def random_log_by_time(count, projects, sns, urls, use_times):
    projects_len = len(projects)
    sns_len = len(sns)
    urls_len = len(urls)
    use_times_len = len(use_times)

    records = []

    for i in range(count):
        project = projects[random.randrange(0, projects_len)]
        sn = sns[random.randrange(0, sns_len)]
        url = urls[random.randrange(0, urls_len)]
        use_time = use_times[random.randrange(0, use_times_len)]
        now_time = random_now_time()

        record = fill_log_record(now_time, project, sn, url, use_time)
        records.append(record)

    return records


def generate_log(filename="random_click_log.log", count=100, max_step_time=1):
    """每1000毫秒生成100条记录"""
    projects = random_project()
    sns = random_sn()
    urls = random_apiurl()
    use_times = random_use_time()

    with open(filename, 'w') as f:

        while True:
            records = random_log_by_time(count, projects, sns, urls, use_times)
            for record in records:
                f.write(record)
                f.write('\n')

            time.sleep(max_step_time)

    pass


if __name__ == "__main__":
    argv = sys.argv
    argv_len = len(argv)

    if argv_len >= 4:
        generate_log(filename=argv[1], count=int(argv[2]), max_step_time=int(argv[3]))
    elif argv_len >= 3:
        generate_log(filename=argv[1], count=int(argv[2]))
    elif argv_len >= 2:
        generate_log(filename=argv[1])
    else:
        generate_log()
