#!/bin/sh

#export PATH=/Users/hzshuai/anaconda3/envs/python27/bin
#python -u train.py --dataset=/Users/hzshuai/PythonProjects/ai-playground/casia-faces/CASIA-maxpy-clean.zip

export PATH=/data/huangzhangshuai/anaconda3/envs/python27/bin
python -u train.py \
--lr=0.0001 \
--dataset=/data/huangzhangshuai/anaconda3/workspace/dataset/CASIA-maxpy-clean.zip \
> log-1213.log 2>&1 &


#ps aux | grep train.py | awk '{print $2}' | xargs kill
# eval lfw
# python -u lfw_eval.py --model=sphere20a_19.pth --lfw=/data/Datasets/msra_lfw/lfw/lfw.zip >> lfw_eval.log
