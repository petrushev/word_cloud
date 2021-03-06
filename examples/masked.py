#!/usr/bin/env python2

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'alice.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = imread(path.join(d, "alice_mask.png"))
plt.imshow(alice_mask)


wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=STOPWORDS.add("said"))
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "alice.png"))

# show
plt.figure()
plt.imshow(wc)
plt.show()
