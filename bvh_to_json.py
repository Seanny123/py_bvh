from skeleton import process_bvhfile

import glob
import os
import json

last_desc = ""

for fi in glob.glob(os.path.join("recordings", "raw", "*.bvh")):
    try:
        print("Processing %s" % fi)
        skel = process_bvhfile(fi)
    except ValueError:
        print("Skipping %s" % fi)
        continue

    body = {}

    for frame in range(skel.frames):

        skel.create_edges_onet(frame)

        for edge in skel.edges[frame]:
            for vert in (edge.wv1, edge.wv2):
                if vert.descr is not last_desc:
                    if vert.descr not in body:
                        body[vert.descr] = []

                    body[vert.descr].append(list(vert.tr[:3]))
                    last_desc = vert.descr

    fi_name = "%s.json" % os.path.splitext(os.path.basename(fi))[0]
    with open(os.path.join("recordings", "converted", fi_name), "w") as out_fi:
        json.dump(body, out_fi)
