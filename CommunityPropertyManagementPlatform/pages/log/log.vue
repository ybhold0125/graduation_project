<template>
	<view>
		<cu-custom bgColor="bg-gradual-green" :isBack="true" style="height: 1000rpx;">
			<block slot="backText">返回</block>
			<block slot="content">日志</block>
		</cu-custom>
		<view class="cu-timeline"  v-for="(item, index) in versionList" :key="index">
			<view class="cu-item">
				<view class="content bg-gradual-green">
					<view class="cu-capsule radius">
						<view class="cu-tag bg-white text-green">v{{ item.versionNumber }}</view>
						<view class="cu-tag line-green text-white">{{ item.updateTime }}</view>
					</view>
					<view class="margin-top">{{ item.updateInformation }}</view>
				</view>
			</view>
<!-- 			<view class="cu-item">
				<view class="content bg-gradual-green">
					<view class="cu-capsule radius">
						<view class="cu-tag bg-white text-green">上午</view>
						<view class="cu-tag line-green text-white">10:00</view>
					</view>
					<view class="margin-top">这是第一次，我家的铲屎官走了这么久。久到足足有三天！！ 在听到他的脚步声响在楼梯间的那一刻，我简直想要破门而出，对着他狠狠地吼上10分钟，然后再看心情要不要他进门。</view>
				</view>
			</view> -->
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				versionList: []
			}
		},
		onLoad() {
			uni.request({
				url: this.global_baseUrl + '/appletRelated/',
				data: {
					
				},
				success: (res) => {
					this.versionList = res.data;
				}
			});
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
