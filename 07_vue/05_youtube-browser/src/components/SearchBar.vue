<template>
    <div>
        <!-- ()는 커스텀 인자 없으면 안붙임 -->
        <!-- v-on: 을 줄여서 @ -->
        <input @keypress.enter="onInput" type="text">
    </div>
</template>

<script>
    export default { 
        name: 'SearchBar', // new cmpnt: 0.이름적기
        methods: {
            onInput (e) {
                // this.$emit('Event이름', 전송할 값): 자식 cmpnt => 부모 cmpnt 데이터 보냄
                this.$emit('inputChange', e.target.value)
            }
        }
    } 
</script>

<style scoped>
/* scoped: 해당 컴포넌트의 태그들만 영향을 받는다 */
    input {
        width: 75%;
    }

    div {
        text-align: center;
        margin: 20px;
    }

</style>