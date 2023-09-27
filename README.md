# Lung Cancer Detection using Machine Vision

[lung_cancer_detection(final).webm](https://github.com/ReyeTech/CancerDetection/assets/109020327/d4e50873-e7d6-46bd-a56e-f29f218fdf4f)

This is a custom trained model to detect 3 types of tumors in the lungs
1. Nodule
2. Adenocarcinoma
3. Cancer

## Steps to use the model

## Step 1: Downlaod the pre-trained model

you can download the pre-trained model for pytorch from [here](https://drive.google.com/file/d/1sPLIQxG0uc8UEIEujukyVZpf8eiYk5EK/view?usp=sharing)

## Step 2: Downlad the sample video 
you can downlaod the from [here](https://drive.google.com/file/d/1a-Wbsd2OOnUGlOV56hai0AEveac784Yo/view?usp=sharing) </br>
or you can downlod the sample image testing dataset from [here](https://drive.google.com/drive/folders/1FOyleSYxoPgUx-mQaj3bG35hKtWjw3XG?usp=sharing)

### Step 3: Clone the repository
use the Git Clone command to clone the repository
```
git clone https://github.com/ReyeTech/CancerDetection
```
### Step 4: Navigate to the directory
```
cd CancerDetection
```
### Step 5: Install the requirements
use the pip install command to install the requirements
```
pip insall -r requirements.txt
```
### Step 6: Run the program
```
python main.py --video lung_cancer.mp4 --model cancer.pt 
```
