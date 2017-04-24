import sys
sys.path.insert(0, '/Users/matthewkirby/lsstdsfp_scratchwork/retrieve_tweets')
import get_recent_tweets as grt

assert len(grt.get_recent_tweets('MillerAdamA', 2)) == 2
assert len(grt.get_recent_tweets('MillerAdamA', 3)) == 3
assert len(grt.get_recent_tweets('MillerAdamA', 4)) == 4
assert len(grt.get_recent_tweets('MillerAdamA', 5)) == 5
