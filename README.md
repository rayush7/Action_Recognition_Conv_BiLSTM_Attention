# Action_Recognition_Conv_BiLSTM_Attention

### Description
Conv+BiLSTM+Attention for Action Recognition

### Requirements
* Python 3.7
* PyTorch


### Dataset
UCF-101 Dataset : [Click here](https://www.crcv.ucf.edu/data/UCF101.php)

### Dataset Setup
The first step involves downloading the dataset and extracting the frames of the videos of the dataset.
```
cd data/              
bash download_ucf101.sh     # Downloads the UCF-101 dataset (~7.2 GB)
unrar x UCF101.rar          # Unrars dataset
unzip ucfTrainTestlist.zip  # Unzip train / test split
python extract_frames.py   # Extracts frames from the video 
```

### Model Architecture

### To run the code
```
python train.py --dataset_path /home/ayush/Activity_Recognition/Action-Recognition/data/UCF-101-frames/ --split_path /home/ayush/Activity_Recognition/Action-Recognition/data/ucfTrainTestlist/ --num_epochs 200 --sequence_length 40 --img_dim 112 --latent_dim 512
```

### Some Experimental Results
* Num Classes : 101
* Epochs : 200  

![Loss Plot](https://github.com/rayush7/Action_Recognition_Conv_BiLSTM_Attention/blob/master/loss_plot.png)
![Accuracy Plot](https://github.com/rayush7/Action_Recognition_Conv_BiLSTM_Attention/blob/master/accuracy_plot.png)



### Credits
* [eriklindernoren Github Repository](https://github.com/eriklindernoren/Action-Recognition)
