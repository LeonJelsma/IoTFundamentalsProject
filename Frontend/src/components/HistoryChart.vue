<template>
    <div class="small">
        <button @click="fillData()">Randomize</button>
        <div class="small">
            <line-chart height=10vw width=50vw class="line-graph" :chart-data="datacollection"></line-chart>
        </div>
        <div class="small">
            <line-chart height=10vw width=50vw class="line-graph" :chart-data="datacollection"></line-chart>
        </div>
        <div class="small">
            <line-chart height="10vw" width="50vw" class="line-graph" :chart-data="datacollection"></line-chart>
        </div>
    </div>
</template>

<script>
    import LineChart from '@/charts/LineChart'

    export default {
        components: {
            LineChart
        },
        data() {
            return {
                datacollection: null
            }
        },
        mounted() {
            this.fillData()
        },
        methods: {
            fillData() {
                this.datacollection = {
                    labels: [this.getRandomInt(), this.getRandomInt()],
                    datasets: [
                        {
                            label: 'Temperature',
                            borderColor: '#3283a8',
                            fill: false,
                            data: [this.getRandomInt(), this.getRandomInt()]
                        }, {
                            label: 'Pressure',
                            borderColor: '#b01f1a',
                            fill: false,
                            data: [this.getRandomInt(), this.getRandomInt()]
                        }
                    ],
                    options: {
                        responsive: true,
                        aspectRatio: 0.5,
                    }
                }
            },
            getRandomInt() {
                return Math.floor(Math.random() * 46) + 5
            }
        }
    }
</script>

<style>


</style>
