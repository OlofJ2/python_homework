# Added the parsing example seen in class

import pandas, cStringIO

s = """  r              jnu            jnu            jnu            jnu            jnu         
                 0,0,206        0,0,207        0,0,208        0,0,209        0,0,210     
  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00
  2.5000000E-05  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00
  5.0000000E-05  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00
  7.5000000E-05  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00
  1.0000000E-04  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00  0.0000000E+00"""
  
v = cStringIO.StringIO()
v.write(s)
v.seek(0)
df = pandas.read_fwf(v, header=[1,2])
print df.columns
print df.columns[0]
print df.columns[1]
print df.columns[2]
