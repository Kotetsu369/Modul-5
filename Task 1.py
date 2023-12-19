import time

start_time = time.time()
def get_thread(thread_name):
    time.sleep(1)
    print(f'my name {thread_name}')
    pass

get_thread('one')
get_thread('two')
get_thread('three')
get_thread('four')
get_thread('five')

end_time = time.time()  # время окончания выполнения
execution_time_1 = end_time - start_time  # вычисляем время выполнения

print(f"Время выполнения программы: {execution_time_1} секунд")

import threading


start_time = time.time()
import asyncio

async def get_thread_one():
    await asyncio.sleep(1)
    print(f'my name one')
    pass

async def get_thread_two():
    await asyncio.sleep(1)
    print(f'my name two')
    pass

async def get_thread_three():
    await asyncio.sleep(1)
    print(f'my name three')

async def get_thread_four():
    await asyncio.sleep(1)
    print(f'my name four')
    pass

async def get_thread_five():
    await asyncio.sleep(1)
    print(f'my name five')
    pass

async  def main():
    t1 = asyncio.create_task(get_thread_one())
    t2 = asyncio.create_task(get_thread_two())
    t3 = asyncio.create_task(get_thread_three())
    t4 = asyncio.create_task(get_thread_four())
    t5 = asyncio.create_task(get_thread_five())
    await t1
    await t2
    await t3
    await t4
    await t5

asyncio.run(main())
end_time = time.time()  # время окончания выполнения
execution_time_2 = end_time - start_time  # вычисляем время выполнения

print(f"Время выполнения программы: {execution_time_2} секунд")

print(f'Быстрее задание 2 на {execution_time_1-execution_time_2} сек')


