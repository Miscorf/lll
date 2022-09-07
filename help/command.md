## 连接GPU节点

```bash
// 连接服务器后 
ssh node0X
// X = 01,02 or 03
```

## 常用命令

### 启动conda环境

```bash
conda activate 环境名
```

### 创建conda环境

```bash
conda create -n envname python=3.6
```

```

```

### 查看显卡占用情况：

```bash
// 查看显卡占用情况
// 需要进入node0X节点
nvidia-smi
// 周期性输出显卡占用情况：
watch -n 0.5 nvidia-smi

```

### module使用

```bash
module load
// 加载软件环境
// 示例：module load anaconda/2.7
// 将anaconda/2.7加载到环境中。

 module list
// 显示用户已加载的编译器及库

 module unload
// 卸载软件环境
//示例：module unload anaconda/2.7
// 将anaconda/2.7从用户环境中卸载。

```

### 查看内存占用情况

 top


free
