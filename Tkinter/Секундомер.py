from tkinter import *
from datetime import datetime
import time
import random

# Закрытие программы
def close():
	global running
	running = False

win = Tk()
win.geometry('500x600')
win.title('Секундомер!!!')
win.protocol('WM_DELETE_WINDOW', close)
win.resizable(False, False)

canvas_2 = Canvas(win)
canvas_2.place(x=0, y= 0, width=500, height=600)

# Функции секундомера
temp = 0
after_id = ''
def zps_1():
	global temp, after_id
	after_id = win.after(1000, zps_1)
	f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
	cnt_1.configure(text=str(f_temp))
	temp += 1
	

def start_zps_1():
	btn_1.place_forget()
	btn_2.place(x=40, y=480)
	zps_1()

# Функция остановки секундмера
def stop_1():
	global temp, ser
	btn_2.place_forget()
	btn_3.place(x=30, y=450)
	btn_4.place(x=30, y=520)
	win.after_cancel(after_id)

# Функция продолжения секундомера
def contin():
	btn_3.place_forget()
	btn_4.place_forget()
	btn_2.place(x=40, y=480)
	zps_1()

# Функция сброса
def Rst():
	global temp, after_id
	btn_3.place_forget()
	btn_4.place_forget()
	temp = 0
	cnt_1.configure(text='00:00')
	btn_1.place(x=40, y=480)



def create_objects(N):
	object_list = []
	for i in range(N):
		x = random.randint(100, 500 - 100)
		y = random.randint(100, 600 - 100)
		speed_x = random.randint(0, 4) - 2
		speed_y = random.randint(0, 2) - 2
		r = 20
		simpl_object = canvas_2.create_oval(x - r, y - r, x + r, y + r, 
														fill='red', outline='green', width=3)

		config = {'sml_object':simpl_object,
					'speed_x':speed_x,
					'speed_y':speed_y} 

		object_list.append(config)
	return object_list



# Реализация кнопок начала и конца отсчёта
btn_1 = Button(win, text="Play", bg="black", fg="red", font=('Arial Bold', 35), command=start_zps_1, width=15)
btn_1.place(x=40, y=480)
btn_2 = Button(win, text="Stop", bg="black", fg="red", font=('Arial Bold', 35), width=15, command=stop_1)
btn_3 = Button(win, text="Continue", bg="black", fg="red", font=('Arial Bold', 25), width=23, command=contin)
btn_4 = Button(win, text="Resert", bg="black", fg="red", font=('Arial Bold', 25), width=23, command=Rst)


# Реализация картинки в приложении путём создания объекта
chees = PhotoImage(file='Часики.png')
chees = chees.subsample(7, 7)

# Реализация окна для счётчика
cnt_1 = Label(win, text='00:00',font=('Arial Bold', 50))
cnt_1.place(x=165, y=210)


txt = PhotoImage(file='image(1).png')
age = True
objects = create_objects(100)
running = True
while running:
	if age:
		txtIMG = canvas_2.create_image(250, 70, anchor=CENTER, image = txt)
		cheesImg = canvas_2.create_image(250,260, anchor=CENTER, image = chees)
		age = False
	for config in objects:
		canvas_2.move(config['sml_object'], config['speed_x'], config['speed_y'])

		Pashok = canvas_2.coords(config['sml_object'])
		if Pashok[0] < 0 or Pashok[2] > 500:
			config['speed_x'] = -config['speed_x']
		if Pashok[1] < 0 or Pashok[3] > 600:
			config['speed_y'] = -config['speed_y']
	canvas_2.move(chees, 0, 0)
	win.update()
	time.sleep(0.01)

win.destroy()
