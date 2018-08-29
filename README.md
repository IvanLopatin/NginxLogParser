# NginxLogParser

```bash
# cat nginx.access.log | ./NginxLogParser.py | more
                                           Request       Count    Avg   Sum
                              GET /kanal%d_%d.html        1628  0.115   187.755
                                             GET /         153  0.290   44.391
                                  GET /film%d.html         107  0.286   30.610
                                 GET /kanal%d.html          80  0.130   10.398
                  HEAD /dowload/new%d/xmltv.xml.gz          78  0.085   6.627
                           GET /new%d/xmltv.xml.gz          72  0.060   4.337
                               GET /kanal%d_%d.old          36  0.117   4.210
                       GET /dawnload/new%d/jtv.zip          36  0.113   4.079
                  GET /download.new%d/xmltv.xml.gz          60  0.066   3.964
                   GET /dowload/new%d/xmltv.xml.gz          78  0.044   3.406
                                        GET /sort/          32  0.095   3.051

```