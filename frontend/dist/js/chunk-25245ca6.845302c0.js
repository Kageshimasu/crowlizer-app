(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-25245ca6"],{1768:function(t,e,s){},"36dc":function(t,e,s){"use strict";s.r(e);var r=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"result-form result-flex-container"},[t.failedConnection?t._e():t._t("default",[t.isVisibleTargetAmount?t._e():t._t("default",[s("div",{class:{fadeOut:!t.isVisibleTargetAmount}},[s("transition-group",{staticClass:"result-form result-flex-container",attrs:{name:"fade"},on:{"after-leave":t.switchShowSuccessProb}},[t.showSuccessProb?s("h1",{key:"prob",staticClass:"result-text display-1 mb-3 text-center",staticStyle:{"flex-grow":"3"}},[t._v(" The success probability of your project would be"),s("br"),s("br"),s("font",{staticClass:"display-2 font-weight-bold red-text"},[t._v(" "+t._s((100*this.successProb).toFixed(2))+" ")]),t._v("% ")],1):t._e(),t.indeterminate?s("v-progress-circular",{key:"circular",attrs:{size:70,width:7,color:"#c52b2d",indeterminate:""}}):t._e(),t.showSuccessProb?s("h2",{key:"scroll-text",staticClass:"scroll-down-style mb-3 text-center",staticStyle:{"flex-grow":"3"}}):t._e()],1)],1)]),t.isVisibleTargetAmount?t._t("default",[s("div",{class:{fadeIn:t.isVisibleTargetAmount}},[t.showSuccessProb?s("h1",{key:"prob",staticClass:"result-text display-1 mb-3 text-center"},[t._v(" I think your project would be worth "),s("br"),s("br"),s("font",{staticClass:"display-2 font-weight-bold red-text"},[t._v(" "+t._s(t.targetEst))]),t._v(" yen ")],1):t._e(),t.indeterminate?s("v-progress-circular",{key:"circular",attrs:{size:70,width:7,color:"#c52b2d",indeterminate:""}}):t._e()],1)]):t._e()]),t.failedConnection?t._t("default",[s("div",{staticClass:"flex-center-container"},[s("h1",{staticClass:"result-text display-1 mb-3 text-center"},[t._v(" Sorry :( "),s("br"),s("font",{staticClass:"display-1 font-weight-bold red-text"},[t._v("Failed")]),t._v(" to Connect the server ")],1)])]):t._e()],2)},i=[],a=(s("a9e3"),s("b680"),s("d3b7"),s("d4ec")),n=s("bee2"),o=s("262e"),c=s("2caf"),l=s("9ab4"),u=s("60a3"),d=s("bc3a"),h=s.n(d),b=s("dcfc"),f=function(t){Object(o["a"])(s,t);var e=Object(c["a"])(s);function s(){var t;return Object(a["a"])(this,s),t=e.apply(this,arguments),t.indeterminate=!0,t.showSuccessProb=!1,t.successProb="",t.targetEst="",t.scrollY=0,t.isVisibleTargetAmount=!1,t.enabledWhenUnloadConfirm=!1,t.failedConnection=!1,t}return Object(n["a"])(s,[{key:"switchShowSuccessProb",value:function(){this.showSuccessProb=!0}},{key:"handleScroll",value:function(){window.scrollY>this.scrollY?this.isVisibleTargetAmount=!0:this.isVisibleTargetAmount=!1,this.scrollY=window.scrollY}},{key:"onBeforeunloadHandler",value:function(t){t.returnValue="編集中の内容は失われます。"}},{key:"mounted",value:function(){var t=this;this.startOver(),window.addEventListener("beforeunload",this.onBeforeunloadHandler,!1),window.addEventListener("scroll",this.handleScroll),h.a.put("/crowlizer/api/inference/",this.$store.getters.projectObject).then((function(e){console.log("scceeded"),t.successProb=e.data.predicted_success_prob,t.targetEst=e.data.predicted_target_amount,t.targetEst=Number(t.targetEst)>0?Number(t.targetEst).toFixed(0):"0",t.showSuccessProb=!0})).catch((function(e){console.log("failed"),console.log(e),t.failedConnection=!0})).finally((function(){t.indeterminate=!1}))}},{key:"startOver",value:function(){var t=new b["a"];this.$store.getters.projectObject.equals(t)&&this.$router.push("/")}},{key:"beforeDestroy",value:function(){window.removeEventListener("scroll",this.handleScroll),window.removeEventListener("beforeunload",this.onBeforeunloadHandler,!1)}}]),s}(u["c"]);f=Object(l["a"])([Object(u["a"])({})],f);var v=f,g=v,m=(s("8dd8"),s("2877")),w=s("6544"),y=s.n(w),p=s("490a"),x=Object(m["a"])(g,r,i,!1,null,null,null);e["default"]=x.exports;y()(x,{VProgressCircular:p["a"]})},"490a":function(t,e,s){"use strict";s("99af"),s("a9e3"),s("8d4f");var r=s("a9ad"),i=s("80d2");e["a"]=r["a"].extend({name:"v-progress-circular",props:{button:Boolean,indeterminate:Boolean,rotate:{type:[Number,String],default:0},size:{type:[Number,String],default:32},width:{type:[Number,String],default:4},value:{type:[Number,String],default:0}},data:function(){return{radius:20}},computed:{calculatedSize:function(){return Number(this.size)+(this.button?8:0)},circumference:function(){return 2*Math.PI*this.radius},classes:function(){return{"v-progress-circular--indeterminate":this.indeterminate,"v-progress-circular--button":this.button}},normalizedValue:function(){return this.value<0?0:this.value>100?100:parseFloat(this.value)},strokeDashArray:function(){return Math.round(1e3*this.circumference)/1e3},strokeDashOffset:function(){return(100-this.normalizedValue)/100*this.circumference+"px"},strokeWidth:function(){return Number(this.width)/+this.size*this.viewBoxSize*2},styles:function(){return{height:Object(i["d"])(this.calculatedSize),width:Object(i["d"])(this.calculatedSize)}},svgStyles:function(){return{transform:"rotate(".concat(Number(this.rotate),"deg)")}},viewBoxSize:function(){return this.radius/(1-Number(this.width)/+this.size)}},methods:{genCircle:function(t,e){return this.$createElement("circle",{class:"v-progress-circular__".concat(t),attrs:{fill:"transparent",cx:2*this.viewBoxSize,cy:2*this.viewBoxSize,r:this.radius,"stroke-width":this.strokeWidth,"stroke-dasharray":this.strokeDashArray,"stroke-dashoffset":e}})},genSvg:function(){var t=[this.indeterminate||this.genCircle("underlay",0),this.genCircle("overlay",this.strokeDashOffset)];return this.$createElement("svg",{style:this.svgStyles,attrs:{xmlns:"http://www.w3.org/2000/svg",viewBox:"".concat(this.viewBoxSize," ").concat(this.viewBoxSize," ").concat(2*this.viewBoxSize," ").concat(2*this.viewBoxSize)}},t)},genInfo:function(){return this.$createElement("div",{staticClass:"v-progress-circular__info"},this.$slots.default)}},render:function(t){return t("div",this.setTextColor(this.color,{staticClass:"v-progress-circular",attrs:{role:"progressbar","aria-valuemin":0,"aria-valuemax":100,"aria-valuenow":this.indeterminate?void 0:this.normalizedValue},class:this.classes,style:this.styles,on:this.$listeners}),[this.genSvg(),this.genInfo()])}})},"8d4f":function(t,e,s){},"8dd8":function(t,e,s){"use strict";var r=s("1768"),i=s.n(r);i.a},a9ad:function(t,e,s){"use strict";s("d3b7"),s("ac1f"),s("25f0"),s("466d"),s("1276"),s("498a");var r=s("3835"),i=s("ade3"),a=s("5530"),n=s("2b0e"),o=s("d9bd");function c(t){return!!t&&!!t.match(/^(#|var\(--|(rgb|hsl)a?\()/)}e["a"]=n["a"].extend({name:"colorable",props:{color:String},methods:{setBackgroundColor:function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};return"string"===typeof e.style?(Object(o["b"])("style must be an object",this),e):"string"===typeof e.class?(Object(o["b"])("class must be an object",this),e):(c(t)?e.style=Object(a["a"])(Object(a["a"])({},e.style),{},{"background-color":"".concat(t),"border-color":"".concat(t)}):t&&(e.class=Object(a["a"])(Object(a["a"])({},e.class),{},Object(i["a"])({},t,!0))),e)},setTextColor:function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};if("string"===typeof e.style)return Object(o["b"])("style must be an object",this),e;if("string"===typeof e.class)return Object(o["b"])("class must be an object",this),e;if(c(t))e.style=Object(a["a"])(Object(a["a"])({},e.style),{},{color:"".concat(t),"caret-color":"".concat(t)});else if(t){var s=t.toString().trim().split(" ",2),n=Object(r["a"])(s,2),l=n[0],u=n[1];e.class=Object(a["a"])(Object(a["a"])({},e.class),{},Object(i["a"])({},l+"--text",!0)),u&&(e.class["text--"+u]=!0)}return e}}})}}]);
//# sourceMappingURL=chunk-25245ca6.845302c0.js.map