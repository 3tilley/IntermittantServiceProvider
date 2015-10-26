import sqlite3
import ping
import statistics
from datetime import datetime, date
import socket
import sys

'''
CREATE TABLE ping(
    timestamp   MEDIUMINT,
    host        INT,
    iswifi      BOOLEAN
    count       INTEGER,
    lost        INTEGER,
    min         DOUBLE,
    max         DOUBLE,
    mean        DOUBLE,
    median      DOUBLE,
    stdev       DOUBLE
);

CREATE TABLE target(
    hostkey     INT,
    hostaddress VARCHAR(50)
);
'''

def pings_to_dict(pings):
    d = {
        "count" : len(pings),
        "lost" : sum(x is None for x in pings),
        "min" : min(pings),
        "max" : max(pings),
        "mean" : statistics.mean(pings),
        "median" : statistics.median(pings),
        "stdev" : statistics.stdev(pings)
    }
    return d
    
def make_insert_statement(host_key, timestamp, is_wifi, p):
    s = "INSERT INTO ping VALUES({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9});"\
    .format(timestamp, host_key, int(is_wifi), p["count"], p["lost"], p["min"], p["max"],\
                p["mean"], p["median"], p["stdev"])
    return s
    
def to_timestamp(dt):
    return (dt - datetime(1970, 1, 1)).total_seconds()
                
def make_ping_list(dest_addr, timeout=2, count=10, psize=64):
    
    plist = []
    
    for i in xrange(count):
        try:
            delay = ping.do_one(dest_addr, timeout, psize)
        except socket.gaierror, e:
            print "failed. (socket error: '%s')" % e[1]
            break
            
        if delay != None:
            delay = delay * 1000
            plist.append(delay)
        
    return plist
        
        
if __name__ == "__main__":
    con = None

    try:
        con = sqlite3.connect('data.db')
        
        cur = con.cursor()
        
        url = "www.google.com"
        
        p = make_ping_list(url, count=10)
        d = pings_to_dict(p)
        s = make_insert_statement(1, to_timestamp(datetime.utcnow()), False, d)
        
        print s
          
        cur.execute(s)
        con.commit()
        print "Ping data commited"
#        data = cur.fetchone()
        
#        print "SQLite version: %s" % data                
        
    except sqlite3.Error, e:
        
        print "Error %s:" % e.args[0]
        sys.exit(1)
        
    finally:
        
        if con:
            con.close()
