<template>
    <ul class="col-lg-4 list-group">
        <VideoListItem 
            v-for="video in videos" 
            :key="video.etag"
            :video="video"
            @videoSelect="onVideoSelect"
        >
        </VideoListItem>
    </ul>
        
    <!-- <li v-for="video in videos" :key="video.etag">
        {{ video.snippet.title }}
    </li> -->
</template>

<script>
    import VideoListItem from './VideoListItem';

    export default { 
        name: 'VideoList',
        // props는 data랑 똑같이 쓸 수 있음. data() { return{}} 이렇게 할 필요 없이 그냥 바로 쓰면 됨!
        props: { // props:['videos'] 처럼 배열로 써도 되지만, 객체를 매우 권장 >> validation 검사에 유리
            videos: Array, // 넘어온 data인 videos가 array인지를 확인 (데이터가 손상없이 잘 넘어왔는지 유효성 검사)
        }, // props 쓰기1. props가 넘어온다고 명시한다. 여러개 넘어올 수 있으므로 [] 씀
        /* 절대 이렇게 하면 안됨
        data() {
            return {
                videos: this.videos
            }
        }
        */
        components: {
            VideoListItem,
        },
        methods: {
            onVideoSelect (video) {
                this.$emit('videoSelect', video)
            }
        }
    }
    
    
    
</script>

<style>
    
</style>