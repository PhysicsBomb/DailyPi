from subprocess import call
import sys

call(['scp', 'plan.txt', 'pi@raspberrypi.local:/home/pi/'])

#call(['ssh', 'pi@raspberrypi.local', '-t', 'espeak -a5000  < plan.txt'])

call(['scp', 'TW.txt', 'pi@raspberrypi.local:/home/pi/'])
call(['scp', 'maps.txt', 'pi@raspberrypi.local:/home/pi/'])
call(['scp', 'Date.txt', 'pi@raspberrypi.local:/home/pi/'])
call(['scp', 'news1.txt', 'pi@raspberrypi.local:/home/pi/'])
call(['scp', 'news2.txt', 'pi@raspberrypi.local:/home/pi/'])
call(['scp', 'news3.txt', 'pi@raspberrypi.local:/home/pi/'])
call(['scp', 'news4.txt', 'pi@raspberrypi.local:/home/pi/'])
call(['scp', 'news5.txt', 'pi@raspberrypi.local:/home/pi/'])


while True:
    call(['ssh', 'pi@raspberrypi.local', '-t', 'espeak -a200 -ven+f1 < Date.txt'])
    call(['ssh', 'pi@raspberrypi.local', '-t', 'espeak -a200 -ven+f1 < TW.txt'])

    call(['ssh', 'pi@raspberrypi.local', '-t', 'espeak -a200 -ven+f1 < news1.txt'])
    call(['ssh', 'pi@raspberrypi.local', '-t', 'espeak -a200 -ven+f1 < news2.txt'])
    call(['ssh', 'pi@raspberrypi.local', '-t', 'espeak -a200 -ven+f1 < news3.txt'])
    call(['ssh', 'pi@raspberrypi.local', '-t', 'espeak -a200 -ven+f1 < news4.txt'])
    call(['ssh', 'pi@raspberrypi.local', '-t', 'espeak -a200 -ven+f1 < news5.txt'])

    call(['ssh', 'pi@raspberrypi.local', '-t', 'espeak -a200 -ven+f1 < maps.txt'])
    call(['ssh', 'pi@raspberrypi.local', '-t', 'espeak -a200 -ven+f1 < plan.txt'])

    reloop = sys.stdin.readline()
