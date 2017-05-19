# PyBvh

Parsing BVH files with Python and converting them to cartesian co-ordinates suitable for animation with `matplotlib`. Adapted from [`cgkit`](http://cgkit.sourceforge.net/) and [`BVHPlay`](https://sites.google.com/a/cgspeed.com/cgspeed/bvhplay). May lose rotation data, so if you were expecting accurate quaternions you're gonna have a bad time.

See `bvh_to_json.py` for usage example.

Compatible with Python 2 and 3, but please use Python 3.

The only requirement is `numpy`.