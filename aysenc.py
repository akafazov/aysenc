import matplotlib.pyplot as plt

# Predefined intersection point by avarage values for MEN
intersection_x, intersection_y = 9.69, 12.76

# Coordinates of the points to be plotted
# points = [(8, 13), (10, 13), (0, 0)]  # Example points

# Create a figure and axis
fig, ax = plt.subplots()

# Plotting the points
# for point in points:
#     ax.plot(point[0], point[1], 'bo', label='Лице 1')  # 'bo' stands for "blue dot"
ax.plot(8, 13, 'bo', label='person1')
ax.annotate('Лице 1', xy=(8, 13), xytext=(7, 15), color='blue', 
            arrowprops=dict(facecolor='black', shrink=0.2, width=1, headwidth=5, headlength=5))

ax.plot(5, 9, 'bo', label='person3')
ax.annotate('Лице 3', xy=(5, 9), xytext=(5, 11), color='blue', 
            arrowprops=dict(facecolor='black', shrink=0.2, width=1, headwidth=5, headlength=5))

# ranges for MEN
ax.set_xlim(4.60, 14.78)
ax.set_ylim(8, 17.09)

# Moving the spines
ax.spines['left'].set_position(('data', intersection_x))
ax.spines['bottom'].set_position(('data', intersection_y))

# Hiding the top and right spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Adjusting the ticks to account for the new origin
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.xlabel('Невротизъм', loc='right', fontsize=8)
plt.ylabel('Екстраветрност', loc='top', fontsize=8)
plt.title('EPQ – Ayzenk (Bulgarian MEN)')
plt.text(5,16,'Сангвиник', fontsize=14)
plt.text(13,16,'Холерик', fontsize=14)
plt.text(5,8, 'Флегматик', fontsize=14)
plt.text(13,8, 'Меланхолик', fontsize=14)
# plt.show()

plt.savefig('/home/akafazov/temp/aysenc/chart-men.png')


