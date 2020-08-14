import time

def countdown(t):

    while t:
        hours, r = divmod(t, 60 ** 2)
        mins, secs = divmod(r, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Acabou!!!')

t = '18:38:00'
h, m, s = t.split(':')
ts = (int(h) * 60 ** 2) + (int(m) * 60) + int(s)

countdown(int(ts))
