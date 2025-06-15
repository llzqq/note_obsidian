
>过滤近距离和远距离的点。
"distance_near_thresh": 0.5,
"distance_far_thresh": 30.0,

>决定是使用随机网格下采样还是体素网格下采样。
"use_random_grid_downsampling": true,
下采样的分辨率。
"downsample_resolution": 1.0,

>指定随机下采样的目标点数，优先满足target
"random_downsample_target": 10000,
"random_downsample_rate": 0.1,

>是否启用异常值去除
"enable_outlier_removal": false,
用于统计异常值去除的参数，分别表示 K 近邻和标准差倍数。
"outlier_removal_k": 10,
"outlier_std_mul_factor": 1.0,

>考虑每个点的 K 个邻近点
"k_correspondences": 30,

"num_threads": 2