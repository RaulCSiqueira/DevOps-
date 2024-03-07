scores = [0.45, 0.90, 0.92, 1.0, None]
try:
    with open('dataset.txt', 'w') as ds:
        try:
            for score in scores:
                ds.write(f'{score * 100}\n')
        except ValueError as ex:
            print(ex)

except OSError as ex:
    print(ex)