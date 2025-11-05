from simple_analyzer.analyzer import Analyzer
import random
import time
from datetime import datetime

def read_interval():
    with open('config/config.txt', 'r') as f:
        values = {}
        for line in f:
            line = line.strip()

            if "=" in line:
                key, val = line.split("=", 1)
                key, val = key.strip(), val.strip()
                values[key] = val

    return int(values['interval']), int(values['sequence_length'])


def main():
    interval, sequence_length = read_interval()

    print(f'interval : {interval}')
    print(f'sequence_length : {sequence_length}')

    analyzer = Analyzer()

    while True:
        num = random.randint(1,100)
        analyzer.add_number(num)

        if len(analyzer.numbers) > sequence_length:
            analyzer.numbers.pop(0)

        print(f"total even: {analyzer.even_count()}") 
        print(f'total odd: {analyzer.odd_count()}')
        print(f"highest number: {analyzer.highest_number()}") 
        print(f"increasing pairs: {analyzer.increasing_pairs()}")

        t = datetime.now()

        if len(analyzer.numbers) >= sequence_length and t.second == 0:
            break

        time.sleep(interval)

if __name__ == "__main__":
    main()