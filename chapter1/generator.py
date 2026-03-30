def gen_range(start, stop):
    while start < stop:
        yield start
        start += 1
res = [i for i in gen_range(0, 10)]
print(res)

def generator_send():
    main_routine_value = 0
    while True:
        main_routine_value = yield
        yield main_routine_value * 2
gen = generator_send()
print(gen)
next(gen)
print(gen.send(100)) # 200
next(gen)
print(gen.send(300)) # 600