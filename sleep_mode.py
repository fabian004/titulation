import asyncio
import psutil
async def proximitly_sensor():
    mem = psutil.virtual_memory()
    total_memory = mem.total / (1024 * 1024)
    available_memory = mem.available / (1024 * 1024)
    used_memory = mem.used / (1024 * 1024)
    print("proximitly")
    print(total_memory)
    print(used_memory)
    print(available_memory)

async def pressure_sensor():
    print("pressure")

async def main():
    await asyncio.gather(proximitly_sensor(), pressure_sensor())

def sleepMode(mode):
    asyncio.run(main())


    

