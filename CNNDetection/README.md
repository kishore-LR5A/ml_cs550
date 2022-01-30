## **How to train and test:**

> Before running, download the mentioned datasets and place in appropriate folders.

## Training dataset:

> https://drive.google.com/file/d/132WMLKn65vgYGjUEGOF2x34-Q17dw-Wv/view?usp=sharing

## Validataion dataset:

> https://drive.google.com/drive/folders/1FlgtItrY9pbhNRBcPaKZDHf3NNI8_Bth?usp=sharing

## Testing data:

> Execute the bash script in dataset/test/download_testset.sh and delete stylegan, stylegan2 and whichfaceisreal folders.

> We trained two classifiers one with resnet101 and other with resnet152.If you want to run resnet101 code then you can run directly.Currently, resnet152 code is commented out in networks/trainer.py, data/datasets.py, demo.py and eval.py. If you want to run resnet152 code please comment out the resnet101 code and activate resnet152 code.

## For training execute this command:

> python train.py --name blur_jpg_prob0.5 --blur_prob 0.5 --blur_sig 0.0,3.0 --jpg_prob 0.5 --jpg_method cv2,pil --jpg_qual 30,100 --dataroot ./dataset --classes bedroom,car,cat --batch_size 32 --num_threads 2

#### Once the training is done you will get a checkpoints folder in the main directory, where tensorboard data is stored in train(loss) and val(accuracy and average precesion) subfolders along with three models.

## For testing execute this command:

> python3 eval.py --num_threads 2

### Once the testing is done results are stored in results folder in main directory in a csv format.

## If you want to checkout our checkpoints folders:

> resnet101: https://drive.google.com/file/d/1edY7stzT3fVqG0ajGv6w4IQHbgo5mp0H/view?usp=sharing

> resnet152: https://drive.google.com/file/d/1--iERpFm1Hz2rQtykyYcE9pps7jNCvc8/view?usp=sharing
> These zip files contains our checkpoints folders we obtained during training.

## If you want to checkout our results folders:

> resnet101: https://drive.google.com/file/d/1--IY2-8_mozYuB34NZn5Tci_FHsotfaQ/view?usp=sharing

> resnet152: https://drive.google.com/file/d/1-2ulRFE2e_mVSOK8EiXnwV9iXhAgDLHE/view?usp=sharing
> These zip files contains our results folders we obtained during training.
