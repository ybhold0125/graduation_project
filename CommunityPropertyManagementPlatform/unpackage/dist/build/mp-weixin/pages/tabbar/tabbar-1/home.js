(global["webpackJsonp"]=global["webpackJsonp"]||[]).push([["pages/tabbar/tabbar-1/home"],{"279b":function(t,n,e){"use strict";e.r(n);var o=e("fe18"),c=e.n(o);for(var i in o)"default"!==i&&function(t){e.d(n,t,function(){return o[t]})}(i);n["default"]=c.a},"54a2":function(t,n,e){"use strict";e.r(n);var o=e("b849"),c=e("279b");for(var i in c)"default"!==i&&function(t){e.d(n,t,function(){return c[t]})}(i);e("73b4");var a,r=e("f0c5"),u=Object(r["a"])(c["default"],o["b"],o["c"],!1,null,null,null,!1,o["a"],a);n["default"]=u.exports},"64da":function(t,n,e){},"73b4":function(t,n,e){"use strict";var o=e("64da"),c=e.n(o);c.a},b849:function(t,n,e){"use strict";var o,c=function(){var t=this,n=t.$createElement;t._self._c},i=[];e.d(n,"b",function(){return c}),e.d(n,"c",function(){return i}),e.d(n,"a",function(){return o})},c1f3:function(t,n,e){"use strict";(function(t){e("73b1"),e("921b");o(e("66fd"));var n=o(e("54a2"));function o(t){return t&&t.__esModule?t:{default:t}}t(n.default)}).call(this,e("543d")["createPage"])},fe18:function(t,n,e){"use strict";(function(t){Object.defineProperty(n,"__esModule",{value:!0}),n.default=void 0;var o=e("2f62");function c(t){for(var n=1;n<arguments.length;n++){var e=null!=arguments[n]?arguments[n]:{},o=Object.keys(e);"function"===typeof Object.getOwnPropertySymbols&&(o=o.concat(Object.getOwnPropertySymbols(e).filter(function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),o.forEach(function(n){i(t,n,e[n])})}return t}function i(t,n,e){return n in t?Object.defineProperty(t,n,{value:e,enumerable:!0,configurable:!0,writable:!0}):t[n]=e,t}var a={onLoad:function(){var n=this;t.request({url:this.global_baseUrl+"/news/",data:{},success:function(t){n.newsList=t.data.slice(0,10)}}),t.request({url:this.global_baseUrl+"/swipePicture/",data:{},success:function(t){n.swiperList=t.data}}),setTimeout(function(){t.hideLoading()},1e3)},onShow:function(){var t=this;t.checkLocalInfo()},methods:{checkLocalInfo:function(){var n=this;null==n.token?(setTimeout(function(){t.showModal({title:"提示",content:"您还未登录，登录体验更多功能",cancelText:"先逛逛",confirmText:"去登录",success:function(n){n.confirm?t.navigateTo({url:"/pages/login/login"}):n.cancel}})},800),t.hideLoading()):t.hideLoading()},cardSwiper:function(t){this.cardCur=t.detail.current},showModal:function(t){this.modalName=t.currentTarget.dataset.target},hideModal:function(t){this.modalName=null},textClick:function(n){this.titile=n.news_title,this.content=n.news_detail,t.showModal({title:this.titile,content:this.content,showCancel:!1,confirmText:"关闭",confirmColor:"#8dc63f",success:function(t){t.confirm||t.cancel}})}},computed:c({},(0,o.mapState)(["token","globalUserInfo"])),data:function(){return{swiperList:[],newsList:[],modalName:null}}};n.default=a}).call(this,e("543d")["default"])}},[["c1f3","common/runtime","common/vendor"]]]);