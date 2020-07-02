<template>
	<view>
		<cu-custom bgColor="bg-gradual-green" :isBack="true" style="height: 1000rpx;">
			<block slot="backText">返回</block>
			<block slot="content">我的提交</block>
		</cu-custom>
		<scroll-view scroll-x class="bg-gradual-green nav text-center">
			<view class="cu-item yb" :class="0==TabCur?'text-white cur':''" @tap="tabSelect" data-id="0">
				<text class="cuIcon-repairfill"></text> 维修
			</view>
			<view class="cu-item yb" :class="1==TabCur?'text-white cur':''" @tap="tabSelect" data-id="1">
				<text class="cuIcon-formfill"></text> 反馈
			</view>
		</scroll-view>
		<view v-if="TabCur==0">
			<view v-for="(item, index) in repairList" :key="index">
				<view class="cu-card article" :class="isCard?'no-card':''">
					<view class="cu-item radius shadow bg-white margin-top">
						<view class="title"><view class="text-cut">{{ item.repairTitle }}<view class="cu-tag line-olive round light">联系电话：{{ item.repairPhone }}</view></view></view>
						<view class="content">
							<view class="desc">
								<view class="text-content">{{ item.repairNote }}</view>
								<view>
									<view class="cu-tag line-green round light" v-if="item.repairStatus==0">未处理</view>
									<view class="cu-tag line-green round" v-if="item.repairStatus==1">已处理</view>
									<view class="cu-tag line-red round light">{{ item.repairTime.substring(0,19).replace("T"," ") }}</view>
								</view>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>
		<view v-if="TabCur==1">
			<view v-for="(item, index) in feedbackList" :key="index">
				<view class="cu-card article" :class="isCard?'no-card':''">
					<view class="cu-item radius shadow bg-white margin-top">
						<view class="title"><view class="text-cut">{{ item.feedbackTitle }}</view></view>
						<view class="content">
							<view class="desc">
								<view class="text-content">{{ item.feedbackContent }}({{ item.feedbackContact }})</view>
								<view>
									<view class="cu-tag line-red round light">{{ item.feedbackTime.substring(0,19).replace("T"," ") }}</view>
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
				repairList: [],
				feedbackList: [],
				TabCur: 0,
			}
		},
		onLoad (){
			uni.request({
				url: this.global_baseUrl + '/repairInfo/',
				data: {
					
				},
				header: {
					'Authorization': 'Token  ' + this.token,
				},
				success: (res) => {
					this.repairList = res.data;
				}
			});
			uni.request({
				url: this.global_baseUrl + '/feedbackInfo/',
				data: {
					
				},
				header: {
					'Authorization': 'Token  ' + this.token,
				},
				success: (res) => {
					this.feedbackList = res.data;
				}
			});
		},
		computed: {
			...mapState(['token', 'globalUserInfo'])
		},
		methods: {
			tabSelect(e) {
				this.TabCur = e.currentTarget.dataset.id;
			},
		}
	}
</script>

<style>
	.yb{
		width: 50%;
	}
</style>
