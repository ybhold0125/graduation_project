<template>
	<view class="page">
		<cu-custom bgColor="bg-gradual-green" :isBack="true" style="height: 1000rpx;">
			<block slot="backText">返回</block>
			<block slot="content">问题反馈</block>
		</cu-custom>
		<view class='feedback-title'>
			    <text>问题(不超过20字)</text>
			    <text class="feedback-quick" @tap="chooseMsg">快速键入</text>
			</view>
			<view class="feedback-body">
			    <textarea placeholder="请简述描述你的问题..." v-model="sendData.title" class="feedback-textare" />
			</view>
			<view class='feedback-title'>
			    <text>意见(不超过200字)</text>
			</view>
			<view class="feedback-body yb">
			    <textarea placeholder="请详细描述您的意见..." v-model="sendData.content" class="feedback-textare" />
			</view>
			<view class='feedback-title'>
			    <text>QQ/邮箱</text>
			</view>
			<view class="feedback-body">
			    <input class="feedback-input" v-model="sendData.contact" placeholder="(选填,方便我们联系你 )" />
			</view>
			<button class="feedback-submit bg-gradual-green" @tap="send">提交</button>
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
                msgTitles: ["小区公共设施毁坏无人维修", "小区卫生环境无人打扫", "小区保安服务态度极差", "平台界面显示错乱", "平台偶发性崩溃"],
                imageList: [],
                sendData: {
                    score: 0,
					title: "",
                    content: "",
                    contact: ""
                }
            }
        },
        onLoad() {
            let deviceInfo = {
                appid: plus.runtime.appid,
                imei: plus.device.imei, //设备标识
                p: plus.os.name === "Android" ? "a" : "i", //平台类型，i表示iOS平台，a表示Android平台。
                md: plus.device.model, //设备型号
                app_version: plus.runtime.version,
                plus_version: plus.runtime.innerVersion, //基座版本号
                os: plus.os.version,
                net: "" + plus.networkinfo.getCurrentType()
            }
            this.sendData = Object.assign(deviceInfo, this.sendData);
        },
		computed: {
			...mapState(['token', 'globalUserInfo'])
		},
        methods: {
            chooseMsg() { //快速输入
                uni.showActionSheet({
                    itemList: this.msgTitles,
                    success: (res) => {
                        this.sendData.title = this.msgTitles[res.tapIndex];
                    }
                })
            },
            send() { //发送反馈
				var that = this;
				if (this.sendData.title.length==0){
					uni.showToast({
						title: "请输入问题",
						icon: 'none'
					})
					return false;
				}
				if (this.sendData.content.length==0){
					uni.showToast({
						title: "请输入意见",
						icon: 'none'
					})
					return false;
				}
					
				uni.request({
					url: that.global_baseUrl + '/feedbackInfo/',
					data: {
						title: this.sendData.title,
						content: this.sendData.content,
						contact: this.sendData.contact,
					},
					method:"POST",
					header: {
						'Content-Type': 'application/x-www-form-urlencoded',
						'Authorization': 'Token  ' + this.token,
					},
					success: (res) => {
						if (res.data == "ok"){
							uni.showToast({
								title: "反馈成功!",
								icon: 'success'
							})
							setTimeout(() => {
								uni.switchTab({
									url: '/pages/tabbar/tabbar-1/home'
								})
							}, 1000)
						}
						setTimeout(function () {
							uni.hideLoading();
						}, 1000);
					}
				});
            }
        }
    }
</script>

<style>
    @font-face {
    	font-family: uniicons;
    	font-weight: normal;
    	font-style: normal;
    }
    page {
        background-color: #EFEFF4;
    }
    view{
        font-size: 28upx;
    }
 
    /*问题反馈*/
    .feedback-title {
    	display: flex;
    	flex-direction: row;
    	justify-content: space-between;
    	align-items: center;
    	padding: 20upx;
    	color: #8f8f94;
    	font-size: 28upx;
    }
    .feedback-star-view.feedback-title {
    	justify-content: flex-start;
    	margin: 0;
    }
    .feedback-quick {
    	position: relative;
    	padding-right: 40upx;
    }
    .feedback-quick:after {
    	font-family: uniicons;
    	font-size: 40upx;
    	content: '\e581';
    	position: absolute;
    	right: 0;
    	top: 50%;
    	color: #bbb;
    	-webkit-transform: translateY(-50%);
    	transform: translateY(-50%);
    }
	.yb{
		height: 400upx;
	}
    .feedback-body {
    	background: #fff;
    }
    .feedback-textare {
    	height: 200upx;
    	font-size: 34upx;
    	line-height: 50upx;
    	width: 100%;
    	box-sizing: border-box;
    	padding: 20upx 30upx 0;
    }
    .feedback-input {
    	font-size: 34upx;
    	height: 80upx;
    	min-height: 50upx;
    	padding: 15upx 20upx;
    	line-height: 50upx;
    }
    .feedback-uploader {
    	padding: 22upx 20upx;
    }
    .feedback-star {
    	font-family: uniicons;
    	font-size: 40upx;
    	margin-left: 6upx;
    }
    .feedback-star-view {
    	margin-left: 20upx;
    }
    .feedback-star:after {
    	content: '\e408';
    }
    .feedback-star.active {
    	color: #FFB400;
    }
    .feedback-star.active:after {
    	content: '\e438';
    }
    .feedback-submit {
/*    	background: #007AFF; */
    	color: #FFFFFF;
    	margin: 20upx;
    }
</style>
