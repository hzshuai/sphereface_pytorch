#!/bin/sh

python27 -u ms_celeb_align_112x96.py --lfw=1 --nproc=2 \
--data-dir=/data/Datasets/msra_lfw/lfw \
--lmk=lfw_lmk \
--output-dir=lfw_112x96 \
> log-align.log 2>&1 &

