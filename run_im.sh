#!/bin/sh

#export PATH=/Users/hzshuai/anaconda3/envs/python27/bin
#python -u train.py --dataset=/Users/hzshuai/PythonProjects/ai-playground/casia-faces/CASIA-maxpy-clean --maxlistnum=300

# export PATH=/data/huangzhangshuai/anaconda3/envs/python27/bin
# python -u train.py \
# --align=1 \
# --lr=0.1 \
# --dataset=/data/huangzhangshuai/anaconda3/workspace/dataset/CASIA-maxpy-clean \
# > log-1213_v1.log 2>&1 &

export PATH=/data/huangzhangshuai/anaconda3/envs/python27/bin
python -u train.py \
--align=0 \
--lr=0.01 \
--dataset=/data/Datasets/msra_lfw/msra \
--lmk=train-gt-100.txt \
> log-1214.log 2>&1 &


#ps aux | grep train.py | awk '{print $2}' | xargs kill
# eval lfw
# python -u lfw_eval.py --model=sphere20a_19.pth --lfw=/data/Datasets/msra_lfw/lfw/lfw.zip >> lfw_eval.log
