#!/usr/bin/env python3.6

import sys
import re

def print_report(results):
    m_result = []
    for result in results.keys():
        try:
            avg_upstream_time = results[result]["upstream_time_sum"] / results[result]["count"]
        except ZeroDivisionError:
            avg_upstream_time = 0

        m_result.append([result, results[result]["upstream_time_sum"],results[result]["count"],avg_upstream_time])

    sorted_x = sorted(m_result, key=lambda i: i[1], reverse=1)

    print("{:>50}\t{:>6}\t{:>5}\t{:>3}".format(
                "Request",
                "Count",
                "Avg",
                "Sum",
    ))
    for sorted_r in sorted_x:
        print("{:>50}\t{:>6}\t{:>5.3f}\t{:>5.3f}".format(
                sorted_r[0],
                sorted_r[2],
                sorted_r[3],
                sorted_r[1],
        ))


def main():

    log_format = '(?P<remote_addr>.+) \- (?P<remote_user>.+) \[(?P<local_time>.+)\] "(?P<method>[A-Z]+) (?P<request>[\w\.\-\/]+).+" ' \
                 '(?P<status>\d{3}) (?P<bytes_sent>\d+) "(?P<http_referer>.+)" ' \
                 '"(?P<uri>.+) (?P<upstream_time>[\d\.-]+)'

    #$remote_addr - $remote_user [$time_local] "$request" $status $bytes_sent "$http_referer" "$http_user_agent" "$gzip_ratio" [$upstream_response_time]
    #40.77.167.71 - - [28/Aug/2018:04:44:39 +0300] "GET /kanal103_20170807.html HTTP/1.1" 200 5747 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" "-" 0.078

    debug=True
    total_count = 0
    results = {}

    for line in sys.stdin:
        m = re.match(log_format, line)
        total_count += 1
        try:
            parsed_line = m.groupdict()

            pl_upstream_time = float(parsed_line['upstream_time'])

            pl_request = parsed_line['method']+" "+parsed_line['request']
            pl_request = re.sub('\d+', '%d', pl_request)

            results[pl_request] = results.get(pl_request, {"upstream_time_sum": 0,"count": 0})
            results[pl_request]["upstream_time_sum"] += pl_upstream_time
            results[pl_request]["count"] += 1


        except AttributeError:
            if debug:
                print('Line {} not parsed: {} '.format(total_count, line))

    print_report(results)

if __name__ == "__main__":
    main()
