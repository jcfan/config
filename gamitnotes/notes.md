#GAMIT/BLOBK中固定解、浮点解、约束解、松弛解等解类型解释

在GAMIT/GLOBK的使用过程中，经常会碰到固定解、浮点解、约束解、松弛解及其相关组合解（如约束固定解）等词汇，对于初学者，一时难以弄明白其中的含义，一般只有按部就班按照教程中，怎么说就怎么弄，不明白其中为什么这么做。现将其解的类型分别作一些介绍。

1. 固定解（fixed）

   固定解指在基线解算过程中，对整周模糊度固定为整数后，回代到方程解算得到的未知参数解（如基线向量、位置坐标、对流层参数等）。在详细解算结果文件（q文件）中，有如下描述
```
**** Summary of biases-fixed solution ****
```

  该行下面的基线结果即为固定解，也就是结果文件中第二处基线解算结果（一共有两处，第一处为浮点解，后面叙述）  

1.  浮点解（free）

 浮点解指的是，在基线解算过程中，没有对模糊度进行固定为整数，而是直接使用最小二次解算得到的浮点结果，同时得到的未知参数解。在详细解算结果文件（q文件）中，有如下描述
```
**** Summary of biases-free solution ****
```

   该行下面的基线结果即为浮点解，也就是结果文件中第一处基线解算结果。

   总结固定解与浮点解，GAMIT软件生成含有基线的结果文件共有4个，如（oscala.034、oscalp.034、qscala.034、qscalp.034），其中q开头的是详细结果文件，o开头的简要结果文件，其实他们两类的文件内容是一样的，只是详细与概略的差异，另外a结尾的是验后结果，p结尾的是先验结果（这里说明下，因为GAMIT软件默认情况下实际上解算是算了两遍，第一遍的结果作为第二遍的先验值），我们一般用验后的结果，所以要获取基线解算结果，我们选取oscala.034或者qscala.034文件，其中两个文件中第一处的基线解算结果为浮点解（free），第二处基线解算结果为固定解（fixed）。至于什么时候用浮点解什么时候用固定解，这里不作详细解算，可以参考相关文献，但一般情况下采用固定解，即提取结果文件中的第二处基线结果。

3. 约束解（constraints）

   GAMIT软件的主要目的是解算基线，如果只需要使用基线结果，那么只要分清固定解与浮点解就OK了，在继续使用GLOBK软件进行计算点位时就要搞清以下概念。约束解是针对平差来讲的，对观测值进行一定约束，即加入已知点，已知边等已知条件，得到约束条件下的结果。  

4. 松弛解（loose）
  松弛解，即为无约束平差，不对观测值进行约束，而是采用无约束平差（自由网平差）得到解。    
  
  总结约束解和松弛解，GAMIT软件生成的结果文件中要被GLOBK软件处理的是h文件，GLOBK软件时采用卡尔曼滤波解算参数，该软件不对基线进行解算，而是对位置点的点位坐标进行解算。故GAMIT软件生成的h文件中都是点的信息（这个可以自己去查看），其点坐标是GAMIT利用生成的基线数据通过平差得到的坐标，GAMIT中SOLVE模块默认生成的无约束固定解（glx）及无约束浮点解（glr），其中（l=loose x=fiexed r=free），glx与glr文件在使用Globk的htoglb模块才会生成。在h文件中有如下信息表是fixed及free的结果
```
keys: DEFLT FULL  DBLE  LC    NOION NOATM FREE  STN   NOORB ZEN   NOCLK  GLR  NOEOP GRD（其中FREE）
keys: DEFLT FULL  DBLE  LC    NOION NOATM FIXED STN   NOORB ZEN   NOCLK  GLX  NOEOP GRD（其中FIXED）
```

   在GLOBK中一般使用glx或者glr为起算数据，即使用GAMIT的无约束解，这是因为如果GAMIT采用了约束解那么会对GLOBK的解算带来一定的麻烦，所以采用很松的解（点精度大约为10m，卫星大约为100m）然后再使用GLOBK过程中对其进行卡尔曼滤波约束，得到结果最终的结果。

   GLOBK解算过程也分为无约束和约束，结果文件为*.prt(无约束)与*.org文件（约束），无约束是调用globk模块解算得到的结果，约束时调用glorg模块对无约束结果进行旋转平移缩放，纳入约束条件中。在此特别说明，使用GLOBK时可以采用sh_glred命令自动处理，会自动调用htoglb、glred、globk、glorg等模块自动生成*.glx、*.glr、*.prg、*.org文件就重复性图。并且GLOBK默认采用*.glx结果，可以再org与prt文件中看到：
