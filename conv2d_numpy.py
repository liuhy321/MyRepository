import numpy as np


def conv2d_numpy(input_data, kernel, stride=1, padding=0):
  # 获取输入数据的尺寸
  input_height, input_width, input_channels = input_data.shape
  # 获取卷积核的尺寸
  kernel_height, kernel_height, kernel_channels = kernel.shape
  # 计算输出图像的尺寸
  output_height = (input_height - kernel_height + 2 * padding) // stride + 1
  output_width = (input_width - kernel_width + 2 * padding) // stride + 1
  
  # 初始化输出图像
  output_data = np.zeros((out_height, output_width))
  
  # 填充输入数据(根据填充数量添加额外的行和列)
  if padding > 0:
    input_data = np.pad(input_data, pad_width=((padding, padding), (padding, padding), (0, 0)), mode="constant")
    
  # 执行卷积操作
  for i in range(0, input_height - kernel_height + 1, stride):
    for j in range(0, input_width - kernel_width + 1, stride):
      for k in range(kernel_channels):
        output_data[i // stride, j // stride] += np.sum(
          input_data[i: i + kernel_height, j: j + kernel_width, k] * kernel[:, :, k]
        )
  
  return output_data


if __name__ == '__main__':
  # 创建一个示例的多通道二维图像数据(400x400像素，3个通道)
  image = np.random.rand(400, 400, 3).astype(np.float32)
  
  # 定义一个卷积核(滤波器)
  conv_kernel = np.random.rand(2, 2, 3).astype(np.float32)
  
  # 执行自定义的的卷积操作
  result = conv2d_numpy(image, conv_kernel, stride=1, padding=0)
  
  # 打印卷积结果
  print(result)
