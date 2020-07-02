<template>
	<view>
		<cu-custom bgColor="bg-gradual-green" :isBack="false" style="height: 1000rpx;">
			<block slot="content">首页</block>
		</cu-custom>
		<uni-notice-bar showIcon="true" scrollable="true" single="true" :text="announcement"></uni-notice-bar>
		<swiper class="card-swiper" :class="dotStyle?'square-dot':'round-dot'" :indicator-dots="true" :circular="true"
		 :autoplay="true" interval="5000" duration="500" @change="cardSwiper" indicator-color="#8799a3"
		 indicator-active-color="#0081ff">
			<swiper-item v-for="(item,index) in swiperList" :key="index" :class="cardCur==index?'cur':''">
				<view class="swiper-item">
					<image :src="item.picture" mode="aspectFill"></image>
					<video :src="item.picture" autoplay loop muted :show-play-btn="false" :controls="false" objectFit="cover" v-if="item.type=='video'"></video>
				</view>
			</swiper-item>
		</swiper>
		<view class="cu-bar bg-white  shadow solid-bottom margin-top">
			<view class="action">
				<text class="cuIcon-titles text-red "></text> 热门新闻
			</view>
		</view>
		<view v-for="(item, index) in newsList" :key="index">
			<view class="cu-card article" :class="isCard?'no-card':''" @click="textClick(item)">
				<view class="cu-item radius shadow bg-white margin-top yb">
					<view class="title"><view class="text-cut">{{ item.news_title }}</view></view>
					<view class="content">
						<view class="desc">
							<view class="text-content">{{ item.news_summary }}</view>
							<view>
								<view class="cu-tag line-green round light">{{ item.news_time }}</view>
								<view class="cu-tag line-red round light">new</view>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import {
			mapState,  
		    mapMutations  
		} from 'vuex'; 
	import uniNoticeBar from '@/components/uni-notice-bar/uni-notice-bar.vue';
	export default {
		components: {uniNoticeBar},
		data() {
			return {
				swiperList: [],
				newsList: [],
				modalName: null,
				announcement: ""
			};
		},
		onLoad(){
			uni.request({
			    url: this.global_baseUrl + '/news/',
			    data: {
					
			    },
			    success: (res) => {
					this.newsList = res.data.slice(0,10);
			    }
			});
			uni.request({
			    url: this.global_baseUrl + '/swipePicture/',
			    data: {
					
			    },
			    success: (res) => {
					// console.log(res.data);
					this.swiperList = res.data;
			    }
			});
			uni.request({
			    url: this.global_baseUrl + '/announcement/',
			    data: {
					
			    },
			    success: (res) => {
					
					this.announcement = res.data[0].announcement_detail;
					console.log(this.announcement);
			    }
			});
			setTimeout(function () {
			    uni.hideLoading();
			}, 1000);
		},
		onShow(){
			var that = this;
			that.checkLocalInfo();
		},
		methods:{
			checkLocalInfo() {
				var that = this;
				if(that.token == null){
					setTimeout(() => {
						uni.showModal({
							title: '提示',
							content: '您还未登录，登录体验更多功能',
							cancelText: '先逛逛',
							confirmText: '去登录',
							success: function(res) {
								if (res.confirm) {
									uni.navigateTo({
										url: '/pages/login/login'
									});
								} else if (res.cancel) {}
							}
						});
					}, 800)
					uni.hideLoading();
				} else {
					uni.hideLoading();
				}
			},
			cardSwiper(e) {
				this.cardCur = e.detail.current
			},
			showModal(e) {
				this.modalName = e.currentTarget.dataset.target
			},
			hideModal(e) {
				this.modalName = null
			},
			textClick(item){
				this.titile = item.news_title;
				this.content = item.news_detail;
				uni.showModal({
				    title: this.titile,
				    content: this.content,
					showCancel: false,
					confirmText: '关闭',
					confirmColor: '#8dc63f',
					
				    success: function (res) {
				        if (res.confirm) {
				        } else if (res.cancel) {
				        }
				    }
				});
			},
		},
		computed: {
			...mapState(['token', 'globalUserInfo'])
		}

	}
</script>

<style>
	.box {
		margin: 20upx 0;
	}
	
	.box view.cu-bar {
		margin-top: 20upx;
	}
	.yb{
		margin-bottom: 0upx;
	}
</style>
