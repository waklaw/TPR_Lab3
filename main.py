import pandas as pd

pd.options.display.max_columns = 9
pd.set_option('display.width', 1400)

file = open('data.txt', encoding="utf8")
data = [line.rstrip('\n') for line in file]

line1 = data[0]
line2 = data[1]
line3 = data[2]
line4 = data[3]
line5 = data[4]
line6 = data[5]

number1 = float(line1[:2])
cand11 = line1[2:3]
cand12 = line1[3:4]
cand13 = line1[4:5]

number2 = float(line2[:2])
cand21 = line2[2:3]
cand22 = line2[3:4]
cand23 = line2[4:5]

number3 = float(line3[:2])
cand31 = line3[2:3]
cand32 = line3[3:4]
cand33 = line3[4:5]

number4 = float(line4[:2])
cand41 = line4[2:3]
cand42 = line4[3:4]
cand43 = line4[4:5]

number5= float(line5[:2])
cand51 = line5[2:3]
cand52 = line5[3:4]
cand53 = line5[4:5]

number6 = float(line6[:2])
cand61 = line6[2:3]
cand62 = line6[3:4]
cand63 = line6[4:5]

#Метод Борда

def Index(lines, symbol):
    mn = 0
    if lines.index(symbol) == 2:
        mn = 2
    if lines.index(symbol) == 3:
        mn = 1
    if lines.index(symbol) == 4:
        mn = 0
    return mn

#Кандидат А
sumA = (number1 * Index(line1,'А')) + (number2 * Index(line2,'А')) + (number3 * Index(line3,'А')) + (number4 * Index(line4,'А')) + (number5 * Index(line5,'А')) + (number6 * Index(line6,'А'))
#Кандидат Б
sumB = (number1 * Index(line1,'Б')) + (number2 * Index(line2,'Б')) + (number3 * Index(line3,'Б')) + (number4 * Index(line4,'Б')) + (number5 * Index(line5,'Б')) + (number6 * Index(line6,'Б'))
#Кандидат С
sumC = (number1 * Index(line1,'С')) + (number2 * Index(line2,'С')) + (number3 * Index(line3,'С')) + (number4 * Index(line4,'С')) + (number5 * Index(line5,'С')) + (number6 * Index(line6,'С'))

print("Кандидат А:",sumA)
print("Кандидат Б:",sumB)
print("Кандидат С:",sumC)

if sumA > sumB and sumA > sumC:
    print("За методом Борда: переможець кандидат А з рахунком", sumA, "очків")
elif sumB > sumA and sumB > sumC:
    print("За методом Борда: переможець кандидат Б з рахунком", sumB, "очків")
elif sumC > sumA and sumC > sumB:
    print("За методом Борда: переможець кандидат C з рахунком", sumC, "очків")
else:
    print("Переможця за методом Борда не знайдено.")

#Метод Кондорсе
ab = 0
ba = 0
bc = 0
cb = 0
ac = 0
ca = 0

for line in data:
    if Index(line,'А') > Index(line,'Б') > Index(line,'С') or Index(line,'С') > Index(line,'А') > Index(line,'Б'):
        ab += float(line[:2])
    elif Index(line,'Б') > Index(line,'А') > Index(line,'С') or Index(line,'С') > Index(line,'Б') > Index(line,'А'):
        ba += float(line[:2])
if ab > ba:
    print("В змаганнях один на один А - Б","-", "А>Б")
elif ba > ab:
    print("В змаганнях один на один А - Б","-", "Б>А")
else:
    print("Переможця за методом Кондорсе не знайдено.")

for line in data:
    if Index(line,'Б') > Index(line,'С') > Index(line,'А') or Index(line,'А') > Index(line,'Б') > Index(line,'С'):
        bc += float(line[:2])
    elif Index(line,'С') > Index(line,'Б') > Index(line,'А') or Index(line,'А') > Index(line,'С') > Index(line,'Б'):
        cb += float(line[:2])
if bc > cb:
    print("В змаганнях один на один Б - С","-", "Б>С")
elif cb > bc:
    print("В змаганнях один на один Б - С","-", "С>Б")
else:
    print("Переможця за методом Кондорсе не знайдено.")

for line in data:
    if Index(line,'А') > Index(line,'С') > Index(line,'Б') or Index(line,'Б') > Index(line,'А') > Index(line,'С'):
        ac += float(line[:2])
    elif Index(line,'С') > Index(line,'А') > Index(line,'Б') or Index(line,'Б') > Index(line,'А') > Index(line,'С'):
        ca += float(line[:2])
if ac > ca:
    print("В змаганнях один на один А - С","-", "А>С")
elif ca > ac:
    print("В змаганнях один на один А - С","-", "С>А")
else:
    print("Переможця за методом Кондорсе не знайдено.")

if ab > ba and ac > ca:
    print("За методом Кондорсе: переможцем є кандидат А")
elif bc > cb and ba > ab:
    print("За методом Кондорсе: переможцем є кандидат Б")
elif ca > ac and cb > bc:
    print("За методом Кондорсе: переможцем є кандидат С")
else:
    print("Переможця за методом Кондорсе не знайдено.")