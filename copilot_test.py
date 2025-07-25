import os
import platform

def get_uptime():
    if platform.system() == "Windows":
        import ctypes
        import time
        kernel32 = ctypes.windll.kernel32
        uptime_ms = kernel32.GetTickCount64()
        uptime_sec = int(uptime_ms / 1000.0)
    else:
        with open('/proc/uptime', 'r') as f:
            uptime_sec = int(float(f.readline().split()[0]))
    hours, remainder = divmod(uptime_sec, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"System uptime: {hours}h {minutes}m {seconds}s"

if __name__ == "__main__":
    print(get_uptime())
