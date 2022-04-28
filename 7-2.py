import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

values = np.loadtxt('data.txt', dtype = float)

T = 0
deltaU = 3.3/256                
with open('settings.txt', 'r') as f:
    str = f.read().split('\n')
    T = float(str[0])
    deltaU = float(str[1])

tInc = values.argmax() / len(values) * T
tDec = T - tInc

values = values * deltaU
t = np.array([val /len(values) *  T for val in range(0, len(values))], dtype = float)

values = values[::3]
t = t[::3]

xmin = 0
xmax = 90

ymin = 0
ymax = 3.5

ymajorstep = 0.5
yminorstep = 0.1

xminorstep = 1
xmajorstep = 10


"""                 START GRAPHICS SETTINGS             """

"""             FONT SIZE AND PICTURE RESOLUTION        """

mpl.rcParams['font.size'] = 16

fig = plt.figure(figsize = (10, 10), dpi = 400)
axes = fig.add_subplot()

"""                 TITLE AND LABELS                    """

plt.title('График зависимости напряжения от времени')
plt.xlabel('Время $t$, с')
plt.ylabel('Напряжение $U$, В')

"""                POINT SETTINGS                       """

plt.errorbar(t, values, fmt = '.', color = 'red')

"""                 LINE SETTING                        """

plt.plot(t, values, label = 'Зависимость $U(t)$', color = 'blue', linestyle='--')

"""                 TEXT SITTINGS                       """ 

plt.text(55, 3, 'Время зарядки {:.1f} с\nВремя разрядки {:.1f} с'.format(tInc, tDec))

"""         START OUTPUT AND CALCULATING PROCESS        """

def getticks(min, max, step):
    return np.arange(min, max, step)

"""                         Y AXES                       """

axes.set_yticks(getticks(ymin, ymax, ymajorstep))
axes.set_yticks(getticks(ymin, ymax, yminorstep), minor = True)

"""                         x AXES                       """

axes.set_xticks(getticks(xmin, xmax, xmajorstep))
axes.set_xticks(getticks(xmin, xmax, xminorstep), minor = True)

plt.xlim([xmin, xmax])
plt.ylim([ymin, ymax])

plt.legend()

plt.grid(b = True, which = 'major', c = 'black', alpha = 0.9)
plt.grid(b = True, which = 'minor', c = 'gray',  alpha = 0.3, linestyle = '--')

#plt.show()
"""         creat out file and graphic in folder        """

fmt = 'svg'
plt.savefig('RC_plot.' + fmt, format = fmt)