<template>
	<view>
		<cu-custom bgColor="bg-gradual-green" :isBack="false" style="height: 1000rpx;">
			<block slot="content">留言板</block>
		</cu-custom>
		<view class="padding">
			<view class="padding-xl radius shadow bg-white margin-top">
				<form>
					<view class="cu-form-group margin-top">
						<textarea maxlength="-1" :disabled="modalName!=null" v-model="sendData.content" placeholder="留言内容(不超过70字)"></textarea>
					</view>
					<view class="cu-form-group">
						<view class="title">昵称</view>
						<input placeholder="昵称(不超过11个字)" name="input" v-model="sendData.nickname" ></input>
					</view>
					<view class="cu-bar bg-white solid-bottom cu-form-group">
						<view class="padding flex flex-direction ybself">
							<button class="cu-btn bg-gradual-green lg" @tap="submit">提交</button>
						</view>
					</view>
				</form>
			</view>
		</view>
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
								<img class="cu-avatar" src="../../../static/匿名用户.png" alt="">
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
				sendData: {
				    content: "",
				    nickname: ""
				},
				messageList: [],
			}
		},
		onLoad() {

		},
		onShow() {
			var that = this;
			that.checkLocalInfo();
			var that = this;
			if(that.token !== null){
				uni.request({
					url: this.global_baseUrl + '/messageBoard/',
					data: {
						
					},
					header: {
						'Authorization': 'Token  ' + this.token,
					},
					success: (res) => {
						this.messageList = res.data;
					}
				});
			}
		},
		computed: {
			...mapState(['token', 'globalUserInfo'])
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
			// inputContent(e) {
			// 	this.content = e.target.value
			// },
			// inputNickname(e) {
			// 	this.nickname = e.target.value
			// },
			submit() {
				if (this.sendData.content.length==0){
					uni.showToast({
						title: "请输入留言内容",
						icon: 'none'
					})
					return false;
				}
				
				if (this.sendData.content.length > 80){
					uni.showToast({
						title: "留言内容不能超过80字",
						icon: 'none'
					})
					return false;
				}
				
				if (this.sendData.nickname.length==0){
					uni.showToast({
						title: "请输入昵称",
						icon: 'none'
					})
					return false;
				}
				if (this.sendData.nickname.length > 11){
					uni.showToast({
						title: "昵称长度不能超过11字",
						icon: 'none'
					})
					return false;
				}
				
				var that = this;
				uni.showLoading({
				    title: '提交中'
				});
				uni.request({
				    url: that.global_baseUrl + '/messageBoard/',
				    data: {
				        content: this.sendData.content,
						nickname: this.sendData.nickname,
				    },
					method:"POST",
				    header: {
				        'Content-Type': 'application/x-www-form-urlencoded',
						'Authorization': 'Token  ' + this.token,
				    },
				    success: (res) => {
						if (res.data == "ok"){
							uni.showToast({
								title: "提交成功!",
								icon: 'success'
							})
							uni.request({
								url: this.global_baseUrl + '/messageBoard/',
								data: {
									
								},
								header: {
									'Authorization': 'Token  ' + this.token,
								},
								success: (res) => {
									this.messageList = res.data;
								}
							});
						}
				    },
				});
				this.sendData.content="";
				this.sendData.nickname="";
			},
		}
	}
</script>

<style>
	.ybself{
		width: 100%;
	}
</style>