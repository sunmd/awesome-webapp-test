#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

import asyncio
import threading
import time
import playsound


# 携程函数
async def hello():
	print("Running in the loop ... ")
	flag = 0
	while flag < 1000:
		with open("test.txt", "a") as f:
			f.write("-----")
		flag += 1
	print("Stop in the loop")
	return "ok"

if __name__ == '__main__':
	coroutine = hello()
	loop = asyncio.get_event_loop()
	task = loop.create_task(coroutine)
	
	print(task)

	try:
		t1 = threading.Thread(target=loop.run_until_complete, args=(task,))

		t1.start()

		# is running 
		time.sleep(1)
		print("11111")
		print(task)
		print("22222")
		t1.join()

	except KeyboardInterrupt as e :
		#print(e)
		task.cancel()
		print(task)

	finally :
		print("finally")
		print(task)
		