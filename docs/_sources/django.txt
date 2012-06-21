Plotting from Django
====================

This is a riff on http://www.scipy.org/Cookbook/Matplotlib/Django::

     import django
     from boomslang import *

     def simple(request):
         plot = Plot()
         line = Line()
         line.yValues = [25, 40, 30, 23, 10, 50]
         line.xValues = range(len(line.yValues))

         plot.add(line)
         plot.setXLabel("X Label")
         plot.setYLabel("Y Label")
         plot.setYLimits(0,60)

         response=django.http.HttpResponse(content_type='image/png')

         plot.save(response)
         return response



This is getting a little off-topic, but multiple views of plots has produced
strange results in mod-python, this is a dumb hack to plot in a separate
process (replacing the plot.save(response) line above)::

     subproc = subprocess.Popen(['python','-c',
     """
     from boomslang import *
     from cPickle import *
     import sys

     plot = load(sys.stdin)
     plot.save(sys.stdout)
     """],
                         env={'PYTHONPATH':":".join(sys.path),
                              'MPLCONFIGDIR':os.environ.get('MPLCONFIGDIR','/tmp')},
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

     cPickle.dump(multiplot, subproc.stdin)
     png = subproc.communicate()[0]

     print >>response, png


