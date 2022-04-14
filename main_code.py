import matplotlib.pyplot as plt
measured_data = [10, 23, 45, 58, 100, 155, 204, 255]
plt.plot(measured_data)
plt.show()

measured_data_str = [str(item) for item in measured_data]

with open("data.txt", "w") as outfile:
    outfile.write("\n".join(measured_data_str))

# https://www.chipdip.ru/calc
# https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.html
# https://docs.python.org/3/tutorial/inputoutput.html#tut-files
# https://docs.python.org/3/library/functions.html#open
# https://www.youtube.com/watch?v=BadZDjyxTcU&list=PLP3ZxgNn8T5LWXRQ_zDEIBWU6aNSY5KWb&index=33&ab_channel=%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%B8%D1%8F%D0%BF%D1%80%D0%B8%D0%BA%D0%BB%D0%B0%D0%B4%D0%BD%D1%8B%D1%85%D0%BD%D0%B0%D0%BD%D0%BE%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B9
# https://github.com/UniverTime?tab=repositories
