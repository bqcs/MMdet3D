# debugProxy.py
import os, sys, runpy

## 1. cd WORKDIR
os.chdir('/media/adas/ubuntu2/hd/mmdetection3d/')
print("当前进程的工作目录：", os.getcwd())
print("------------------------------")

## 2.
args = 'python tools/train.py /media/adas/ubuntu2/hd/mmdetection3d/projects/BEVFusion/configs/only_lidar.py'
## 2B. python -m mymodule.test 4 5
# args = 'python -m mymodule.test 4 5'
args = args.split()   # ['python', 'test.py', '4', '5']
print("DSJNFIDSJNJINNNNNNNNNNNNNNNNN")
if args[0] == 'python':
    """pop up the first in the args""" 
    args.pop(0) #删除第一个元素
if args[0] == '-m':
    """pop up the first in the args"""
    args.pop(0) # 删除第一个元素
    fun = runpy.run_module
else:
    fun = runpy.run_path #runpy.run_path是一个函数，用于执行指定Python脚本文件，先赋值给fun
sys.argv.extend(args[1:]) #args[1:]表示除了test.py之后的参数，传给sys.argv。原本sys.argv是['C:\\Users\\40218\\Desktop\\nsafdj\\dwesfnj.py']这样一个列表
fun(args[0], run_name='__main__')  #args[0]是要执行的文件，比如train.py
