    num_threads：用于优化的线程数。
    max_correspondence_distance：最大对应点距离。
    ivox_resolution：iVox体素分辨率。
    location_consistency_inf_scale 和 constant_velocity_inf_scale：位置一致性和恒定速度的约束精度。
    lm_max_iterations：Levenberg-Marquardt优化的最大迭代次数。
    smoother_lag：平滑器的滞后时间。



"so_name": "libodometry_estimation_ct.so",

// ivox params
>iVox体素分辨率。
"ivox_resolution": 2.0,

>定义了iVox中体素内点的最小距离
"ivox_min_points_dist": 0.1,

>决定了体素被删除的频率和数量
"ivox_lru_thresh": 200,

// CT-GICP params
>最大对应点距离
"max_correspondence_distance": 14.0,

>约束精度
"location_consistency_inf_scale": 1e-3,
"constant_velocity_inf_scale": 1e-3,

>优化的最大迭代次数
"lm_max_iterations": 8,

// smoother params
>基于当前时间点前x秒内的所有数据来优化当前状态。
"smoother_lag": 0.8,

"use_isam2_dogleg": false,

>指定在多少次调用 `ISAM2::update()` 后进行重线性化操作
"isam2_relinearize_skip": 1,

>指定变量的线性变化量超过该阈值时，才会进行重线性化
"isam2_relinearize_thresh": 0.1,

// Misc
>用于优化的线程数。
"num_threads": 4
