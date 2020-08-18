# 粒子群最佳化演算法(Particle Swarm Optimization，PSO)
    一種群體智慧演算法，作者從觀察鳥群覓食的行為獲得啟發。鳥群在一空間搜索食物時，會結合自身與其他同伴的
    最佳經驗判斷該去哪邊才能找到最多食物，漸漸的整個鳥群會朝最多食物的方向飛去。
## 目標
![image](https://github.com/leodflag/PSO/blob/master/question.png)
## 條件限制
![image](https://github.com/leodflag/PSO/blob/master/condition.png)
## 虛擬碼
	1.產生N個粒子的各自亂數初始位置以及初始速度
	2.設定適應函數
	3.計算適應值，並將第一代群體和個體最佳先存起來
	4.計算適應值
	5.群體最佳值更新
	6.個體最佳值更新
	7.速度更新與調整
	8.位置更新與調整
	9.印出群體最佳值
	10.重複4-9  迭代itera次
## 公式
### 數學符號
![image](https://github.com/leodflag/PSO/blob/master/math_symbol.png)
### 速度更新公式
![image](https://github.com/leodflag/PSO/blob/master/speed_update_formula.png)
### 位置更新公式
![image](https://github.com/leodflag/PSO/blob/master/location_update_formula.png)
## PSO參數的設置
	adapt_fun(x,v,N)：適應函數，x為位置，v為速度，N為粒子數
	N：粒子數，10~20個
	c0 、c1：常數，設2.0
	Vmax：最大速度，以粒子範圍為大小，設200
	w ：慣性權重，採線性遞減的慣性權重，從0.9線性遞減到0.4
	itera：150
## 結果
![image](https://github.com/leodflag/PSO/blob/master/PSO_result.png)

迭代次數與群體最佳值關係曲線圖<br/>
x軸為迭代次數、y軸為群體最佳值
