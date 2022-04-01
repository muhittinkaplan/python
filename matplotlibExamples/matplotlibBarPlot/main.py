import matplotlib.pyplot as plt
fig,ax = plt.subplots()
city = ['ankara', 'istanbul', 'izmir', 'adana', 'bursa']
rank = [23,10,5,8,11]
ax.bar(city,rank)
plt.show()