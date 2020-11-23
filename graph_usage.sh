python -m cProfile -o log/speed.log -s cumtime main.py
gprof2dot -f pstats log/speed.log | dot -Tsvg -o log/time_used.svg
