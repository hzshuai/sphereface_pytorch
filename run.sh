#!/bin/sh

#export PATH=/Users/hzshuai/anaconda3/envs/python27/bin
#python -u train.py --dataset=/Users/hzshuai/PythonProjects/ai-playground/casia-faces/CASIA-maxpy-clean.zip

export PATH=/data/huangzhangshuai/anaconda3/envs/python27/bin
python -u train.py \
--dataset=/data/huangzhangshuai/anaconda3/workspace/dataset/CASIA-maxpy-clean.zip \
> log-1212.log 2>&1 &


#ps aux | grep train.py | awk '{print $2}' | xargs kill
