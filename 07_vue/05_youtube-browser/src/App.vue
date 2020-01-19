<template> 
    <!-- HTML -->
    <!-- template 안에는 무조건 div 하나만 가지는 게 일반적 -->
    <div class="container">
        <h1>Show you Top5 Related Videos</h1>
        <!-- v-on: [자식 component에서 emit하는 이벤트 이름]=""을 줄인 것-->
        <SearchBar @inputChange="onInputChange"></SearchBar>  <!-- step 3. template에 보여주기 -->
        
        <div class="row">
            <VideoDetail :video="selectedVideo"></VideoDetail>

            <!-- 'v-bind:' 는 줄여서 ':' -->
            <!-- props 쓰기0. bind로 데이터를 넘긴다. -->
            <VideoList 
                @videoSelect="onVideoSelect"
                v-bind:videos="videos"
            ></VideoList>
        </div>        
    </div>
</template>

<script>
    import SearchBar from './components/SearchBar'; // step 1. import
    import VideoList from './components/VideoList';
    import VideoDetail from './components/VideoDetail';
    import axios from 'axios';

    const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;

// export default는 new Vue({})와 동일
    export default {
        // 컴포넌트 만들면
        // 0. 이름 적기
        name: 'App',
        components: {
            // 'SearchBar': SearchBar,  // step 2. 부모에게 자식들 등록하기
            // SearchBar: SearchBar,  // '' 사이 띄어쓰기 없으면 이렇게 줄일 수 있고,
            SearchBar,  // 뒤의 값과 같으면 더 줄일 수 있음 => syntactic sugar
            VideoList,
            VideoDetail,
        },
        data() {
            return {
                videos: [],
                selectedVideo: null,
            }
        },
        methods: {
            onInputChange(inputValue) {
                axios.get('https://www.googleapis.com/youtube/v3/search', {
                    params: {
                        key: API_KEY,
                        type: 'video',
                        part: 'snippet',
                        q: inputValue,
                    }
                })
                .then(res => {
                    this.videos = res.data.items // this.videos 처럼 바로접근
                })
            },
            onVideoSelect(video) {
                this.selectedVideo = video;
            }
        }
    }
</script>

<style scoped>
    h1 {
        text-align: center;
        margin: 20px;
    }
    
</style>