### How to plot YOLO loss? 
In order to plot a loss, you first need a log of the <i>darknet train</i> command
For example,below command will save the log into log/aggregate-voc-tiny7.log <br /><br />
```cmd
darknet.exe detector train data/aggregate-voc-tiny7.data cfg/aggregate-voc-tiny7.cfg  backup/aggregate-voc-tiny7/aggregate-voc-tiny7_21000.weights >> log/aggregate-voc-tiny7.log -gpus 0,1
```
Once you have \\path\\to\\log\\aggregate-voc-tiny7.log, plot the loss by executing 
```cmd
python plot_yolo_log.py \\path\\to\\log\\aggregate-voc-tiny7.log
python plot_yolo_log.py <path to log.txt>
```
In Colab
```cmd
./darknet detector train ../data/obj.data cfg/yolo-obj.cfg ../data/darknet53.conv.7 2>&1 > log.txt
%matplotlib inline
from IPython.display import Image
Image('<path to loss_plot.jpg>')
```

