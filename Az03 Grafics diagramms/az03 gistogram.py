import matplotlib.pyplot as plt

data = [ 5,7,10,11,12,6,6,8,9,1,2,3,3,4,5,5,5]

plt.hist(data, bins = 3 )


plt.xlabel("часы сна")
plt.ylabel("количество людей")
plt.title("гистограмма количства часов сна")

plt.show()
