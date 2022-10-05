""" You sell lemonade over 2 weeks, the list show
number of lemonades psold per day

- profit for each lemonade: 1.5 $

- add another day to week 2 list by by capturing a number as input

- combine the 2 lists into the list called "sales"

- calculate / print how much is earned on:
    - > Best day
    - > worst day
    - > separately and in total """

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = [] 

new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
sales = sales_w1 + sales_w2
worst_day_prof = min(sales) * 1.5
best_day_prof = max(sales) * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')