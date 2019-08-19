# Action_Recognition_Conv_BiLSTM_Attention

### Description
Conv+BiLSTM+Attention for Action Recognition

### Requirements


### Dataset

### Dataset Setup
```
python extract_frames.py
```

### Model Architecture

### To run the code
```
python train.py --dataset_path /home/ayush/Activity_Recognition/Action-Recognition/data/UCF-101-frames/ --split_path /home/ayush/Activity_Recognition/Action-Recognition/data/ucfTrainTestlist/ --num_epochs 200 --sequence_length 40 --img_dim 112 --latent_dim 512
```

### Some Experimental Results

### Credits
* [Github Repository](https://github.com/eriklindernoren/Action-Recognition)
