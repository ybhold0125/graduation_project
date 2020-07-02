<template>
	<view>
		<cu-custom bgColor="bg-gradual-green" :isBack="true" style="height: 1000rpx;">
			<block slot="backText">返回</block>
			<block slot="content">我的留言</block>
		</cu-custom>
		<view class="cu-bar bg-white  shadow solid-bottom margin-top">
			<view class="action">
				<text class="cuIcon-titles text-red "></text> 留言内容
			</view>
		</view>
		<view v-for="(item, index) in messageList" :key="index">
			<view class="cu-card dynamic" :class="isCard?'no-card':''">
				<view class="cu-item shadow">
					<view class="cu-list menu-avatar">
						<view class="cu-item">
							<view class="cu-avatar round lg">
								<img class="cu-avatar" src="../../static/匿名用户.png" alt="">
							</view>
							<view class="content flex-sub">
								<view>{{ item.messageNickname }}</view>
								<view class="text-gray text-sm flex justify-between">
									{{ item.messageTime.substring(0,19).replace("T"," ") }}
								</view>
							</view>
						</view>
					</view>
					<view class="text-content">
						{{ item.messageContent }}
					</view>
	<!-- 				<view class="text-gray text-sm text-right padding">
						<text class="cuIcon-attentionfill margin-lr-xs"></text> 10
						<text class="cuIcon-appreciatefill margin-lr-xs"></text> 20
						<text class="cuIcon-messagefill margin-lr-xs"></text> 30
					</view> -->
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
				messageList: [],
			}
		},
		onLoad (){
			uni.request({
				url: this.global_baseUrl + '/message_list/',
				data: {
					
				},
				header: {
					'Authorization': 'Token  ' + this.token,
				},
				success: (res) => {
					this.messageList = res.data;
				}
			});
		},
		computed: {
			...mapState(['token', 'globalUserInfo'])
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
