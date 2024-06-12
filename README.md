# AICUP-2024-competition
AICUP 2024 Cross-camera Multiple-object tracking

## Team 5093: 林垣志, Luu Van Tin, Ngo Duc Thang, Nguyen Quang Sang 
- [**AI 驅動出行未來：跨相機多目標車輛追蹤競賽 － 模型組**](https://tbrain.trendmicro.com.tw/Competitions/Details/33)  
  
<a href="https://tbrain.trendmicro.com.tw/Competitions/Details/33"><img src="https://i.imgur.com/3nfLbdW.png" title="source: imgur.com" /></a>  
> In recent years, surveillance camera systems have been widely used on roads due to the demands for
home security and crime prevention. Since most surveillance systems are currently based on singlecamera recording, each camera operates independently, making it impossible to continue identifying
moving objects once they leave the field of view. Additionally, in the event of accidents or criminal
incidents, because each camera records independently and there is no mechanism for cooperative
operation between cameras, law enforcement agencies must expend significant manpower resources to
manually search through surveillance recordings to track the paths and trajectories of suspicious vehicles
or pedestrians. 

<a href="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Louislin0128%2FAICUP-2024-competition&label=visitors&countColor=%232ccce4&style=plastic" target="_blank">
  <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Louislin0128%2FAICUP-2024-competition&label=visitors&countColor=%232ccce4&style=plastic" alt="Visitors">
</a>

<a href="https://img.shields.io/github/downloads/Louislin0128/AICUP-2024-competition/total" target="_blank">
  <img src="https://img.shields.io/github/downloads/Louislin0128/AICUP-2024-competition/total" alt="Download">
</a>


### This work earn the 6th place among 286 teams
<details>
  <summary><b>LeaderBoard </b></summary>
  
  ![image](https://github.com/Louislin0128/AICUP-2024-competition/blob/main/photo/lb.png)
</details>


### Pipeline of our tracking method
![image](https://github.com/Louislin0128/AICUP-2024-competition/blob/main/photo/architecture.png)


## Demo Results
### Here are some tracking results.

<br>
<details>
  <summary><b>Example demo </b></summary>
  #TODO

</br>
</details>

### Install
This implementation uses Python 3.8, [Pytorch](http://pytorch.org/),  Cuda 11.3. 
```shell
# Copy/Paste the snippet in a terminal
git clone https://github.com/tinery/AICUP-2024-competition.git
cd Density-Imbalance-Eased

#Dependencies
conda create -n atlasnet python=3.8 --yes
conda activate Tracker
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
pip install --user --requirement  requirements.txt # pip dependencies
```

### Usage

Demo :    ```./run_submit.sh``` <br>
