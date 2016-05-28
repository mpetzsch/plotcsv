"""
Multi plots: scatter, histogram, cumulative distribution
args: filename
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

fileName = sys.argv[1]
data = np.genfromtxt(fileName, delimiter=',', names=True)
x = data[data.dtype.names[0]]
ys = np.delete(data.dtype.names, 0)

# if you plot more that len(colors) data points then you'll get index out of bounds at the moment
colors ='bgrcmyk'

# TODO need to find a nicer way of full screening this
fig = plt.figure(1, figsize=(20,10))
fig.suptitle(fileName, fontsize=14, fontweight='bold')

# subplot for the scatter
plt.subplot(211)
for series in xrange(len(ys)):
    plt.scatter(data['idx'], data[ys[series]], c=colors[series], alpha=0.9, edgecolors='face', label=ys[series])
plt.grid(True)
plt.title('all data points')
plt.ylabel('time (ms)')
plt.xlabel('iteration')
plt.legend(loc='best', ncol=3, fancybox=True, shadow=False, framealpha=0.5, fontsize=10)

# subplot for the histogram
plt.subplot(223)
for series in xrange(len(ys)):
    plt.hist(data[ys[series]], bins=len(data), alpha=0.5, label=ys[series], cumulative=False, histtype='stepfilled')
plt.grid(True)
plt.title('histogram')
plt.ylabel('count')
plt.xlabel('time')
plt.legend(loc='best', ncol=3, fancybox=True, shadow=False, framealpha=0.5, fontsize=10)

# subplot for the cumulative distribution
plt.subplot(224)
for series in xrange(len(ys)):
    plt.hist(data[ys[series]], bins=len(data), alpha=0.5, label=ys[series], cumulative=True, histtype='stepfilled')
plt.grid(True)
plt.title('cumulative distribution')
plt.ylabel('count')
plt.xlabel('time')
plt.legend(loc='best', ncol=3, fancybox=True, shadow=False, framealpha=0.5, fontsize=10)
plt.savefig(fileName + '.png', dpi=200)
plt.show()
