# Short script to download the iris dataset

import urllib.request
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
dest = '/home/jul-ian/github/iris-practice/data/raw/iris.data'

urllib.request.urlretrieve(url, dest)
