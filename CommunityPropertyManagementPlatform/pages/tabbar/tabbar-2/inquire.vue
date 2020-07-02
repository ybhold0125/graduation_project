<template>
	<view>
		<cu-custom bgColor="bg-gradual-green" :isBack="false" style="height: 1000rpx;">
			<block slot="content">查询</block>
		</cu-custom>
		<view class="cu-bar bg-white margin-top solid-bottom">
			<view class="action">
				<text class="cuIcon-title text-orange"></text> 费用查询
			</view>
		</view>
		<scroll-view scroll-x class="bg-gradual-green nav text-center">
			<view class="cu-item" :class="0==TabCur?'text-white cur':''" @tap="tabSelect" data-id="0">
				<text class="cuIcon-moneybagfill"></text> 水费
			</view>
			<view class="cu-item" :class="1==TabCur?'text-white cur':''" @tap="tabSelect" data-id="1">
				<text class="cuIcon-lightfill"></text> 电费
			</view>
			<view class="cu-item" :class="2==TabCur?'text-white cur':''" @tap="tabSelect" data-id="2">
				<text class="cuIcon-hotfill"></text> 燃气费
			</view>
			<view class="cu-item" :class="3==TabCur?'text-white cur':''" @tap="tabSelect" data-id="3">
				<text class="cuIcon-homefill"></text> 物业管理费
			</view>
		</scroll-view>
		<view v-if="TabCur==0">
			<view v-for="(item, index) in costList" :key="index">
				<view class="cu-card article" :class="isCard?'no-card':''" v-if="item.type==0">
					<view class="cu-item radius shadow bg-white margin-top">
						<view class="title"><view class="text-cut">{{ item.costTitle }}</view></view>
						<view class="content">
							<view class="desc">
								<view class="text-content">{{ item.amount }}</view>
								<view>
									<view class="cu-tag line-green round light" v-if="item.costStatus==0">待缴纳</view>
									<view class="cu-tag line-green round" v-if="item.costStatus==1">已缴纳</view>
									<view class="cu-tag line-red round light">{{ item.startTime }}</view>
								</view>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>
		<view v-if="TabCur==1">
			<view v-for="(item, index) in costList" :key="index">
				<view class="cu-card article" :class="isCard?'no-card':''" v-if="item.type==1">
					<view class="cu-item radius shadow bg-white margin-top">
						<view class="title"><view class="text-cut">{{ item.costTitle }}</view></view>
						<view class="content">
							<view class="desc">
								<view class="text-content">{{ item.amount }}</view>
								<view>
									<view class="cu-tag line-green round light" v-if="item.costStatus==0">待缴纳</view>
									<view class="cu-tag line-green round light" v-if="item.costStatus==1">已缴纳</view>
									<view class="cu-tag line-red round light">{{ item.startTime }}</view>
								</view>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>
		<view v-if="TabCur==2">
			<view v-for="(item, index) in costList" :key="index">
				<view class="cu-card article" :class="isCard?'no-card':''" v-if="item.type==2">
					<view class="cu-item radius shadow bg-white margin-top">
						<view class="title"><view class="text-cut">{{ item.costTitle }}</view></view>
						<view class="content">
							<view class="desc">
								<view class="text-content">{{ item.amount }}</view>
								<view>
									<view class="cu-tag line-green round light" v-if="item.costStatus==0">待缴纳</view>
									<view class="cu-tag line-red round light" v-if="item.costStatus==1">已缴纳</view>
									<view class="cu-tag bg-red light sm round">{{ item.startTime }}</view>
								</view>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>
		<view v-if="TabCur==3">
			<view v-for="(item, index) in costList" :key="index">
				<view class="cu-card article" :class="isCard?'no-card':''" v-if="item.type==3">
					<view class="cu-item radius shadow bg-white margin-top">
						<view class="title"><view class="text-cut">{{ item.costTitle }}</view></view>
						<view class="content">
							<view class="desc">
								<view class="text-content">{{ item.amount }}</view>
								<view>
									<view class="cu-tag line-green round light" v-if="item.costStatus==0">待缴纳</view>
									<view class="cu-tag line-red round light" v-if="item.costStatus==1">已缴纳</view>
									<view class="cu-tag line-red round light">到期时间：{{ item.endTime }}</view>
								</view>
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
		
	export default {
		data() {
			return {
				costList: [],
				TabCur: 0,
			}
		},
		computed: {
			...mapState(['token', 'globalUserInfo'])
		},
		onLoad() {
			// uni.request({
			//     url: this.global_baseUrl + '/costInfo/',
			//     data: {
					
			//     },
			//     header: {
			// 		'Authorization': 'Token  ' + this.token,
			//     },
			//     success: (res) => {
			// 		console.log(res.data);
			// 		this.costList = res.data;
			//     }
			// });
			// setTimeout(function () {
			//     uni.hideLoading();
			// }, 1000);
		},
		onShow(){
			var that = this;
			that.checkLocalInfo();
			var that = this;
			if(that.token !== null){
				uni.request({
					url: this.global_baseUrl + '/costInfo/',
					data: {
						
					},
					header: {
						'Authorization': 'Token  ' + this.token,
					},
					success: (res) => {
						this.costList = res.data;
					}
				});
			}
			setTimeout(function () {
			    uni.hideLoading();
			}, 1000);
		},
		methods: {
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
			tabSelect(e) {
				this.TabCur = e.currentTarget.dataset.id;
			},
		}
	}
</script>

<style>
	
</style>
