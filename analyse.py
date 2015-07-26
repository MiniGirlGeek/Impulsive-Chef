import glob, csv
import matplotlib.pyplot as plt
import sys

#print(sys.argv)

csv_files = glob.glob('./data/*.csv')

for file in csv_files:
    no_click = 0
    no_error = 0
    clicked = 0
    csvfile = open(file)
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Error Type'] == '':
            no_error += 1
        elif row['Error Type'] == 'clicked':
            clicked += 1
        else:
            no_click += 1

    total = float(no_error + clicked + no_click)
    labels = 'No Error', 'Click Error', 'No Click Error'
    sizes = [no_error, clicked, no_click]
    colors = ['yellowgreen', 'lightskyblue', 'lightcoral']

    plt.pie(sizes, labels=labels, colors=colors, shadow=True, startangle=45)
    plt.axis('equal')

    plt.savefig(file + '.png', dpi=50, orientation='portrait', format='png',
            transparent=True)
    plt.clf()
