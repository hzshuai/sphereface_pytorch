from __future__ import print_function

import os
import argparse
import numpy as np
import cv2
from multiprocessing import Process, Queue, Array
from matlab_cp2tform import get_similarity_transform_for_cv2

def alignment_large(src_img,src_pts):
    of = 2
    ref_pts = [ [30.2946+of, 51.6963+of],[65.5318+of, 51.5014+of],
        [48.0252+of, 71.7366+of],[33.5493+of, 92.3655+of],[62.7299+of, 92.2041+of] ]
    crop_size = (96+of*2, 112+of*2)

    s = np.array(src_pts).astype(np.float32)
    r = np.array(ref_pts).astype(np.float32)

    tfm = get_similarity_transform_for_cv2(s, r)
    face_img = cv2.warpAffine(src_img, tfm, crop_size)
    return face_img

def alignment(src_img,src_pts):
    ref_pts = [ [30.2946, 51.6963],[65.5318, 51.5014],
        [48.0252, 71.7366],[33.5493, 92.3655],[62.7299, 92.2041] ]
    crop_size = (96, 112)
    src_pts = np.array(src_pts).reshape(5,2)

    s = np.array(src_pts).astype(np.float32)
    r = np.array(ref_pts).astype(np.float32)

    tfm = get_similarity_transform_for_cv2(s, r)
    face_img = cv2.warpAffine(src_img, tfm, crop_size)
    return face_img


def do_align(args, filelist):
    cnt = 0
    while True:
        filename = filelist.get()
        if filename.endswith('\n'):
            filename = filename[:-1]
        if filename == 'FINISH':
            filelist.put('FINISH')
            break
        cnt += 1
        if cnt % args.print_inter == 0:
            print('cnt = ', cnt)
        split = filename.split()
        image_path = split[0]
        if args.lfw:
            split = split[2:]
        else :
            split = split[1:]

        img = cv2.imread(os.path.join(args.data_dir, image_path), 1)

        src_pts = []
        for i in range(5):
            src_pts.append([int(split[2 * i]), int(split[2 * i + 1])])
        img = alignment(img, src_pts)

        output_path = os.path.join(args.outpu_dir, image_path)
        output_dir = os.path.dirname(output_path)
        if os.path.exists(output_dir):
            os.makedirs(output_dir)

        cv2.imwrite(output_path, img)


def run(args):
    filelist = Queue()
    with open(args.lmk) as fin:
        for line in fin.xreadlines():
            filelist.put(line.strip())
    for i in range(args.nproc):
        filelist.put('FINISH')
        p = Process(target = do_align, args=(args, filelist))
        p.start()
        print('start process: ', i)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ms celeb align 112x96')
    parser.add_argument('--data-dir', type=str)
    parser.add_argument('--lmk', type=str)
    parser.add_argument('--nproc', type=int)
    parser.add_argument('--output-dir', type=str)
    parser.add_argument('--lfw', type=int)
    parser.add_argument('--print-inter', type=int)


    args = parser.parse_args()

    run(args)

    '''
    python27 -u ms_celeb_align_112x96.py --lfw=1 --nproc=2 --data-dir=  --lmk= --output-dir=
    '''

