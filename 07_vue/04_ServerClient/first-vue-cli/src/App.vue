<template>
<!-- 반드시, Template 안에는 "단 한개"의 최상단 태그(노드)가 존재해야함. 여기선 div -->
    <div>
        <h1>나쁜말 거름종이</h1>
        <input type="text" v-model="input">
        <p>{{ filteredInput }}</p>
    </div>
</template>

<script>
export default {
    name: 'App',
    // 왜인지는 모르겠지만, 이제부터는 data: function(){return{}}으로 만들어야해
    data: function () {
        return {
            input: 'Type something'
        }
    },
    methods: {},
    computed: {
        filteredInput: function () {
            // [바보] 가 들어오면, ** 로 바꿔서 return 하도록 한다.
            let result = this.input.replace(/바보|멍청이|똥개/gi, '##');
            return `Filtered: ${result}`;
        },
    }
}
</script>

<style></style>
