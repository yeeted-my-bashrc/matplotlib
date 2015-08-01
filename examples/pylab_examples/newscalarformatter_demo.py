# from pylab import *
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.ticker import OldScalarFormatter, ScalarFormatter

x = np.arange(0, 1, .01)
f = plt.figure(figsize=(6, 6))
f.text(0.5, 0.975, 'The old formatter', horizontalalignment='center', verticalalignment='top')
plt.subplot(221)
plt.plot(x*1e5 + 1e10, x*1e-10 + 1e-5)
plt.gca().xaxis.set_major_formatter(OldScalarFormatter())
plt.gca().yaxis.set_major_formatter(OldScalarFormatter())
plt.subplot(222)
plt.plot(x*1e5, x*1e-4)
plt.gca().xaxis.set_major_formatter(OldScalarFormatter())
plt.gca().yaxis.set_major_formatter(OldScalarFormatter())
plt.subplot(223)
plt.plot(-x*1e5 - 1e10, -x*1e-5 - 1e-10)
plt.gca().xaxis.set_major_formatter(OldScalarFormatter())
plt.gca().yaxis.set_major_formatter(OldScalarFormatter())
plt.subplot(224)
plt.plot(-x*1e5, -x*1e-4)
plt.gca().xaxis.set_major_formatter(OldScalarFormatter())
plt.gca().yaxis.set_major_formatter(OldScalarFormatter())

x = np.arange(0, 1, .01)
f = figure(figsize=(6, 6))
f.text(0.5, 0.975, 'The new formatter, default settings', horizontalalignment='center',
       verticalalignment='top')
plt.subplot(221)
plt.plot(x*1e5 + 1e10, x*1e-10 + 1e-5)
plt.gca().xaxis.set_major_formatter(ScalarFormatter())
plt.gca().yaxis.set_major_formatter(ScalarFormatter())
plt.subplot(222)
plt.plot(x*1e5, x*1e-4)
plt.gca().xaxis.set_major_formatter(ScalarFormatter())
plt.gca().yaxis.set_major_formatter(ScalarFormatter())
plt.subplot(223)
plt.plot(-x*1e5 - 1e10, -x*1e-5 - 1e-10)
plt.gca().xaxis.set_major_formatter(ScalarFormatter())
plt.gca().yaxis.set_major_formatter(ScalarFormatter())
plt.subplot(224)
plt.plot(-x*1e5, -x*1e-4)
plt.gca().xaxis.set_major_formatter(ScalarFormatter())
plt.gca().yaxis.set_major_formatter(ScalarFormatter())

x = np.arange(0, 1, .01)
f = figure(figsize=(6, 6))
f.text(0.5, 0.975, 'The new formatter, no numerical offset', horizontalalignment='center',
       verticalalignment='top')
plt.subplot(221)
plt.plot(x*1e5 + 1e10, x*1e-10 + 1e-5)
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.subplot(222)
plt.plot(x*1e5, x*1e-4)
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.subplot(223)
plt.plot(-x*1e5 - 1e10, -x*1e-5 - 1e-10)
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.subplot(224)
plt.plot(-x*1e5, -x*1e-4)
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))

x = np.arange(0, 1, .01)
f = figure(figsize=(6, 6))
f.text(0.5, 0.975, 'The new formatter, with mathtext', horizontalalignment='center',
       verticalalignment='top')
plt.subplot(221)
plt.plot(x*1e5 + 1e10, x*1e-10 + 1e-5)
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.subplot(222)
plt.plot(x*1e5, x*1e-4)
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.subplot(223)
plt.plot(-x*1e5 - 1e10, -x*1e-5 - 1e-10)
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.subplot(224)
plt.plot(-x*1e5, -x*1e-4)
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.show()
