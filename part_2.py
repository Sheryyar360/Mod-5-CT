

books_purchased = int(input('Please enter the # of books purchased this month: '))
num_points = 0

if books_purchased == 0:
    num_points += 0
if books_purchased == 2:
    num_points += 5
if books_purchased == 4:
    num_points += 15
if books_purchased == 6:
    num_points += 30
if books_purchased >= 8:
    num_points += 60

print(f'You have been awarded {num_points} points')

