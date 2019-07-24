var page8 = new vue({
    el: "#page8",
    data:{
        image: "./page3_A0_Rectangle_2_pattern.png",
    }
})

var top = new Vue({
    el:"#TOP",
    data:{
        color: "none",
    },
    methods: {
        mouseover: function (){
            this.color = "rgba(0,0,0,0.7)"
        },
        mouseleave: function (){
            this.color = "none"
        }
    },
})

var send = new Vue({
    el: "#SEND",
    data:{
        color:"none",
    },
    methods:{
        mouseover: function (){
            this.color = "rgba(0,0,0,0.7)"
        }
    },
})

var look = new Vue({
    el: "#LOOK",
    data: {
        color: "none",
    },
    methods:{
        mouseover: function (){
            this.color = "rgba(0,0,0,7)"
        },
        mouseleave: function (){
            this.color ="none"
        }
    },
})

var about = new Vue({
    el: "#ABOUT",
    data:{
        color: "none",
    },
    methods:{
        mouseover: function (){
            this.color ="rgba(0,0,0,0.7)"
        },
        mouseleave: function (){
            this.color ="none"
        }
    },
})

var sigh_up =new Vue({
    el: "#SIGH_UP",
    data:{
        color:"none",
    },
    methods:{
        mouseover: function(){
            this.color = "rgba(0,0,0,0.7)"
        },
        mouseleave: function(){
            this.color = "none"
        }
    },
})