```
 OUTGLOBAL file : H000205_scal.GLX 说明采用了glx文件。
```

   通过上面的解释，解释清了4中基本解类型。

#表说明
下载路径[ftp://garner.ucsd.edu/archive/garner/gamit/tables/](ftp://garner.ucsd.edu/archive/garner/gamit/tables/)
一、表类型说明
1. antmod.dat   天线相位中心参数文件 
2. racvcan.dat   接收机及天线名称对照表 
3. gdetic.dat   各种大地坐标系参数
4. ut1.     地球自转UTC时间修正参数 
5. pole.    极移参数 
6. leap.sec    跳秒参数 
7. soltab.    太阳星历 
8. luntab.    月亮星历 
9. nutabl.    章动参数
10. svs_exclude.dat  需要剔除卫星列表 
11. svnav.dat    卫星星号对照表PRN 与SV的对照 
12. hi.dat    仪器高文件 
13. dcb.dat    差分码表 

二、表更新说明  
1. 每年更新 leap.sec   soltab. luntab. nutabl.    
2. 每月更新  dcb.dat   
3. 每周更新  ut1.  pole.    
4. 有新卫星发射或者卫星调整编号  svnav.dat  antmod.dat    
5. 有卫星出现异常  svs_exclude.dat    
6. 有接收机更新后  racvcan.dat


#Gamit文档笔记
##求解流程
1. 数据下载, 表文件更新.
* 建立工程路径orbdef, 建立路径brdc igs rinex 
```
mkdir orbd
cd orbd
mkdir brdc igs rinex
```
* 下载星历, 精密轨道, 观测文件
```
sh_get_nav -archive cddis -yr 2016 -doy 300 -ndays 3
sh_get_orbits -archive cddis -yr 2016 -doy 302 -ndays 1 -makeg no (只能一天一天下)
sh_get_rinex -archive sopac -yr 2016 -doy 301 -ftp_prog wget  -sd ../tables/sites.defaults -expt orbd
```
* 链接表
```
sh_setup  -yr 2016
```
* 建立doy目录, 链接数据文件,链接表文件.
```
ln -s ../rinex/*3000.16o .
ln -s ../brdc/brdc3000.16n .
ln -s ../igs/igs19203.sp3 . 
links.day 2016 300 orbd
sh_upd_stnfo -files *.16o 
``` 

* 准备L文件
    - IGS apr: gapr_to_l IGS08.apr lfile. ../tables/sites.defaults 2008
    - 通过rinex概略坐标: 
```
grep POSITION *.16o > lfile.rnx
rx2apr lfile.rnx 2016 300
gapr_to_l lfile.rnx.apr lfile. "" 2016 300
cp lfile. ../tables
```
* sh_makexp 为后续的批处理生成相应的配置.
```
sh_makexp -expt orbd -orbt igsf -yr 2016 -doy 300 -sess 99 -srin -nav brdc3000.16n -sinfo 30 00 00 2880
```
生成session.info orbd.makex.batch makexp.out  dorbd6.300 bctot.inp

* 轨道拟合
sh_sp3fit -f igs19203.sp3 -o igsf
生成tmp.stinfo sestbl. trot.out svs_igsf16.300 sp3fit_igsf6300.rms sp3fit_igsf6300.fit ORBFIT.status gigsf6.300

sh_check_sess -sess 300 -type gfile -file gigsf6.300

makej brdc3000.16n   jbrdc6.300          
生成prns jbrdc6.300

sh_check_sess -sess 300 -type jfile -file jbrdc6.300          

makex orbd.makex.batch    
生成x-file k-file orbd.makex.infor 
fixdrv dorbd6.300           OR  run interactively
iorbd6.300 b-files fixdrv.out


* 评估轨道
  - 生成的g文件积分轨道, 修改批处理borbd6.001的输入输出, `arc < borbda.001`, 输出新的T文件tigsfa.300.







###批处理流程
1. arc
用初轨G文件积一组轨道(T文件). G文件是由sh_sp3fit拟合产生的. 
1. yawtab
根据T文件以及arc生成的姿态文件, 生成每个观测时刻卫星的姿态.
1. grdtab
读潮汐格网文件, 大气文件生成U文件.
1. model
对于每个X文件, 计算预拟合残差和偏导数, 生成C文件.
1. autcln
读取model生成的C文件, 做周跳探测. 修复相位数据和预拟合残差生成新的C文件(a结尾).
1. cfmrg 
通过C文件定义求解参数配置M文件.
1. solve
对站坐标和轨道参数进行最小二乘估计. 更新M文件(为后拟合做准备), 生成新的L文件和G文件(a结尾). 生成新的M文件和Q文件(p结尾).
1. model
根据X文件和更新后的坐标文件计算新的残差和偏导数, 生成C文件(b结尾).
1. autcln
读取model生成新的C文件, 做周跳探测. 修复相位数据和预拟合残差生成新的C文件(b结尾).
1. cfmrg
生成新的M文件(b结尾)
1. sh_sigelv
将通过autcln.post.sum得到的数据噪声(权), 以及求解的WL宽巷模糊度写入N文件.
1. solve
对站坐标和轨道参数进行最小二乘估计. 求解模糊度. 覆盖L文件(a结尾), 生成G文件(b结尾). 生成M文件和Q文件(a结尾).

###结果评估

有两个一阶评估准则: 是否有足够的数据量来保证估计的合理; 数据拟合能否达到其噪声的量级.
第一个准则可以通过基线组成的求解数量来判断. 如果结果大大超出所预想的先验估计, 那么查看Q文件或者autcln.sum文件往往会发现大量的数据被autcln踢出掉了. 第二个准则可以查看nrms(平方根 卡方每个自由度). 如果数据随机的分布, 且先验权是正确的, 那么nrms接近于一致(unity). 实际应用中, 默认的权模式是使用临时的相关矩阵, nrms约为0.2是一个好的结果. 如果超过0.5表明有周跳没有修正, 或者是模型有问题. 如果最终结果满足这两个准则, 一般情况下我们不需要再查看其余的输出. autcln.sum.post中记录的单路观测残差表明接收机的相对观测质量.

####Q文件详解
* 基本概况
* autcln修正双差宽巷模糊度的结果
* 对于bias-free的参数估计结果统计(GCR). 
    - 重点要关注postfit nrms.
    - live 参数表示需要估计的参数.
* 参数估计结果. 
    - Formal: 形式误差. 表明绝对解的精度. 主要是根据先验约束.
    - 双差的模糊度接近于整数为正常. 
    - Adjustments larger than 给出了超限(sestbl给的)的接收机. 即Adjustment超过门限.
* 所有测站构成的基线参数.
* solve求解由autcln解出的宽巷模糊度的, 单个卫星接收机的窄巷(L1)模糊度.
* bias-fixed求解结果(GCX).
    - 检验模糊度是否正确求解的方法是 固定解的坐标是否与自由解坐标的不确定性一致.
* 给出了两种解. 分别为biases-free normal equations(GLR)和biases-fix normal equations(GLX).

##数据编辑

一般周跳探测有两种方法: 利用伪距数据组成宽巷观测量, 以及结合宽巷观测双差组合.
###autcln
利用model生成的C文件, 自动剔除异常值, 修复周跳, 周跳添加标志, 生成新的C文件.
```
autcln [command-file] [out C-file series ] [D-file] [input C-file series] 
                                                 or [list of C-files]
```
* command-file: 输入的控制文件, ''表示使用默认.
* out C-file series: 输出的C文件标志. 如果为字母, 输出的C文件第六位就为该字母. 如果为.表示输出的文件与原文件命名相同. 如果+表示输出的C文件名第六位加一([yr]=>a,a=>b). ''表示不输出C文件.
* D-file 为配置文件.
* input C-file series: D文件名第六位改为这个值.




# 修改程序
##bctot.f

gamit/orbit/bctot.f: 第384行, thdrit的输入增加两个'NONE '.

##arcinp.f

gamit/orbit/arcinp.f: 第85行, a20改为a19.
