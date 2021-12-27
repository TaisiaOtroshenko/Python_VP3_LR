# Задача 3. По умолчанию цвета осей координат, 
# линий вспомогательной сетки отрисовываются чёрным цветом, 
# а цвет фона (основы рисунка) - белым. Измените параметры рисования, 
# отвечающие за соответствующие цвета на ваше усмотрение и 
# выведите на экран график зависимости амплитуды от времени.

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 10*np.pi+0.1, 0.1)
A = 5 # Амплитуда
T = 5 # Период
x = A*np.sin(1.985*np.pi*t/T+ 0)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_facecolor('#CFCFCF')
ax.set_xlabel('time')
ax.set_ylabel('amplitude')
ax.set_ylim([-10, 10])
ax.set_xlim([-1, 20])
ax.spines['bottom'].set_color('red')
ax.spines['left'].set_color('red')
ax.tick_params(axis='x', colors='red')
ax.tick_params(axis='y', colors='red')
ax.axhline(y=0, xmin= 0, xmax=20, color='green')
ax.axvline(x=0, ymin= -10, ymax=10, color='green')        
           
ax.plot(t, x, color='blue')
plt.grid(True)
plt.title('График зависимости амплитуды от времени')
plt.show()
