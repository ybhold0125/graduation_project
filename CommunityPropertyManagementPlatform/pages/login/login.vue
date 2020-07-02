<template>
	<view>
		<cu-custom bgColor="bg-gradual-green" :isBack="false" style="height: 1000rpx;">
			<block slot="content">小区物业管理平台</block>
		</cu-custom>
		<view class="cu-bar bg-white  shadow solid-bottom margin-top">
			<view class="action">
				<text class="cuIcon-titles text-red "></text> 小区物业管理平台
			</view>
		</view>
		<view class="padding">
			<view class="padding-xl radius shadow bg-white margin-top">
				<form>
					<view class="cu-form-group">
						<view class="title text-olive cuIcon-people"></view>
						<input id="username" placeholder="Username" type="text" :value="username" @input="inputUsername"></input>
					</view>
					<view class="cu-form-group">
						<view class="title text-olive cuIcon-lock"></view>
						<input type="password" placeholder="*********" :value="userpwd" @input="inputPwd"></input>
					</view>
					<view class="cu-bar bg-white solid-bottom cu-form-group">
						<view class="padding flex flex-direction ybself">
							<button class="cu-btn bg-gradual-green lg" @tap="login">LOGIN</button>
						</view>
					</view>
				</form>
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
			const isUni = typeof(uni) !== 'undefined'
			return {
				username: '',
				userpwd: '',
				pwdType: 'password',
				flag: true
			}
		},
		computed: {
			...mapState(['token', 'globalUserInfo'])
		},
		methods: {
			
			...mapMutations(['setToken', 'setGlobalUserInfo']), 
			
			inputUsername(e) {
				this.username = e.target.value
			},
			inputPwd(e) {
				this.userpwd = e.target.value
			},
			login() {
				if (this.username.length==0){
					uni.showToast({
						title: "请输入用户名",
						icon: 'none'
					})
					return false;
				}
				if (this.userpwd.length==0){
					uni.showToast({
						title: "请输入密码",
						icon: 'none'
					})
					return false;
				}
				var that = this;
				uni.showLoading({
				    title: '登陆中'
				});
				uni.request({
				    url: that.global_baseUrl + '/user_info/',
				    data: {
				        username: this.username,
						password: this.userpwd,
						// username: "admin",
						// password: "admin",
				    },
					method:"POST",
				    header: {
				        'Content-Type': 'application/x-www-form-urlencoded'
				    },
				    success: (res) => {
						this.code = res.data.code;
						that.getToken();
				    }
	
				});
			},
			getToken(){
				var that = this;
				if (that.code === "登录成功"){				
					uni.showToast({
						title: "登录成功!",
						icon: 'success'
					})
					uni.request({
					    url: that.global_baseUrl + '/api/token/',
					    data: {
					        username: that.username,
							password: that.userpwd,
					    },
						method:"POST",
					    header: {
					        'Content-Type': 'application/x-www-form-urlencoded'
					    },
					    success: (res) => {
							that.setToken(res.data.access);
							console.log(that.token);
							uni.setStorageSync('token', res.data.access); //token存在本地
					    }
					});
					setTimeout(() => {
						uni.switchTab({
							url: '/pages/tabbar/tabbar-1/home'
						})
					}, 1000)
				}else if(that.code === "密码错误"){
					uni.showToast({
						title: "密码错误!",
						icon: 'none'
					})
				}else if(that.code === "用户名不存在"){
					uni.showToast({
						title: "用户名不存在!",
						icon: 'none'
					})
				}
			}
		}
	}
</script>
<style>
	.ybself{
		width: 100%;
	}
</style>
 