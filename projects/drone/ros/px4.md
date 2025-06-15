#### 话题查看
```
4_Firmware/build/px4_sitl_default/bin
./px

in PX4-uorb top
```

#### sitl在环仿真
program <----> mavros <----> px4 sitl(drone)

Gazebo SITL:
包含 PX4 SITL 与 Gazebo 

PX4 直接使用Gazebo API与Gazebo交互

#### px4内pwm计算
**(位置控制->)速度控制->姿态控制->角速度控制->电机输出**

位置控制/速度控制:
modules/mc_pos_control  发布vehicle_attitude_setpoint

姿态控制:
modules/mc_att_control  发布vehicle_rates_setpoint

角速度控制:
modules/mc_rate_control   发布 actuator_controls_0 力和力矩

pwm控制:
第一步：整体力和力矩的控制信号
actuator_controls_0
                Control Group #0 (Flight Control)
                •	0: roll (-1..1)
                •	1: pitch (-1..1)
                •	2: yaw (-1..1)
                •	3: throttle (0..1 normal range, -1..1 for variable pitch / thrust reversers)
                •	4: flaps (-1..1)
                •	5: spoilers (-1..1)
                •	6: airbrakes (-1..1)
                •	7: landing gear (-1..1)

第二步：混控器输出各电机的pwm
混控器启动（飞控里）：混控器的启动是在启动脚本rcS的运行下一步步加载的。
        大概的加载顺序是rcS->rc.autostart->4001_quad_x->rc.mc_defaults

#### 文件理解
*drivers里的是被执行的进程
lib里的是类和函数的定义*


- modules/mc_rate_control/MulticopterRateControl.cpp
接收vel_cmd
转化为无人机的期望角速率 -->_rates_sp(0)：期望的滚转角速率（绕X轴旋转的速度）
                        _rates_sp(1)：期望的俯仰角速率（绕Y轴旋转的速度）
                        _rates_sp(2)：期望的偏航角速率（绕Z轴旋转的速度）
输出期望力矩和推力
力矩控制方向，推力控制具体速率-->actuator_controls_s::INDEX_ROLL
                            actuator_controls_s::INDEX_PITCH
                            actuator_controls_s::INDEX_YAW
                            actuator_controls_s::INDEX_THROTTLE

<pr></pr>

- src/lib/mixer/MultirotorMixer/geometries/tools/px_generate_mixers.py
自动根据构型配置文件生成头文件
rotor位置       src/lib/mixer/MultirotorMixer/geometries/quad_x.toml

<pr></pr>
- src/lib/mixer
定义了混控的逻辑，函数定义

<pr></pr>
- src/lib/mixer_module
为上层应用调用mixer做好各种方便的函数接口
MixingOutput()
update()

<pr></pr>
- src/drivers/pwm_out
mixing_output.update()