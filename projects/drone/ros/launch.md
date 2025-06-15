```
<launch>
	<node pkg="followbot" type="followbot.py" name="myfollowbotname"/>
	
	<remap from="/old_topic" to="/new_topic" />
	
	<param name="aaa" type="int" value="2" />
	
	</node>
	
</launch>

//param是设置pkg内参数
//arg仅用于设置launch文件
```