# AICUP-2024-competition
AICUP 2024 Cross-camera Multiple-object tracking

## Team 5093: 林垣志, Luu Van Tin, Ngo Duc Thang, Nguyen Quang Sang 
- [**AI 驅動出行未來：跨相機多目標車輛追蹤競賽 － 模型組**](https://tbrain.trendmicro.com.tw/Competitions/Details/33)  
  
<a href="https://tbrain.trendmicro.com.tw/Competitions/Details/33"><img src="https://i.imgur.com/3nfLbdW.png" title="source: imgur.com" /></a>  
> 鑒於居家安全、犯罪偵防等需求，近年來攝影機系統在道路上被廣泛的運用。由於目前一般的監視系統都是基於單相機錄影，每個攝影機是獨立運作，所以當移動物件離開拍攝範圍後，就無法繼續辨識。其次，當發生車禍碰撞、犯罪事件，由於每台相機單獨錄影，相機間沒有協同作業的機制，
> 因此警政單位必須花費龐大的人力資源，由人工搜尋監視系統錄製的影片，才能追蹤可疑車輛或行人的路徑與軌跡。本競賽著眼於跨相機多目標追蹤的技術以解決上述的問題。競賽資料集提供跨相機的道路車輛行駛影片，讓參賽團隊發展跨相機多目標追蹤的AI模型，
> 目標要能夠偵測與辨識出在不同相機的相同車輛，期望能深化台灣在智慧交通的AI技術深化與多元發展。 

<a href="https://drive.google.com/file/d/1VLShkCYHkK3wPXu97iid_D3epXNhmRP8/view?usp=sharing" target="_blank">
  <img src="https://img.shields.io/badge/Supplementary-Paper-blue" alt="Paper">
</a>

<a href="https://drive.google.com/file/d/1kPULVZGvUKC-0ohew0K2pYOyIksacUXv/view?usp=sharing" target="_blank">
  <img src="https://img.shields.io/badge/Supplementary-CompetitionReport-blue" alt="CompetitionReport">
</a>

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

<br>

### Pipeline of our tracking method
![image](https://github.com/Louislin0128/AICUP-2024-competition/blob/main/photo/architecture.png)

<br>

## Demo Results
### Here are some tracking results.

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
