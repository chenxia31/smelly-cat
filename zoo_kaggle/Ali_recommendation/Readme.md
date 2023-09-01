## 阿里移动推荐算法数据集
> [阿里移动推荐算法数据集2015](https://tianchi.aliyun.com/dataset/46) 

> [阿里移动推荐算法挑战赛](https://tianchi.aliyun.com/competition/entrance/1/information)

> [长期赛事地址](https://tianchi.aliyun.com/competition/entrance/532043/information)

## 赛题介绍
本次采用脱敏后的移动电商平台数据，通过大数据和算法构建面向移动电子商务的商品推荐模型。本文的目标是根据 前三十天对于商品行为 来预测和推荐第31天的商品属性

* U：用户集合
* I：商品集合
* P：商品子集
* D：用户对商品全集的行为数据集合

尝试利用D来构建从D中推荐给U的模型

## 数据描述

提供两个数据集 行为集合**tianchi_mobile_recommend_train_user.zip** 和 商品子集**tianchi_mobile_recommend_train_item.zip**

user_id: 用户标识
item_id: 商品标识
behavior_type: 用户对商品的行为：1 浏览、2 收藏、3 加购物车、4 购买
user_geohash: 用户地理位置标识
item_category: 商品分类标识
time: 行为时间，精确到小时级别

item_id : 商品标识
item_geohashL 商品的空间标识
item_category: 商品分分类标识

## 思路分析
首先从探索性纯数据分析角度：
1. 从用户的角度
    1.1 可以对用户群体行为进行聚类分析，例如：爱浏览用户、爱收藏用户、爱购买用户、不爱购买用户等等
    1.2 