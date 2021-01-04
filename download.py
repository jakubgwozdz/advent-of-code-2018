import requests

with open('local/cookie') as f:
    cookie = f.read().strip()

year = 2018
day = 1

while day <= 25:
    r = requests.get('https://adventofcode.com/{0}/day/{1}/input'.format(year, day), headers={'Cookie': cookie}).text
    with open('data/input{0}.txt'.format(day), mode='w') as f:
        f.write(r)

    day = day + 1
