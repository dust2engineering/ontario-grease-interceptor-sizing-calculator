#!/usr/bin/env python3
"""Grease interceptor flow rate — OBC 2024, Sentence 7.4.4.3.(7).
Usage: python3 grease_interceptor.py DDT_SECONDS PUMP_L_PER_S VOLUME_L [VOLUME_L ...]
Q = SUM(0.75 x V / DDT) + PD.  Fixture volume V is the full brim capacity in
litres (the 0.75 factor accounts for a fixture filled to about 75% with
displacement by contents). Select an interceptor rated at or above Q.
"""
import sys

def main():
    if len(sys.argv) < 4:
        print(__doc__); return
    ddt, pd = float(sys.argv[1]), float(sys.argv[2])
    vols = [float(x) for x in sys.argv[3:]]
    q = sum(0.75 * v / ddt for v in vols) + pd
    for v in vols:
        print(f"  fixture {v:g} L -> {0.75 * v / ddt:.3f} L/s")
    if pd: print(f"  pump discharge -> {pd:g} L/s")
    print(f"Q = {q:.2f} L/s = {q * 60:.1f} L/min = {q * 60 / 3.785:.1f} US gpm")
    print("Select a CSA B481.1/B481.2 rated interceptor with capacity at or above Q, located as close as possible to the fixtures (7.4.4.3.(6)).")

if __name__ == "__main__":
    main()
