
import random


name = input('Введите своё имя: ')

print ('Введите ваш пол,буква (м\ж): ')

p = str(input()); 

classm = ["Варвар","Лучник","Маг","Инженер","Друид"]
classw = ["Амазонка", "Лучница", "Чародейка","Снайперша","Нимфа"]

if p == 'м':
 c = str(random.choice(classm))
 barbarian = ["Удар топором", "Рывок", "Стан", "Форма воина", "Бросок топора", "Режим защиты", "Ярость"] 
 b = c
 if b == 'Варвар':
 print(f'Ваши скиллы:{random.sample(barbarian, k=3)}')
 
 archer = ["Мощный залп", "Уворот", "Стан", "Град стрел", "Капкан", "Призыв волка", "Невидимость"] 
 a = c
 if a == 'Лучник':
 print(f'Ваши скиллы:{random.sample(archer, k=3)}')
 
 magic = ["Магическая стрела", "Молния", "Огненный шар", "Удушье", "Проклятье", "Бестелесная форма", "Град"] 
 d = c
 if d == 'Маг':
 print(f'Ваши скиллы:{random.sample(magic, k=3)}')
 
 ing = ["Мина", "Ракетница", "Экзоскелет", "Залп бомб", "Турель", "Наращивание брони", "Станящая мина"] 
 e = c
 if e == 'Инженер':
 print(f'Ваши скиллы:{random.sample(ing, k=3)}')
 
 druid = ["Форма медведя", "Рев", "Месть природы", "Призыв энта", "Лечение", "Защита от магии", "Форма грифона"] 
 f = c
 if b == 'Друид':
 print(f'Ваши скиллы:{random.sample(druid, k=3)}')
 
 print(f'Ваш класс:{c}')
if p == 'ж':
 c = str(random.choice(classw))
 barbarianw = ["Метание копья", "Рывок", "Стан", "Уклонение", "Круговой удар копьем", "Режим защиты", "Ярость"] 
 x = c
 if x == 'Амазонка':
 print(f'Ваши скиллы:{random.sample(barbarianw, k=3)}')
 
 archerw = ["1000 выстрелов", "Уворот", "Стан", "Град стрел", "Капкан", "Призыв пумы", "Невидимость"] 
 z = c
 if z == 'Лучница':
 print(f'Ваши скиллы:{random.sample(archerw, k=3)}')
 
 magicw = ["Магическая стрела", "Молния", "Метеорит", "Вселение", "Проклятье", "Бестелесная форма", "Невидимость"] 
 y = c
 if y == 'Чародейка':
 print(f'Ваши скиллы:{random.sample(magicw, k=3)}')
 
 ingw = ["Меткий выстрел", "Граната", "Невидимость", "Уклонение", "Залп", "Критические попадания", "Станящая мина"] 
 l = c
 if l == 'Снайперша':
 print(f'Ваши скиллы:{random.sample(ingw, k=3)}')
 
 druidw = ["Бестелесная форма", "Оплетание корнями", "Месть природы", "Призыв фей", "Лечение", "Защита от магии", "Форма королевы пум"] 
 o = c
 if o == 'Нимфа':
 
print(f'Ваши скиллы:{random.sample(druidw, k=3)}')
 
print(f'Ваш класс:{c}')

print(f'Ваше имя: {name}')