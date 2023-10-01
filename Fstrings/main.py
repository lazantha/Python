import datetime
name='mike'
age=25
weight=60.45644
wind=0.454
net_worth=178747395942
# print(f'name is {name} and age is {age} and weight is {weight:.3f} and wind {wind:.2%} and net worth: {net_worth:,}')


cur=datetime.datetime.now()
# Y=Year
# m=month
# d=day
# H=Hour
# m=minute
# S=Second

print(f'{cur:%Y}')



