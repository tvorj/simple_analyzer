def read_interval():
    with open('config/config.txt', 'r') as f:
        values = {}
        for line in f:
            line = line.strip()

            if "=" in line:
                key, val = line.split("=", 1)
                key, val = key.strip(), val.strip()
                values[key] = val

    return values['interval'], values['sequence_length']


if __name__ == "__main__":
    interval, sequence_length = read_interval()

    print(f'interval : {interval}')
    print(f'sequence_length : {sequence_length}')