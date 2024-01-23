from mrjob.job import MRJob
import re

class MRVisibility(MRJob):

    def mapper(self, _, line):
        val = line.strip()
        usaf_id = val[4:10]
        visibility = val[78:84]
        if visibility != "999999" and re.match("[01459]", val[84:85]):
            yield usaf_id, visibility

    def reducer(self, usaf_id, visibility):
        for vis in visibility:
            yield int(usaf_id), int(vis)

if __name__ == '__main__':
    MRVisibility.run()
