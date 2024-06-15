

num_years = int(input('Please enter the # of years you would like to compute monthly average rainfall for: '))
total_rain = 0
months = 0
for year in range(num_years):
    for month in range(12):
        total_rain += int(input('Please enter inches of rainfall for year {}, month {}: '.format(year + 1,month + 1)))
        months += 1
print('The total rainfall for {} months was {} inches. That\'s an average of {} inches per month'
      .format(months, total_rain, total_rain/months))
