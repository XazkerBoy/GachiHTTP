#!/usr/bin/env python3
from time import perf_counter  # Time measurement
import gachi_http as gh  # Library itself

reqs = [gh.get(f"https://google.com") for i in range(10)]  # Get google 10 times with different parameter values
start = perf_counter()  # Start "stopwatch"
resp = gh.map(reqs, verify_ssl=False)  # Map request (execute)
print("GachiHTTP:", perf_counter() - start)  # Print time
print(resp)