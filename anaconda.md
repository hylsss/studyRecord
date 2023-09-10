## anaconda开箱即用python

#### 创建python环境

```ruby
conda create --name 你的环境名称 python=版本号
conda create --name myenv python=3.8
```

#### 激活环境

```ruby
//Windows
conda activate 你的环境名称

//mac && Linux
source activate 你的环境名称
```

#### 在对应环境安装包

```ruby
conda install numpy
```

#### 停用环境

```ruby
conda deactivate
```

### 查看已安装的环境

```ruby
conda env list
或者
conda info --envs
```

#### 删除环境

```ruby
conda env remove --name 你的环境名称
```

#### 查看已经安装的包

```ruby
conda 
```

