# SWRC Fit and hystfit

## SWRC Fit
SWRC Fit is a web interface which uses `unsatfit` and determines parameters for water retention function. As it is easy to use, it has been [used in many papers](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=Gs_ABawAAAAJ&citation_for_view=Gs_ABawAAAAJ:9yKSN-GCB0IC).
 Source code is in the [repository](https://github.com/sekika/unsatfit/tree/main/swrcfit).

- [SWRC Fit](https://seki.webmasters.gr.jp/swrc/)

You can run SWRC Fit locally on your machine by using [Docker](https://www.docker.com/), which might be useful when the server is down or you have unstable network connection. Follow the [instructions here](https://github.com/sekika/unsatfit/blob/main/docker/Readme.md).

[GNU Octave version of SWRC Fit](https://github.com/sekika/swrcfit/blob/master/doc/en/README.md) is no longer maintained but the code is available.

## hystfit
[hystfit](https://sekika.github.io/hystfit/) is a Python library for calculating hysteresis in water retention curve. It is implemented as a subclass of `unsatfit`.
