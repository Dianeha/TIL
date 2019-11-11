<template>
    <li @click="onVideoClick" class="list-group-item">
        <img :src="thumbnailUrl" class="mr-3" :alt="video.snippet.title"> 
        <!-- v-bind를 걸어야지만 vue가 읽을 수 있다. 
        :alt="video.snippet.title" 하지 않고 
        alt="video.snippet.title"하면 string이 뜸  -->
        <div class="media-body">
            <span v-html="video.snippet.title"></span>
        </div>        
    </li>
</template>

<script>
export default {
    name: 'VideoListItem',
    props: {
        video: Object, // 넘어오는 video는 object일거야 >> 유효성 검사
    },
    methods: {
        onVideoClick () {
            this.$emit('videoSelect', this.video)
            // 부모 컴퍼넌트에 'videoSelect'와 this.video 객체 자체를 담아서 보냄
        }
    },
    computed: { // 데이터 수정 하지 않고 가공해서 내보낼때 computed
        thumbnailUrl () {
            return this.video.snippet.thumbnails.default.url
        }
    }
}
</script>

<style scoped>
    li {
        display: flex;
        cursor: pointer;
    
    }

    li:hover {
        background-color: #eee;
    }    
</style>