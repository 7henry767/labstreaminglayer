import sys; sys.path.append('..')  # make sure that pylsl is found (note: in a normal program you would bundle pylsl with the program)
import pylsl
import random
import time

# first create a new stream info (here we set the name to MyMarkerStream, the content-type to Markers, 1 channel, irregular sampling rate, and string-valued data)
# The last value would be the  locally unique identifier for the stream as far as available, e.g. program-scriptname-subjectnumber (you could also omit it but interrupted connections wouldn't auto-recover).
# The important part is that the content-type is set to 'Markers', because then other programs will know how to interpret the content
info = pylsl.stream_info('MyMarkerStream','Markers',1,0,pylsl.cf_string,'dgeyurtutu567sdf');

# next make an outlet
outlet = pylsl.stream_outlet(info)

print("now sending markers...")
markernames = ['Test', 'Blah', 'Marker', 'XXX', 'Testtest', 'Test-1-2-3']
while True:
	# choose a marker string randomly and store it as a pylsl.vectorstr (note that this is actually a list since there can be multiple channels in the sample, even though it is of little use for markers)
	mysample = pylsl.vectorstr([ random.choice(markernames) ])
	# now send it and wait for a bit
	outlet.push_sample(mysample)
	time.sleep(random.random()*3)
