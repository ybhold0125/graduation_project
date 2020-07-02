<template>
	<view>
		<cu-custom bgColor="bg-gradual-green" :isBack="false" style="height: 1000rpx;">
			<block slot="content">我的</block>
		</cu-custom>
		<view class="personInfoItem bg-gradual-green" >
			<view class="yb">
				<view class="flex  p-xs margin-bottom-sm mb-sm">
					<view class="flex-twice padding-sm margin-xs radius">
						<view class="solids-bottom padding-xs flex align-center">
							<view class="flex-sub text-center">
								<view class="solid-bottom text-xl padding">
									<view v-if="name == ''">
										<text class="text-white text-bold" @tap="logIn">登陆</text>
									</view>
									<view v-if="name !== ''">
										<view v-if="sex==1">
											<text class="text-white text-bold">欢迎你，{{name}}先生</text>
										</view>
										<view v-if="sex==2">
											<text class="text-white text-bold">欢迎你，{{name}}女士</text>
										</view>
									</view>
								</view>
							</view>
						</view>
					</view>
					<view class="flex-sub padding-sm margin-xs radius text-center" @tap="showTip">
						<img class="ybself" src="../../../static/二维码.png" alt="">
					</view>
				</view>
			</view>
		</view>
		<view class="padding">
			<view class="padding-xl radius shadow bg-white margin-top card-menu text-grey">
				<view class="action">
					<text class="cuIcon-titles text-red "></text> 我的提交
				</view>
				<view class="flex text-center margin-top">
					<view class="flex-sub bg-white padding-sm margin-xs radius text-gray ybself1" @click="goToPage('/pages/list/submitlist')">发布</view>
					<view class="flex-sub bg-white padding-sm margin-xs radius text-gray" @click="goToPage('/pages/list/messagelist')">留言</view>
				</view>
			</view>
		</view>
		<view class="cu-list menu sm-border card-menu margin-top">
			<view class="cu-item arrow" @click="goToPage('/pages/log/log')">
				<view class="content"">
					<img src="../../../static/日志.png" class="png" mode="aspectFit">
					<text class="text-grey">日志</text>
				</view>
			</view>
			<view class="cu-item arrow">
				<view class="content">
					<img src="../../../static/赞.png" class="png" mode="aspectFit">
					<text class="text-grey">赞赏支持</text>
				</view>
			</view>
			<view class="cu-item arrow"  @click="goToPage('/pages/tabbar-3-detial/tabbar-3-feedback/tabbar-3-feedback')">
				<view class="content"">
					<img src="../../../static/意见反馈.png" class="png" mode="aspectFit">
					<text class="text-grey">意见反馈</text>
				</view>
			</view>
			<view class="cu-item arrow">
				<view class="content">
					<img src="../../../static/版本信息.png" class="png" mode="aspectFit">
					<text class="text-grey">版本信息</text>
					<text class="text-grey ybself0">v{{ version }}</text>
				</view>
			</view>
		</view>
<!-- 		<view class="padding" v-if="name !== ''">
			<view class="padding-xl radius shadow bg-gradual-green margin-top card-menu text-white text-center text-xl" @click="goToPage('/pages/login/login')">
			退出登录
			</view>
		</view> -->
		<view class="padding flex flex-direction" v-if="name !== ''">
			<button class="cu-btn bg-gradual-green lg" @click="signOut">退出登录</button>
		</view>
	</view>
</template>

<script>
	import {
			mapState,  
		    mapMutations  
		} from 'vuex'; 
	export default {
		data() {
			return {
				name: "",
				sex: 1,
				version: "",
			}
		},
		onLoad() {
			// console.log(this.globalUserInfo)
		},
		onShow() {
			var that = this;
			if(that.token !== null){
				uni.request({
					url: this.global_baseUrl + '/user_info/',
					data: {
						
					},
					header: {
						'Authorization': 'Token  ' + this.token,
					},
					success: (res) => {
						this.name = res.data.name;
						this.sex = res.data.sex;
					}
				});
			}
			uni.request({
				url: this.global_baseUrl + '/appletRelated/',
				data: {
					
				},
				success: (res) => {
					this.version = this.res.data[0].versionNumber;
				}
			});
			
		},
		computed: {
			...mapState(['token', 'globalUserInfo'])
		},
		methods: {
			showTip() {
				uni.showModal({
					 title: '提示',
					 content: '该功能尚未开发',
					 showCancel: false,
				});
			},
			logIn() {
				uni.reLaunch({
					url: '/pages/login/login'
				});
			},
			goToPage(url) {
				if (this.token==null){
					uni.showToast({
						title: "登录才能使用此功能",
						icon: 'none'
					})
					return false;
				}
				if (!url) return;
				uni.navigateTo({
					url
				});
			},
			signOut() {
				uni.reLaunch({
				    url: '/pages/login/login'
				});
			}
		}
	}
</script>

<style>
	.personInfoItem {

		width: 100%;
		height: 200rpx;
		border-radius: 0 0 50rpx 50rpx;
		display: flex;
	}
	.yb{
		width: 100%;
		height: 200rpx;
	}
	.ybself{
		width: 100rpx;
		height: 100rpx;
	}
	.ybself0{
		float: right;
	}
	.ybself1{
		border-right: 1rpx solid #aaaaaa;
	}
</style>