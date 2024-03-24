import matplotlib.pyplot as plt

# Predefined intersection point by avarage values for MEN
intersection_x, intersection_y = 13.25, 12.04

# Coordinates of the points to be plotted
# points = [(8, 13), (10, 13), (0, 0)]  # Example points

# Create a figure and axis
fig, ax = plt.subplots()

# Plotting the points
ax.plot(5, 6, 'bo', label='person2')
ax.annotate('Лице 2', xy=(5, 6), xytext=(5, 8), color='blue', 
            arrowprops=dict(facecolor='black', shrink=0.2, width=1, headwidth=5, headlength=5))

# ranges for WOMEN
# ax.set_xlim(8.18, 18.32)
# ax.set_ylim(7.63, 16.45)
ax.set_xlim(4, 18.32)
ax.set_ylim(5, 16.45)

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
plt.title('EPQ – Ayzenk (Bulgarian WOMEN)')
x_offset=3
plt.text(5+x_offset,16,'Сангвиник', fontsize=14)
plt.text(13+x_offset,16,'Холерик', fontsize=14)
plt.text(5+x_offset,8, 'Флегматик', fontsize=14)
plt.text(13+x_offset,8, 'Меланхолик', fontsize=14)
# plt.show()

plt.savefig('/home/akafazov/temp/aysenc/chart-women.png')


