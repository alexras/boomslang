# About Boomslang

I created Boomslang to decrease the amount of boilerplate code I had to write
when producing graphs for research papers. Boomslang treats data and plots
separately and encapsulates them both in objects, giving the programmer the
ability to author modular, re-usable graphing code.

# Downloading Boomslang

The current stable version of Boomslang is [0.6
beta](https://github.com/downloads/alexras/boomslang/boomslang-0.6b.tar.gz). For
a list of new features and bug fixes in this version, check the changelog in
the wiki.

Boomslang requires `matplotlib`. You can get it at [their GitHub
page](http://github.com/matplotlib/matplotlib) or install it through your
favorite package management utility like pip.

Since the rate of churn of Boomslang's feature set is still pretty high, I
recommend that people use Boomslang by checking out a read-only copy of the
repository.

# Documentation

Documentation is available at [http://alexras.github.com/boomslang/docs/](http://alexras.github.com/boomslang/docs/)

# FAQ

Q: `Plot.plot()` seems to fail silently, but `Plot.save()` works. How do I fix this?

A: The most likely explanation is that your configured backend doesn't support
anything but saving. You can try changing your backend to Agg by editing your
`~/.matplotlib/matplotlibrc` file and adding the following line:

`Agg: Agg`

# Staying Up-To-Date

Users of Boomslang are encouraged to subscribe to the (low-traffic)
[boomslang-users mailing list](http://groups.google.com/group/boomslang-users). Feature
suggestions and bug reports can be filed using the Issues tab above. If you
want to stay informed about commits to Boomslang, you can subscribe to the
[commits RSS feed](https://github.com/alexras/boomslang/commits/master.atom).

# Troubleshooting

First, check the FAQ; if a question gets asked more than about twice, I'll put
it there. Then, ask the mailing list, file an issue, or ask me directly.
