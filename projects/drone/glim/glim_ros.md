
glim_ros  -->  
——preprocessor
——odometry_estimation
——time_keeper
——global_mapping
——sub_mapping

创建AsyncSubMapping类的实例，其中sub是SubMapping类的实例
AsyncSubMapping用于异步处理，SubMapping是具体实现，并且是在SubMappingBase类的基础上
参数具体作用于SubMapping中
——sub_mapping.reset(new AsyncSubMapping(sub))