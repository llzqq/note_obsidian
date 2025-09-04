```cpp
#include <opencv2/opencv.hpp>
using namespace cv;
```

### **形态学处理**

**膨胀（Dilation）**

膨胀操作通过将图像中的每个像素与其邻域内的像素进行比较，将邻域内的**最大值**赋给当前像素，从而使图像的边缘向外扩展。

- **连接断开的部分**：膨胀操作可以使图像中的断开部分连接起来。
    
- **扩大物体的边界**：膨胀操作可以使图像中的物体边界向外扩展。
    
- **填充小孔**：膨胀操作可以帮助填充图像中的小孔。

**腐蚀（Erosion）**

腐蚀操作通过将图像中的每个像素与其邻域内的像素进行比较，将邻域内的**最小值**赋给当前像素，从而使图像的边缘向内收缩。

- **分离粘连的部分**：腐蚀操作可以使图像中粘连的部分分离。
    
- **缩小物体的边界**：腐蚀操作可以使图像中的物体边界向内收缩。
    
- **去除小的噪声点**：腐蚀操作可以帮助去除图像中的小的噪声点。


```cpp

Mat kernel_dilated = getStructuringElement(MORPH_RECT, Size(2, 2));

Mat eroded_image;

erode(binary_image, eroded_image, kernel_eroded); //腐蚀
```
```cpp
// 膨胀操作
    Mat dilated_image;
    dilate(image, dilated_image, kernel);
```


### **读取，显示，保存图像**

使用 `cv::imread` 函数读取图像文件。

```cpp

    // 读取图像
    Mat image = imread("path/to/image.jpg", IMREAD_COLOR);

    // 检查图像是否成功加载
    if (image.empty()) {
        std::cerr << "Error: Could not open or find the image." << std::endl;
        return -1;
    }

	// 读取某个点的值
	uchar pixelValue = binaryImage.at<uchar>(y, x);

	static_cast<int>(pixelValue)


```

使用 `cv::imshow` 函数显示图像。

```cpp

    // 显示图像
    namedWindow("Image", WINDOW_NORMAL); // 创建窗口
    imshow("Image", image); // 显示图像
    waitKey(0); // 等待用户按键

}
```

使用 `cv::imwrite` 函数保存图像。

```cpp
    // 保存图像
    imwrite("path/to/output_image.jpg", image);

}
```


### **图像转换**

将彩色图像转换为灰度图像。
```cpp

    // 转换为灰度图像
    Mat gray_image;
    cvtColor(image, gray_image, COLOR_BGR2GRAY);

```
转化为二值图像

```cpp
// 创建二值图像

Mat binary_image;

// 使用固定阈值进行阈值化

threshold(_image, binary_image, 120, 255, THRESH_BINARY); //小于等于120被转化为黑色，大于为白色
```
### **图像裁剪，缩放，旋转**

裁剪图像的特定区域。

```cpp
    // 裁剪图像
    Rect roi(100, 100, 300, 300); // 定义裁剪区域 （起始x， 起始y， 宽度， 高度）
    
    Mat cropped_image = image(roi);
```

调整图像的大小。
```cpp
    // 缩放图像
    Mat resized_image;
    resize(image, resized_image, Size(), 0.5, 0.5, INTER_LINEAR); // 缩小到原来的一半
```
旋转图像。

```cpp

    // 旋转图像
    Mat rotated_image;
    Point2f center(image.cols / 2.0, image.rows / 2.0); // 旋转中心
    Mat rotation_matrix = getRotationMatrix2D(center, 45, 1.0); // 旋转矩阵
    warpAffine(image, rotated_image, rotation_matrix, image.size()); // 应用旋转

}
```

### **图像滤波**

应用滤波操作，如高斯模糊。

```cpp
    // 应用高斯模糊
    Mat blurred_image;
    GaussianBlur(image, blurred_image, Size(15, 15), 0);
}
```

### **边缘，轮廓检测**


- **使用Canny边缘检测算法。**

```cpp

    // 应用Canny边缘检测
    Mat edges;
    Canny(image, edges, 100, 200);

}
```

1. **`threshold1`**：这是用于识别弱边缘的阈值。如果像素梯度值高于 `threshold1`，则该像素被认为是边缘的一部分。
    
2. **`threshold2`**：这是用于识别强边缘的阈值。只有当像素梯度值高于 `threshold2` 时，该像素才被确定为强边缘。

- **降低 `threshold1`**：可以检测到更多的边缘，但可能会增加噪声。
    
- **提高 `threshold2`**：会减少检测到的边缘数量，但边缘的质量可能会更高。

- **检测图像中的轮廓。**

```cpp
    // 应用Canny边缘检测
    Mat edges;
    Canny(image, edges, 100, 200);

    // 查找轮廓
    std::vector<std::vector<Point>> contours;
    findContours(edges, contours, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);

    // 绘制轮廓
    Mat contour_image = Mat::zeros(edges.size(), CV_8UC3);
    cvtColor(edges, contour_image, COLOR_GRAY2BGR);
    drawContours(contour_image, contours, -1, Scalar(0, 255, 0), 2);

}
```


