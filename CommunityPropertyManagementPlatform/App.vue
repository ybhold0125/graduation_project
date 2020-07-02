<script>
import Vue from 'vue'
export default {
	onLaunch: function() {
		uni.getSystemInfo({
		    success: function(e) {
		        // #ifndef MP
		        Vue.prototype.StatusBar = e.statusBarHeight;
		        if (e.platform == 'android') {
		            Vue.prototype.CustomBar = e.statusBarHeight + 50;
		        } else {
		            Vue.prototype.CustomBar = e.statusBarHeight + 45;
		        };
		        // #endif
		        // #ifdef MP-WEIXIN
		        Vue.prototype.StatusBar = e.statusBarHeight;
		        let custom = wx.getMenuButtonBoundingClientRect();
		        Vue.prototype.Custom = custom;
		        Vue.prototype.CustomBar = custom.bottom + custom.top - e.statusBarHeight;
		        // #endif       
		        // #ifdef MP-ALIPAY
		        Vue.prototype.StatusBar = e.statusBarHeight;
		        Vue.prototype.CustomBar = e.statusBarHeight + e.titleBarHeight;
		        // #endif
		    }
		})
		// setTimeout(() => {
		// 	uni.setTabBarBadge({
		// 		index: 1,
		// 		text: '31'
		// 	});
		// 	uni.showTabBarRedDot({
		// 		index: 3
		// 	});
		// }, 1000);
	},
	onShow: function() {
		console.log('App Show');
	},
	onHide: function() {
		console.log('App Hide');
	}
};
</script>

<style>
	@import "colorui/main.css";
	@import "colorui/icon.css";
</style>
