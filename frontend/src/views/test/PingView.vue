<template>
    <div>
        <h2>{{ msg }}</h2>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                msg: "",
            };
        },
        methods: {
            fetchData() {
                const path = "http://localhost:8000/ping";
                fetch(path, {method:"GET"})
                .then(response => response.json() )
                .then(data => {
                    console.log(data)  //this will display data in our console
                    this.msg = data
                })
                .catch(err => console.log(err.message))
            }
        },
        mounted() {
            this.fetchData()
        }
    }
</script>

